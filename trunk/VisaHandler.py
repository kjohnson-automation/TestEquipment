# This is the base controller for VISA based devices.
# From here all subClasses of VISA devices will inhereit base functionality to increase productivity and add features

import os, sys, visa

rm = visa.ResourceManager("@py")

class Visa_Device():
    """ Base class for VISA device communications """

    def __init__(self):
        """ Creates the initial connection and checks settings before proceeding """
        pass