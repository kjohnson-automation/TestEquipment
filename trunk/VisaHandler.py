# This is the base controller for VISA based devices.
# From here all subClasses of VISA devices will inhereit base functionality to increase productivity and add features

import os, sys, visa
# import logging

RM = visa.ResourceManager()
AVAILABLE_RESOURCES = RM.list_resources()


class Visa_Device():
    """ Base class for VISA device communications """

    def __init__(self, gpib_address):
        """ Creates the initial connection and checks settings before proceeding """
        global RM, AVAILABLE_RESOURCES
        self.FREQ_PREFIXES = {"ghz": 1e9, "mhz": 1e6, "khz": 1e3, "hz": 1e0}
        resource = None

        for resource in AVAILABLE_RESOURCES:
            if "::{gpib_address}::".format(gpib_address=gpib_address)  in resource:
                self.resource = resource
                break
        if resource is None:
            # TODO: Logging will be added later
            # logger.warning("Resource not found, please check connections and try again")
            print("Resource not found, please check connections and try again")
        else:
            self.device = RM.open_resource(self.resource)
            self.get_idn()

    def query(self, cmd):
        """ Creates the query command for the device """
        try:
            return self.device.query("{0}".format(cmd)).strip("\n")
        except visa.VisaIOError as e:
            # logger.warning("Error trying to query: {0}".format(cmd))
            # logger.warning("VisaIOError: {0}".format(e))
            print("Error trying to query: {0}".format(cmd))
            print("VisaIOError: {0}".format(e))
            return 1

    def write(self, cmd):
        """ Creates the write command for the device """
        try:
            self.device.write("{0}".format(cmd))
            return 0
        except visa.VisaIOError as e:
            # logger.warning("Error trying to write: {0}".format(cmd))
            # logger.warning("VisaIOError: {0}".format(e))
            print("Error trying to write: {0}".format(cmd))
            print("VisaIOError: {0}".format(e))
            return 1

    def read(self):
        """ Reads from the buffer, if there is nothing it will return 0 """
        try:
            return self.device.read()
        except visa.VisaIOError:
            # Not worth logging anything as this could happen often
            return 0

    def flush_buffer(self):
        """ While read returns non-zero values, it continues to read until its empty in order to
            ensure you are read the most up to date response - useful with write and separate read commands
        """
        buffer = self.read()
        while buffer != 0:
            buffer = self.read()
    
    def get_idn(self):
        """ Sets the base idn attribute for the class - *IDN? """
        self.idn = self.query("*IDN?")

    def reset_device(self):
        """ Resets the device - *RST """
        return self.write("*RST")

    def clear_status(self):
        """ Clears the current status on device """
        return self.write("*CLS")

    def operation_complete(self):
        """ Checks for operation to be complete """
        return self.query("*OPC?")

    def wait(self):
        """ Waits for all pending operations to complete before moving forward """
        return self.write("*WAI")

    def close(self):
        """ Closes the device connection """
        self.device.close()
        print("Device disconnected")
        return 0

    def prefix_check(self, prefix):
        """ checks the given prefix """
        if (not isinstance(prefix, str)) or (prefix.lower() not in self.FREQ_PREFIXES.keys()):
            print("Prefix not of valid, please use one of: {0}".format(self.FREQ_PREFIXES))
            return 1
        return prefix

    def set_num_freq(self, freq, prefix):
        """ Returns Hz value of <freq> given <prefix> """
        prefix = self.prefix_check(prefix)
        if prefix != 1:
            return freq * self.FREQ_PREFIXES[prefix.lower()]
        else:
            print("Cannot convert specified freq: {0} with prefix: {1}".format(freq, prefix))
            return None

    def get_num(self, num:str):
        """ Returns the <(int, float)> of freq value """
        try:
            return float(num)
        except ValueError:
            return num

    def _conversion(self, conv):
        """ This is a base convsersion routine that takes bool/str (on/off) and returns int(0/1) """
        if isinstance(conv, int):
            return conv
        if isinstance(conv, bool):
            return int(conv)
        elif isinstance(conv, str):
            if conv.lower() == "off":
                return 0
            elif conv.lower() == "on":
                return 1
        else:
            try:
                return int(conv)
            except ValueError:
                print("Invalid Conversion of {0} to int".format(conv))
                return "NaN"
    