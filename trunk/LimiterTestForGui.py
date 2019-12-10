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
from datetime import datetime
import time

from Agilent8648 import SignalGenerator
from AgilentE4443 import SpectrumAnalyzer

class LimiterTest():
    """ Defines the limiter test criteria """
    def __init__(self, **kwargs):
        """ Configures all test instance requirements:
            Expected/Valid kwargs:
            sg1_gpib, sg2_gbib, ps1_gbib, ps2_gpib, sa_gpib
            sg1_start_f, sg1_stop_f, sg1_step_f, sg1_start_p, sg1_stop_p, sg1_step_p
            sg2 ...
            ps1_start_v, ps1_stop_v, ps1_step_v
            ps2 ...
            sa_vb, sa_rb
            output_file
        """
        # If output file is None: test will be saved as Limiter_test{date}.csv
        siggen1_gpib = kwargs.get("sg1_gpib", None)
        siggen2_gpib = kwargs.get("sg2_gpib", None)

        ps1_gpib = kwargs.get("ps1_gpib", None)
        ps2_gpib = kwargs.get("ps2_gpib", None)

        sa_gpib = kwargs.get("sa_gpib", None)

        print(kwargs)
        input("Waiting here")
        if output_file is None:
            now = datetime.now().strftime("%m%d%Y_%H%M")
            output_file = "Limiter_test{0}.csv".format(now)
            print("Creating Write file: {0}".format(output_file))
            self.write_file = open(output_file, "w")
        self.siggen1 = SignalGenerator(siggen1_gpib)
        self.siggen2 = SignalGenerator(siggen2_gpib)
        self.spec_analyzer = SpectrumAnalyzer(sa_gpib)
        # edit_freq = input("Do you want to change the frequenices? (Y/N)")
        # if "y" in edit_freq.lower():
        #     self.frequency_pairs = []
        #     response = ""
        #     while "n" not in response:
        #         response = input("Input frequency pairs - enter \"n\" to stop").split(",")
        #         self.frequency_pairs.append(response)
        # else:

        #### NOTE: EDIT FREQUENCIES HERE - FREQUENCIES IN GHz! ####
        self.frequency_pairs = [[2.395, 2.405], [2.995, 3.005]]
        self.power_levels = [-10, -5, 0, 5, 10, 15]
        ############################################################

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

    def test_OIP3(self):
        """ Tests the defined <self.frequency_pairs> and <self.power_levels>
            for OIP3 measurements and writes a csv file with data and plots
            results
        """

        # Diables siggen outputs before setting things - just in case
        self.disable_signal_output()
        self.spec_analyzer.set_reference_level(0)
        for freq_pair in self.frequency_pairs:
            for power in self.power_levels:
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
                self.spec_analyzer.plot_sweep_data([x,y], label)
                self.disable_signal_output()
        print("Testing Complete")
        print("Data File: {0}".format(self.write_file))
        self.close_file()
        _ = input("Any Key To Continue...")

def main():
    """ Main routine that starts the testing """
    base_elements = {"sg1_gpib":19, "sg2_gpbi":21, "sa_gpib":18}
    # test= LimiterTest()
    test = LimiterTest(kwargs=base_elements)
    print("Starting OIP3 Test")
    test.test_OIP3()

if __name__=="__main__":
    main()