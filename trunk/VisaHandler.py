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
        index = None
        for resource in AVAILABLE_RESOURCES:
            if "::{gpib_address}::".format(gpib_address=gpib_address)  in resource:
                index = AVAILABLE_RESOURCES.index(resource)
        if index is None:
            # TODO: Logging will be added later
            # logger.warning("Resource not found, please check connections and try again")
            print("Resource not found, please check connections and try again")
        else:
            self.device = RM.open_resource(AVAILABLE_RESOURCES[index])
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
            # Not worth logging anything as this could happen a bit
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