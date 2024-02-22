## Resources
* [LiquidInstruments Python API](https://www.liquidinstruments.com/products/apis/python-api/)
* [Moku manuals and datasheets](https://www.liquidinstruments.com/resources/supporting-material/product-documentation/)

## Quick guide
1. Turn on the Moku's and wait until they started up
2. Navigate to the Python program's directory (there is a shortcut on the desktop)
3. (Optional) change the wave settings (freq, delay, phase, etc.) in config.py. 
4. Run script.bat and wait until it is finished.
5. The Moku's should be setup and running now
6. Further control can be done with the Moku software (also shortcut on desktop/taskbar)

## Files
* Main.py
  * Calls all functions required to connect to the Mokus and upload the waveforms
* Moku.py
  * Contains Moku class, which holds methods for connecting, configuration and uploading waveforms of the Mokus
* Waveform.py
  * Contains Waveform class. A waveform object represents a single wavegenerator channel and holds the waveoform formula and arrays
* config.py
  * Configuration settings for Moku and waveforms