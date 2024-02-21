from moku.instruments import ArbitraryWaveformGenerator
import numpy as np
import config as cfg


class Moku:
    def __init__(self, ip: str):
        self.ip = ip
        self.device = ArbitraryWaveformGenerator(ip, force_connect=False)

    def setupChannel(self, channel: int, waveform: np.ndarray) -> None:
        self.setupTrigger(channel)
        self.setupOutputTermination(channel)
        self.uploadWaveform(channel, waveform)

    def uploadWaveform(self, channel: int, waveform: np.ndarray) -> None:
        self.device.generate_waveform(
            channel,
            sample_rate=cfg.SAMPLE_RATE,
            lut_data=list(waveform),
            frequency=1/cfg.CHIRP_DURATION,
            amplitude=1,
            interpolation=True
        )

    def setupTrigger(self, channel: int) -> None:
        self.device.burst_modulate(
            channel,
            trigger_source='External',
            trigger_mode='NCycle',
            burst_cycles=1
        )

    def setupOutputTermination(self, channel: int) -> None:
        self.device.set_output_termination(
            channel,
            termination='50Ohm'
        )

    def closeConnection(self) -> None:
        self.device.relinquish_ownership()
