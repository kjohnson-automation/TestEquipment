# Agilent Spectrum Analyzer Handler - Supports E4443A
from VisaHandler import Visa_Device
import matplotlib.pyplot as plt

class SpectrumAnalyzer(Visa_Device):
    """ Creates Visa_Device SpectrumAnalyzer """

    def __init__(self, gpib_address):
        """ Creates device """
        super().__init__(gpib_address)

    def get_start_freq(self):
        """ Gets the starting frequency of sweep """
        start_freq = self.query("FREQ:START?")
        return(self.get_num(start_freq))

    def set_start_freq(self, freq:(float, int), prefix:str="GHz"):
        """ Sets the start frequency of sweep """
        out_freq = self.set_num_freq(freq, prefix)
        if out_freq is not None:
            self.write("FREQ:START {0}".format(out_freq))
        else:
            print("Start Freq not set, invalid settings")
            return 1
        return 0

    def get_stop_freq(self):
        """ Gets the stop frequency of sweep """
        stop_freq = self.query("FREQ:STOP?")
        return(self.get_num(stop_freq))

    def set_stop_freq(self, freq:(float, int), prefix:str="GHz"):
        """ Sets the stop frequency of sweep """
        out_freq = self.set_num_freq(freq, prefix)
        if out_freq is not None:
            self.write("FREQ:STOP {0}".format(out_freq))
        else:
            print("Stop Freq not set, invalid settings")
            return 1
        return 0

    def get_freq_span(self):
        """ Gets the span of frequency sweep """
        freq_span = self.query("FREQ:SPAN?")
        return(self.get_num(freq_span))

    def set_freq_span(self, freq:(float, int), prefix:str="GHz"):
        """ Sets the sweep span bandwidth """
        out_freq = self.set_num_freq(freq, prefix)
        if out_freq is not None:
            self.write("FREQ:SPAN {0}".format(out_freq))
        else:
            print("Freq Span not set, invalid settings")
            return 1
        return 0

    def get_center_freq(self):
        """ Gets the center frequency of sweep """
        center_freq = self.query("FREQ:CENT?")
        return(self.get_num(center_freq))
    
    def set_center_freq(self, freq:(float, int), prefix:str="GHz"):
        """ Sets the center frequency of the sweep """
        out_freq = self.set_num_freq(freq, prefix)
        if out_freq is not None:
            self.write("FREQ:CENT {0}".format(out_freq))
        else:
            print("Center Freq not set, invalid settings")
            return 1
        return 0

    def get_attenuation(self):
        """ Returns the SA attenuation """
        attenuation = self.query("POW:ATT?")
        return self.get_num(attenuation)

    def set_attenuation(self, atten:(int,float)=0):
        """ Sets the SA attenuation """
        if 0 <= atten <= 70:
            self.write("POW:ATT {0}".format(atten))
        else:
            print("Selected Attenuation out of range: {0}".format(atten))
            return 1
        return 0

    def get_reference_level(self):
        """ Gets the reference level of the SA """
        ref_level = self.query("DISP:WIND:TRAC:Y:RLEV?")
        return self.get_num(ref_level)

    def set_reference_level(self, ref_level:(int, float)=0):
        """ Sets the reference level of the SA, defaults to 0db """
        if not isinstance(ref_level, (int, float)):
            try:
                ref_level = float(ref_level)
            except ValueError:
                print("Invalid reference level selected: {0}".format(ref_level))
                return 1
        self.write("DISP:WIND:TRAC:Y:RLEV {0}".format(ref_level))
        return 0

    # NOTE: doesn't work yet
    def get_marker_peak(self, marker_num:int=1):
        """ Gets the max amplitude of <marker_num> (defaults to marker 1) """
        if marker_num not in range(1,5):
            print("Invalid marker number: {0}, needs to be [1-4]".format(marker_num))
        marker_peak = self.query("CALC:MARK{0}:MAX".format(marker_num))
        return marker_peak

    # NOTE: doesn't work yet
    def set_marker_operation(self, mode:str="MAX"):
        """ Sets marker type to <MAX|PAR> """
        supported_modes = ["MAX", "PAR"]
        if mode.upper() not in supported_modes:
            print("Invalide mode: {0}, please use one of {1}".format(mode, supported_modes))
            return 1
        self.write("CALC:MARK:PEAK:SEARC:MODE {0}".format(mode.upper()))

    def set_data_format(self, fmt:str="ASC"):
        """ sets output data format, default is ascii <ASC> """
        valid_formats = ["ASC"]
        if fmt not in valid_formats:
            print("Invalid data format: {0}".format(fmt))
            return 1
        self.write("FORM:DATA: {0}".format(fmt))

    def set_sweep_mode(self, mode:str="single"):
        """ Sets the SA to single sweep mode """
        modes = ["single", "sin", "0", 0, "continuous", "cont", "1", 1]
        if mode not in modes:
            print("Invalid sweep mode: {0}, please try any of: {1}".format(mode, modes))
            return 1
        elif mode in modes[:4]:
            mode = 0
        elif mode in modes[4:]:
            mode = 1
        self.write("INIT:CONT {0}".format(mode))

    def get_point_count(self):
        """ Returns the number of points of the sweep """
        points = self.query("SENS:SWE:POIN?")
        return self.get_num(points)


    def get_freq_points(self):
        """ Returns a list of freq points that are being sampled """
        span = self.get_freq_span()
        points = self.get_point_count()
        start_freq = self.get_start_freq()
        freq_values = []
        freq_step = span/points
        for freq in range(int(points)):
            freq_values.append(start_freq + freq*freq_step)
        return freq_values


    def get_sweep_data(self, trace:int=1):
        """ Gets the current sweep data """
        self.set_sweep_mode("single")
        sweep = self.query("TRAC:DATA? TRACE{0}".format(trace))
        y_values = []
        for value in sweep.split(","):
            y_values.append(self.get_num(value))
        x_values = self.get_freq_points()
        self.set_sweep_mode("continuous")
        return [x_values, y_values]

    def plot_sweep_data(self, data, label:str=None, title:str="Single Sweep"):
        """ Displays a plot of the sweep data """
        if label is None:
            label = self.idn
        x = data[0]
        y = data[1]
        plt.plot(x, y, label=label)
        plt.xlabel("Freq")
        plt.ylabel("dBm")
        plt.title(title)
        plt.legend()
        plt.ion()
