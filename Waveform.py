import numpy as np
from scipy.signal import chirp


class Waveform:
    """
    Waveforms are created from t=0 to t=1
    The actual duration of the waveforms is adjusted in the Moku software by changing the AWG frequency
    """

    def __init__(self, channel: int, chirp_len: float, f_start: float, f_stop: float, delay: float, rel_ramp_duration: float, n_points: int, phase=0.0):
        self.channel = channel
        self._chirp_len = chirp_len
        self.f_start_uncorr = f_start
        self.f_stop_uncorr = f_stop
        self.f_start = f_start * self.chirp_len
        self.f_stop = f_stop * self.chirp_len
        self.delay = delay
        self.rel_ramp_duration = rel_ramp_duration
        self.phase = phase
        self.timepoints = np.linspace(0, 1, n_points)
        self.wave_array = self.createWaveArray()

    @property
    def chirp_len(self):
        return self._chirp_len
    
    @chirp_len.setter
    def chirp_len(self, new_value):
        self.f_start = self.f_start_uncorr * new_value
        self.f_stop = self.f_stop_uncorr * new_value
        self._chirp_len = new_value 

    def wave(self, t):
        return self._rampEnvelope(t) * chirp(t, self.f_start, 1, self.f_stop, phi=-self.phase)

    def createWaveArray(self) -> np.ndarray:
        return np.array([
            self.wave(t) for t in self.timepoints
        ])

    def saveWaveAsCSV(self, folder: str) -> None:
        file_name = f'wave_chirp_{str(self.f_start)}-{(self.f_stop)}_phase-{str(self.phase)}_delay-{str(self.delay)}_rampdur-{self.rel_ramp_duration}.csv'
        np.savetxt(folder + '\\' + file_name, self.wave_array)

    def _rampEnvelope(self, t):
        if t < self.rel_ramp_duration:
            return t / self.rel_ramp_duration
        elif t > 1 - self.rel_ramp_duration:
            return -(t - 1) / self.rel_ramp_duration
        else:
            return 1
