import numpy as np
import matplotlib.pyplot as plt
from Waveform import Waveform
import config as cfg


wave1 = Waveform(
    cfg.F_START,
    cfg.F_STOP,
    cfg.REL_RAMP_DURATION,
    cfg.N_POINTS
)

wave2 = Waveform(
    cfg.F_START,
    cfg.F_STOP,
    cfg.REL_RAMP_DURATION,
    cfg.N_POINTS,
    45
)

plt.plot(wave1.timepoints, wave1.wave_array)
plt.plot(wave2.timepoints, wave2.wave_array)
plt.show()

np.savetxt('waveform1.csv', wave1.wave_array)
np.savetxt('waveform2.csv', wave2.wave_array)
