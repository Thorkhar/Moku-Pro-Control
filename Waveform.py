import numpy as np


class Waveform:
    """
    Waveforms are created from t=0 to t=1
    The actual duration of the waveforms is adjusted in the Moku software by changing the AWG frequency
    """
    def __init__(self, f_start: float, f_stop: float, rel_ramp_duration: float, n_points: int, phase=0.0):
        self.f_start = f_start
        self.f_stop = f_stop
        self.phase = phase
        self.rel_ramp_duration = rel_ramp_duration
        self.timepoints = np.linspace(0, 1, n_points)
        self.wave_array = self.createWaveArray()

    def wave(self, t):
        return self._rampEnvelope(t) * self._chirp(t)

    def createWaveArray(self):
        return np.array([
            self.wave(t) for t in self.timepoints
        ])

    def _freq(self, t):
        return (self.f_stop - self.f_start) * t + self.f_start*2 # Figure out why the hell this factor 2 has to be here

    def _chirp(self, t):
        return np.sin(2 * np.pi * self._freq(t) * t - self.phase)

    def _rampEnvelope(self, t):
        if t < self.rel_ramp_duration:
            return t / self.rel_ramp_duration
        elif t > 1 - self.rel_ramp_duration:
            return -(t - 1) / self.rel_ramp_duration
        else:
            return 1
