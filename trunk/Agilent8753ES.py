from VisaHandler import Visa_Device
import time

class NetworkAnalzyer(Visa_Device):
    """ Creates class object for Network Analyzer

    Args:
        Visa_Device ([class]): [Network Analzyer class object that extends Visa_Device]
    """

    def __init__(self, gpib_address:int):
        """[Initializes said device using <gpib_address>]

        Args:
            gpib_address ([int]): [The GPIB address of the NWA]
        """
        super().__init__(gpib_address)

    def get_start_freq(self):
        """[returns start frequency of NWA sweep]
        """
        start_freq = self.query("STAR?")
        return self.get_num(start_freq)

    def get_stop_freq(self):
        """ returns stop frequency of NWS sweep
        """
        return self.get_num(self.query("STOP?"))

    def get_center_freq(self):
        """ Gets center frequency of NWS Sweep
        """
        return self.get_num(self.query("CENT?"))

    def get_sweep_points(self):
        """ Gets the number of data points for the NWS sweep
        """
        return self.get_num(self.query("POIN?"))
    
    def get_averaging_status(self):
        """ Returns True/False if averaging is On/Off
        """
        # 0 - Off, 1 - On
        averaging = self.get_num(self.query("AVERO?"))
        # bool(0) = False, bool(1) = True
        return bool(averaging)

    def set_start_freq(self, freq:(int,float), prefix:str="hz"):
        """ Sets the start frequency of the sweep to <freq>

        Args:
            freq ([int/float]): [The starting freqency for the NWA Sweep, best to provide in Hz]
            prefix (str, optional): [The Frequency prefix, can be ghz, mhz, khz, hz]. Defaults to "hz".

        Returns:
            [int]: [0 - successful, 1 - unsuccessful]
        """
        freq = self.set_num_freq(freq, prefix)
        if freq < 30:
            print(f"Invalid Starting frequency: {freq} - must be greater than 30Hz")
            return -1
        return self.write(f"STAR {freq}")

    def set_stop_freq(self, freq:(int,float), prefix:str="Hz"):
        """ Sets the stop frequency of the sweep to <freq>

        Args:
            freq ([int/float]): [The stop freqency for the NWA Sweep, best to provide in Hz]
            prefix (str, optional): [The Frequency prefix, can be ghz, mhz, khz, hz]. Defaults to "hz".

        Returns:
            [int]: [0 - successful, 1 - unsuccessful]
        """
        freq = self.set_num_freq(freq, prefix)
        if freq > 6000000000:
            print(f"Invalide stop frequency: {freq} - must be less than 6GHz")
            return -1
        return self.write(f"STOP {freq}")

    def set_center_freq(self, freq:(int,float), prefix:str="hz"):
        """ Sets the center frequency of the sweep to <freq>

        Args:
            freq ([int/float]): [The center freqency for the NWA Sweep, best to provide in Hz]
            prefix (str, optional): [The Frequency prefix, can be ghz, mhz, khz, hz]. Defaults to "hz".

        Returns:
            [int]: [0 - successful, 1 - unsuccessful]
        """
        freq = self.set_num_freq(freq, prefix)
        if not 30 < freq < 6000000000:
            return self.write(f"CENT {freq}")
        return -1

    def set_averaging(self, averaging:bool):
        """ Sets AVERAGING to <averaging> - first checks state, then toggles if needed

        Args:
            averaging (bool): True - enable, False - disable
        """
        averaging_state = self.get_averaging_status()
        if averaging_state != averaging:
            return self.write(f"AVERO {int(averaging)}")
        return 0

    def get_reference_position(self):
        """ Returns the reference position of the measurement sweep
        """
        return self.get_num(self.query("REFP?"))

    def get_reference_value(self):
        """ Returns the reference value of the measurement sweep
        """
        return self.get_num(self.query("REFV?"))

    def set_reference_position(self, pos:(int,float)):
        """ Sets the reference position to <pos>

        Args:
            pos (int,float): new reference position in dB
        """
        return self.write(f"REFP {pos}")

    def set_reference_value(self, value:(int,float)):
        """ Sets the reference value to <value>

        Args:
            value (int,float): new reference value in dB
        """
        return self.write(f"REFV {value}")

