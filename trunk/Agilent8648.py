# Signal Generator 8648/C Handler
import re
import numpy as np
from VisaHandler import Visa_Device

PREFIXES = {"ghz": 1e9, "mhz": 1e6, "khz": 1e3, "hz": 1e0}

class SignalGenerator(Visa_Device):
    """ Creates Visa_Device SignalGenerator """

    def __init__(self, gpib_address):
        """ Creates the actual device """
        super().__init__(gpib_address)

    def prefix_check(self, prefix):
        """ checks the given prefix """
        if (not isinstance(prefix, str)) or (prefix.lower() not in PREFIXES.keys()):
            print("Prefix not of valid, please use one of: {0}".format(PREFIXES))
            return 1
        return prefix

    def convert_frequency(self, raw_freq:str, prefix:str):
        """ Converts string rsp frequency to int with base prefix """
        global PREFIXES
        try:
            hz = float(raw_freq)
        except ValueError:
            print("Can't handle {0} yet...".format(raw_freq))
            return raw_freq
        return hz/PREFIXES[prefix.lower()]


    def get_frequency(self, prefix:str="ghz"):
        """ Returns the frequency in <freq> at specified prefex
            GHz: 1e9
            MHz: 1e6
            KHz: 1e3
            Hz:  1e0
        """
        global PREFIXES
        prefix = self.prefix_check(prefix)
        if prefix == 1:
            return 1
        raw_freq = self.query("FREQ?")
        return self.convert_frequency(raw_freq, prefix)
    
    def set_frequency(self, freq:(float, int), prefix:str="ghz"):
        """ Sets the signal generator to the specified frequency with prefix <prefix>
            If no prefix is given, assumed GHz
        """
        prefix = self.prefix_check(prefix)
        

