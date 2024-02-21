from moku.instruments import ArbitraryWaveformGenerator
import numpy as np


class Moku:
    def __init__(self, ip: str, sample_rate: str):
        self.ip = ip
        self.device = ArbitraryWaveformGenerator(ip, force_connect=False)
        self.sample_rate = sample_rate

    def uploadWaveform(self, channel: int, waveform: np.ndarray) -> None:
        self.device.generate_waveform(
            channel,
            sample_rate='1.25Gs',
            lut_data=list(waveform),
            frequency=25,
            amplitude=1,
            phase=0,
            offset=0,
            interpolation=False
        )

    def closeConnection(self):
        self.device.relinquish_ownership()
