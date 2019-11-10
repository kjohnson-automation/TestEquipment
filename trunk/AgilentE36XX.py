# Power Supply E36XX Handler
#pylint: disable=import-error
from VisaHandler import Visa_Device

MAX_VOLTAGE = 12
MAX_CURRENT = 3
# NOTE: Defaults to P6V output
AVAILABLE_OUTPUTS = ["P6V", "P25V", "N25V"]


class PowerSupply(Visa_Device):
    """ Creates Visa_Device SignalGenerator """

    def __init__(self, gpib_address):
        """ Creates the actual device """
        super().__init__(gpib_address)

    def set_port(self, interface:int=0):
        """ Sets <interface> to num, numbers coorespond to AVAILABLE_OUTPUTS """
        global AVAILABLE_OUTPUTS
        if not isinstance(interface, int):
            if interface not in AVAILABLE_OUTPUTS:
                print("Invalid Output Selection, please choose [0, 1, 3] or {0}".format(AVAILABLE_OUTPUTS))
                return 1
            else:
                interface = AVAILABLE_OUTPUTS[interface]
        check = self._check_port(interface)
        if check == 0:
            return 0
        self.write("INST {0}".format(interface))
        return self._check_port(interface)

    def _check_port(self, interface):
        """ Called from set_port to make sure it was set correctly """
        port = self.query("INST?")
        if interface not in port:
            return 1
        else:
            return 0

    def get_output_state(self, interface:int=0):
        fail = self.set_port(interface)
        if fail:
            print("Failed to set output interface")
            return 1
        output_state = self.query("OUPT?")
        if output_state == "0":
            return "Off"
        if output_state == "1":
            return "On"

    def toggle_output(self, interface:int=0, toggle:str="off"):
        """ Toggles PSU <interface> output On/Off """
        toggle = self._conversion(toggle)
        if toggle == "NaN":
            print("Invalid Toggle switch: {0} - Needs On/Off".format(toggle))
            return 1
        fail = self.set_port(interface)
        if fail:
            print("Invalid interface: {0}".format(interface))
            return 1
        self.write("OUTP {0}".format(toggle))
        return self.get_output_state(interface)

    def set_voltage_output(self, interface:int=0, voltage:float=0):
        """ Sets the output voltage at <interface> to <voltage> """
        global MAX_VOLTAGE
        fail = self.set_port(interface)
        if fail:
            print("Failed to set output interface")
            return 1
        if voltage > MAX_VOLTAGE:
            print("Voltage over MAX voltage")
            return 1
        voltage_setting = self.check_set_voltage(interface)
        if voltage == voltage_setting:
            return 0
        self.write("OUPT:VOLT {0}".format(voltage))
        return self.check_set_voltage(interface)

    def check_set_voltage(self, interface:int=0):
        """ Checks the current voltage setting on <interface> """
        fail = self.set_port(interface)
        if fail:
            return 1
        return self.query("OUTP:VOLT?")

    def set_current_limit(self, interface:int=0, current:float=1):
        """ Sets <interface> current limit in AMPS """
        current_limit = self.get_current_limit(interface)
        if current == current_limit:
            return 0
        self.write("CURR {0}".format(current))
        return self.get_current_limit(interface)

    def get_current_limit(self, interface:int=0):
        """ Gets the current <interface> current limit """
        fail = self.set_port(interface)
        if fail:
            return 1
        return float(self.query("CURR?"))