""" OIP3 Test Script """

""" Initial Test Sequence:
Limiter tests:

	Test frequencies:
		(2.395 and 2.405GHz)
		(2.995 and 3.005GHz)
	Input Power:
		[-10dBm, -5dBm, 0dBm, +5dBm, +10dBm, +15dB]m
"""
# Need to add GUI from Mac Windows
import sys
from datetime import datetime
import time

from frange import frange

from AgilentE36XX import PowerSupply
from Agilent8648 import SignalGenerator
from AgilentE4443 import SpectrumAnalyzer

class LimiterTest():
    """ Defines the limiter test criteria """
    def __init__(self, **kwargs):
        """ Configures all test instance requirements:
            Expected/Valid kwargs:
            p_no, lot, temp, tester
            sg1_gpib, sg2_gbib, ps1_gbib, ps2_gpib, sa_gpib
            sg1_start_f, sg1_stop_f, sg1_step_f, sg1_start_p, sg1_stop_p, sg1_step_p
            sg2 ...
            ps1_start_v, ps1_stop_v, ps1_step_v
            ps2 ...
            sa_vb, sa_rb
            output_file
        """
        # If output file is None: test will be saved as Limiter_test{date}.csv
        kwargs = kwargs["kwargs"]
        siggen1_gpib = kwargs.get("sg1_gpib", None)
        print("sg1_gpib: {0}".format(siggen1_gpib))
        
        siggen2_gpib = kwargs.get("sg2_gpib", None)
        print("sg2_gpib: {0}".format(siggen2_gpib))

        ps1_gpib = kwargs.get("ps1_gpib", None)
        print("ps1_gpib: {0}".format(ps1_gpib))

        ps2_gpib = kwargs.get("ps2_gpib", None)
        print("ps2_gpib: {0}".format(ps2_gpib))

        sa_gpib = kwargs.get("sa_gpib", None)
        print("sa_gpib: {0}".format(sa_gpib))

        output_file = kwargs.get("output_file", None)

        if siggen1_gpib is not None:
            self.siggen1 = SignalGenerator(siggen1_gpib)
            self.set_sg1_vars(kwargs=kwargs)
        
        if siggen2_gpib is not None:
            self.siggen2 = SignalGenerator(siggen2_gpib)
            self.set_sg2_vars(kwargs=kwargs)

        if ps1_gpib is not None:
            self.ps1 = PowerSupply(ps1_gpib)
            self.set_ps1_vars(kwargs=kwargs)

        if ps2_gpib is not None:
            self.ps2 = PowerSupply(ps2_gpib)
            self.set_ps2_vars()

        if sa_gpib is None:
            print("Spectrum Analyzer GPIB is not defined, it is required")
            sys.exit("No Spectrum Analyzer GPIB defined")
        self.spec_analyzer = SpectrumAnalyzer(sa_gpib)

        self.set_sa_vars(kwargs=kwargs)

        if output_file is None:
            now = datetime.now().strftime("%m%d%Y_%H%M")
            output_file = "Limiter_test{0}.csv".format(now)
            print("Creating Write file: {0}".format(output_file))
            self.write_file = open(output_file, "w")

        self.write_test_info(kwargs=kwargs)

        #### NOTE: EDIT FREQUENCIES HERE - FREQUENCIES IN GHz! ####
        # self.frequency_pairs = [[2.395, 2.405], [2.995, 3.005]]
        # self.power_levels = [-10, -5, 0, 5, 10, 15]
        ############################################################

    def write_test_info(self, **kwargs):
        """ Writes the base test info to the text file on line 1, csv """
        #p_no, lot, temp, tester
        kwargs = kwargs["kwargs"]
        part_no = kwargs.get("p_no", None)
        lot = kwargs.get("lot", None)
        temp = kwargs.get("temp", None)
        tester = kwargs.get("tester", None)
        self.write_file.write("Part Number, {0}, Lot, {1}, Temp, {2}, Tester, {3}\n".format(part_no, lot, temp, tester))

    def set_sg1_vars(self, **kwargs):
        """ Sets the signal generator 1 freq and power values """
        kwargs = kwargs["kwargs"]
        self.start_freq_1 = float(kwargs.get("sg1_start_f", None))
        self.stop_freq_1 = float(kwargs.get("sg1_stop_f", None))
        self.step_freq_1 = float(kwargs.get("sg1_step_f", None))
        self.start_pow_1 = float(kwargs.get("sg1_start_p", None))
        self.stop_pow_1 = float(kwargs.get("sg1_stop_p", None))
        self.step_pow_1 = float(kwargs.get("sg1_step_p", None))

    def set_sg2_vars(self, **kwargs):
        """ Sets the signal generator 2 freq and power values """
        kwargs = kwargs["kwargs"]
        self.start_freq_2 = float(kwargs.get("sg2_start_f", None))
        self.stop_freq_2 = float(kwargs.get("sg2_stop_f", None))
        self.step_freq_2 = float(kwargs.get("sg2_step_f", None))
        self.start_pow_2 = float(kwargs.get("sg2_start_p", None))
        self.stop_pow_2 = float(kwargs.get("sg2_stop_p", None))
        self.step_pow_2 = float(kwargs.get("sg2_step_p", None))

    def set_ps1_vars(self, **kwargs):
        """ Sets the power supply 1 voltage values """
        kwargs = kwargs["kwargs"]
        self.start_v_1 = kwargs.get("ps1_start_v", None)
        self.stop_v_1 = kwargs.get("ps1_stop_v", None)
        self.step_v_1 = kwargs.get("ps1_step_v", None)

    def set_ps2_vars(self, **kwargs):
        """ Sets the power supply 2 voltage values """
        kwargs = kwargs["kwargs"]
        self.start_v_2 = kwargs.get("ps2_start_v", None)
        self.stop_v_2 = kwargs.get("ps2_stop_v", None)
        self.step_v_2 = kwargs.get("ps2_step_v", None)

    def set_sa_vars(self, **kwargs):
        """ Sets the spectrum analyzer values """
        kwargs = kwargs["kwargs"]
        # NOTE: Not used right now
        self.video_bw = kwargs.get("sa_vb", None)
        self.res_bw = kwargs.get("sa_rb", None)

    def close_file(self):
        """ Closes write file """
        self.write_file.close()

    def write_sweep_data(self, data:list):
        """ writes <data> (x,y) to self.write_file
            Line 1: x
            Line 2: y
        """
        self.write_file.write("{0}\n".format(",".join(map(str, data[0]))))
        self.write_file.write("{0}\n\n".format(",".join(map(str, data[1]))))

    def disable_signal_output(self):
        """ Turns off both signal generator outputs """
        self.siggen1.set_output_state(False)
        self.siggen2.set_output_state(False)

    def enable_signal_output(self):
        """ Turns on both signal generator outputs """
        self.siggen1.set_output_state(True)
        self.siggen2.set_output_state(True)

    def set_freq_pair(self, freq_pair:list):
        """ Reads in <freq_pair>:
            - sets siggen1 = <freq_pair>[0]
            - sets siggen2 = <freq_pair>[1]
        """
        if len(freq_pair) != 2:
            print("Invalid freq length")
            return 1
        s1_fail = self.siggen1.set_frequency(freq_pair[0])
        s2_fail = self.siggen2.set_frequency(freq_pair[1])
        return any([s1_fail, s2_fail])

    def set_power(self, power:(int, float)):
        """ Sets both signal generators to <power> """
        s1_fail = self.siggen1.set_power(power)
        s2_fail = self.siggen2.set_power(power)
        return any([s1_fail, s2_fail])

    def set_sa_parameters(self, freq_pair:list, power:(float, int)):
        """ Sets the spectrum analyzer for 100MHz below F1 and 100MHz above F2
            Can also adjust ref power based on input power range as well as
            attenuation but this is not handled yet
        """
        # Frequencies +/- 100MHz since default unit is GHz
        start_fail = self.spec_analyzer.set_start_freq(freq_pair[0]-.05)
        stop_fail = self.spec_analyzer.set_stop_freq(freq_pair[1]+.05)
        return any([start_fail, stop_fail])
    
    def map_freq_pairs(self):
        """ maps the sets of frequencies to a list of lists [[1,2], [3,4], etc...] """
        sg1_freqs = list(frange(self.start_freq_1, self.stop_freq_1, self.step_freq_1))
        sg2_freqs = list(frange(self.start_freq_2, self.stop_freq_2, self.step_freq_2))
        return list(zip(sg1_freqs, sg2_freqs))

    def map_power_levels(self):
        """ creates the power level ranges - only based on signal generator 1 right now """
        power_levels = list(frange(self.start_pow_1, self.stop_pow_1, self.step_pow_1))
        return power_levels

    def test_OIP3(self):
        """ Tests the defined <self.frequency_pairs> and <self.power_levels>
            for OIP3 measurements and writes a csv file with data and plots
            results
        """
        frequency_pairs = self.map_freq_pairs()
        print(frequency_pairs)
        power_levels = self.map_power_levels()
        print(power_levels)
        # Diables siggen outputs before setting things - just in case
        self.disable_signal_output()
        self.spec_analyzer.set_reference_level(0)
        for freq_pair in frequency_pairs:
            for power in power_levels:
                print("Testing frequencies: {0} - {1}".format(
                    freq_pair[0], freq_pair[1]))
                print("Power Level: {0}dBm".format(power))
                fail = self.set_freq_pair(freq_pair)
                if fail:
                    print("Setting Frequencies Failed - Stopping Test")
                    return "FAILED at {0} - {1}dBm".format(freq_pair, power)
                fail = self.set_power(power)
                if fail:
                    print("Failed setting signal generator power: {0}".format(power))
                    return "FAILED at {0} - {1}dBm".format(freq_pair, power)
                fail = self.set_sa_parameters(freq_pair, power)
                if fail:
                    print("Failed setting up spectrum analyzer")
                    return "FAILED at {0} - {1}dBm".format(freq_pair, power)
                self.enable_signal_output()
                time.sleep(2)
                [x, y] = self.spec_analyzer.get_sweep_data()
                self.write_sweep_data([x, y])
                label = "{0}-{1} @ {2}dBm".format(freq_pair[0],
                        freq_pair[1], power)
                # self.spec_analyzer.plot_sweep_data([x,y], label)
                self.disable_signal_output()
        print("Testing Complete")
        print("Data File: {0}".format(self.write_file))
        self.close_file()
        return self.write_file

