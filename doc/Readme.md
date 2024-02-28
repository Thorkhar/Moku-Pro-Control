## Resources
* [LiquidInstruments Python API](https://www.liquidinstruments.com/products/apis/python-api/)
* [Moku manuals and datasheets](https://www.liquidinstruments.com/resources/supporting-material/product-documentation/)

## Quick guide
1. Turn on the Moku's and wait until they started up
2. Navigate to the Python program's directory (there is a shortcut on the desktop)
3. (Optional) change the wave settings (freq, delay, phase, etc.) in config.json. 
4. Run Run.bat and wait until it is finished (A graph with ch1's waveform pops up once done).
5. The Moku's should be setup and running now
6. Further control can be done with the Moku software (also shortcut on desktop/taskbar)

## Files
* main.py
  * Calls all functions required to connect to the Mokus and upload the waveforms
* functions.py
  * Contains some functions used in main.py
* Moku.py
  * Contains Moku class, which holds methods for connecting, configuration and uploading waveforms of the Mokus
* Waveform.py
  * Contains Waveform class. A waveform object represents a single wavegenerator channel and holds the waveoform formula and arrays
* config.py
  * Loads settings from config.json
* config.json
  * Here you can adjust the settings, such as the Moku IP addresses but also the waveform phases, frequencies, etc.
* requirements.txt
  * Python module requirements file for pip
* Run.bat
  * Simple batch script which starts main.py