import matplotlib.pyplot as plt
from config import settings as cfg
from Waveform import Waveform

def exitHandler(devices_dict: dict) -> None:
    for key, moku in devices_dict.items():
        try:
            moku.closeConnection()
        except Exception as ex:
            print(ex)
            print('No existing connection to %s' % key)


def findCorrespondingMoku(channel: int) -> str:
    if 1 <= channel <= 4:
        return cfg['MOKU_A_NAME']
    else:
        return cfg['MOKU_B_NAME']


def showExampleWave(waveform: Waveform):
    plt.plot(
        [t * cfg['CHIRP_DURATION'] for t in waveform.timepoints],
        waveform.wave_array
    )
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (V)')
    plt.show()
