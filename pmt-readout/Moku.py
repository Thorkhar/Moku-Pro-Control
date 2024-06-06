from moku.instruments import MultiInstrument, TimeFrequencyAnalyzer, ArbitraryWaveformGenerator

class Moku:
    def __init__(self, ip: str) -> None:
        self.mim = MultiInstrument(ip, force_connect= True)
        self.time_analyzer_1 = self.mim.set_instrument(1, TimeFrequencyAnalyzer)
        self.time_analyzer_2 = self.mim.set_instrument(2, TimeFrequencyAnalyzer)
        self.awg_1 = self.mim.set_instrument(3, ArbitraryWaveformGenerator)
        self.awg_2 = self.mim.set_instrument(4, ArbitraryWaveformGenerator)

        self.time_analyzer_1.set_connections([
            {"source": "Input1", "destination": "Slot1InA"},
            {"source": "Input2", "destination": "Slot1InB"}
        ])

        self.time_analyzer_2.set_connections([
            {"source": "Input3", "destination": "Slot2InA"},
            {"source": "Input4", "destination": "Slot2InB"}
        ])

        self.awg_1.set_connections([
            {"source": "Slot3OutA", "destination": "Output1"},
            {"source": "Slot3OutB", "destination": "Output2"}
        ])

        self.awg_2.set_connections([
            {"source": "Slot4OutA", "destination": "Output3"},
            {"source": "Slot4OutB", "destination": "Output4"}
        ])

        for ch in range(1, 4):
            self.mim.set_frontend(ch, impedance="50Ohm", attenuation="0dB", coupling="DC")
            self.mim.set_output(ch, "0dB")

        self._timeAnalyzerSetup(self.time_analyzer_1)
        self._timeAnalyzerSetup(self.time_analyzer_2)


    def _timeAnalyzerSetup(self, device):
        device.clear_data()
        device.set_defaults()
        device.set_acquisition_mode(mode="Windowed", window_length=1)
        device.set_histogram(start_time=0, stop_time=0.1)
        for i in [1, 2]:
            device.set_event_detector(i, source=f"Input{str(i)}", threshold="0.1", edge="Rising")
