# Signal Generator 8648/C Handler
import re
import numpy as np
#pylint: disable=import-error
from VisaHandler import Visa_Device

MAX_POWER = 20
POWER_UNITS = ["dbm", "db"] # more can be added but I think these are the common ones

class SignalGenerator(Visa_Device):
    """ Creates Visa_Device SignalGenerator """

    def __init__(self, gpib_address):
        """ Creates the actual device """
        super().__init__(gpib_address)

    def convert_frequency(self, raw_freq: str, prefix: str):
        """ Converts string rsp frequency to int with base prefix """
        try:
            hz = float(raw_freq)
        except ValueError:
            print("Can't handle {0} yet...".format(raw_freq))
            return raw_freq
        return hz/self.FREQ_PREFIXES[prefix.lower()]


    def get_frequency(self, prefix:str="ghz"):
        """ Returns the frequency in <freq> at specified prefex
            GHz: 1e9
            MHz: 1e6
            KHz: 1e3
            Hz:  1e0
        """
        prefix = self.prefix_check(prefix)
        if prefix == 1:
            return 1
        raw_freq = self.query("FREQ?")
        return self.convert_frequency(raw_freq, prefix)

    def set_frequency(self, freq:(float, int), prefix:str="ghz"):
        """ Sets the signal generator to the specified frequency with prefix <prefix>
            If no prefix is given, assumed GHz
        """
        return self.write("FREQ:CW {0} {1}".format(freq, prefix))

    def get_output_state(self):
        """ Checks to see if RF is enabled/disabled
            1: On
            0: Off
        """
        return self.query("OUTP:STAT?")

    def set_output_state(self, target:bool):
        """ Sets the output to <target>:
            False: Off
            True: On
        """
        if not isinstance(target, bool):
            target_type = type(target)
            if target_type is (int, float):
                if int(target) not in [0, 1]:
                    print("Cannot interpret target output status: {0}, try True/False".format(target))
                    return 1
            elif target_type is str:
                if target.lower() == "off":
                    target = 0
                elif target.lower() == "on":
                    target = 1
                else:
                    print("Cannot interpret target output status: {0}, try True/False".format(target))
                    return 1
        return self.write("OUTP:STAT {0}".format(int(target)))

    def get_power(self):
        """ Returns the CW power in dBm """
        return float(self.query("POW:AMPL?"))

    def set_power(self, power:float, unit:str="dbm"):
        """ Sets the CW power to <power><units> """
        global POWER_UNITS
        if unit.lower() not in POWER_UNITS:
            print("Invalid power unit: {0}, use on of {1}".format(unit, POWER_UNITS))
            return 1
        # TODO: EDIT FOR proper checking
        if float(power) > MAX_POWER:
            print("POWER TOO HIGH: EXITING")
            return 1
        return self.write("POW:AMPL {0} {1}".format(power, unit))


