import numpy as np
import matplotlib.pyplot as plt
from Waveform import Waveform
from Moku import Moku
import config as cfg

'''moku_morgul = Moku(
    cfg.MOKU_MORGUL_IP,
    cfg.SAMPLE_RATE
)

moku_morgul.closeConnection()'''

channels = []
for ch in range(8):
    channels.append(
        Waveform(
            ch,
            cfg.F_START,
            cfg.F_STOP,
            cfg.REL_RAMP_DURATION,
            cfg.N_POINTS,
            ch * 45
        )
    )


for ch in channels:
    np.savetxt(
        f'waveform_ch{str(ch.channel)}.csv',
        ch.wave_array
    )

plt.plot(channels[0].timepoints, channels[0].wave_array)
plt.show()