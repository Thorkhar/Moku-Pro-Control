from Waveform import Waveform
from Moku import Moku
from config import settings as cfg
import matplotlib.pyplot as plt
import atexit


def exitHandler(devices_dict: dict) -> None:
    for key, moku in devices_dict.items():
        try:
            moku.closeConnection()
        except Exception as ex:
            print(ex)
            print('No existing connection to %s' % key)


def _findCorrespondingMoku(channel: int) -> str:
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


devices = {}
atexit.register(exitHandler, devices)

if __name__ == "__main__":
    # Attempt to establish connection with Moku's
    try:
        devices = {
            cfg['MOKU_A_NAME']: Moku(cfg['MOKU_A_IP']),  # Channels 1 to 4
        }
    except Exception as e:
        print(e)
        print('Failed to connect to Moku:Pro devices. Closing program')
        exit()

    # Create waveforms for each channel based on config parameters
    waves = [
        Waveform(ch, cfg['F_START'], cfg['F_STOP'], cfg['DELAYS'][ch-1], cfg['REL_RAMP_DURATION'], cfg['N_POINTS'], cfg['PHASES'][ch-1]) for ch in range(1, 9)
    ]

    # Upload waveforms and set Moku:Pro's in the good settings
    for wave in waves:
        devices[_findCorrespondingMoku(wave.channel)].setupChannel(
            wave.channel,
            wave.wave_array
        )

    showExampleWave(waves[0])

    # CLose connection with Moku:Pro's
    for name, device in devices.items():
        device.closeConnection()

    print('Finished setting up Moku:Pro devices')
