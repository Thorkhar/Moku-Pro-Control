from moku.instruments import ArbitraryWaveformGenerator
import numpy as np


class Moku:
    def __init__(self, ip:str):
        self.ip = ip
        self.device = ArbitraryWaveformGenerator(ip, force_connect=False)

    def test_waveform(self, t: float):
        pass

