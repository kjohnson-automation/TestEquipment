# TestEquipment
Library of test equipment handlers.

Language: Python 3.7.x (Current working version 3.7.4)
Available here: https://www.python.org/downloads/release/python-374/
Libraries that will be used and therefore need to be installed (continually updated list):
- numpy
- scipy
- pyvisa
- matplotlib

To install these packages, using terminal/cmd:
- `pip install <library>`

This library will be used to control and number of pieces of equipment.

Current supported library with explicit functionality:
- Agilent E4443; Spectrum Analyzer
- Agilent 8648; Signal Generator

Current library also supports any base visa device through VisaHandler

Examples:
```python
import AgilentE4443
spectrum_analyzer = AgilentE4443.SpectrumAnalyzer(gpib_address)
spectrum_analzyer.set_center_frequency(2.484) # Defaults to GHz
spectrum_analyzer.set_freq_span(1) # Defaults to GHz
data = spectrum_analzyer.get_sweep_data() # retrieves sweep data
spectrum_analyzer.plot_sweep_data(data) # plots using matplotlib
```

```python
import Agilent8648
sig_gen = Agilent8648.SignalGenerator(gpib_address)
f1 = sig_gen.get_frequency() #gets current tx frequency
if f1 != desired_freq:
    sig_gen.set_frequency(desired_freq) # if not already set, sets tx freq to desired
tx_power = sig_gen.get_power() # gets current tx power
if tx_power != desired_power:
    sig_gen.set_power(desired_power) # if not already set, sets tx power to desired
if sig_gen.get_output_state() != 1:
    sig_gen.set_output_state(1) #if power is not enabled, turns tx on
```
