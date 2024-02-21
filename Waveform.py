import numpy as np
from scipy.signal import chirp


class Waveform:
    """
    Waveforms are created from t=0 to t=1
    The actual duration of the waveforms is adjusted in the Moku software by changing the AWG frequency
    """

    def __init__(self, channel: int, f_start: float, f_stop: float, delay: float, rel_ramp_duration: float, n_points: int, phase=0.0):
        self.channel = channel
        self.f_start = f_start
        self.f_stop = f_stop
        self.delay = delay
        self.rel_ramp_duration = rel_ramp_duration
        self.phase = phase
        self.timepoints = np.linspace(0, 1, n_points)
        self.wave_array = self.createWaveArray()

    def wave(self, t):
        return self._rampEnvelope(t) * chirp(t, self.f_start, 1, self.f_stop, phi=self.phase)

    def createWaveArray(self):
        return np.array([
            self.wave(t) for t in self.timepoints
        ])

    def _rampEnvelope(self, t):
        if t < self.rel_ramp_duration:
            return t / self.rel_ramp_duration
        elif t > 1 - self.rel_ramp_duration:
            return -(t - 1) / self.rel_ramp_duration
        else:
            return 1
