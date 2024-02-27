from Waveform import Waveform
from Moku import Moku
from config import settings as cfg
import atexit
import functions as fncs

# Pre-create devices dict for exit handler
devices = {}
atexit.register(fncs.exitHandler, devices)

def main() -> None:
    """Try to establisch connections with the Moku devices
    Create Waveform objects for each of the 8 channels
    Upload waveforms to Moku devices
    Show waveform of ch1, close connection to Moku devices and close program
    """

    try:
        devices = {
            cfg['MOKU_A_NAME']: Moku(cfg['MOKU_A_IP']),  # Channels 1 to 4
            cfg['MOKU_B_NAME']: Moku(cfg['MOKU_B_IP'])   # Channels 5 to 8
        }
    except Exception as e:
        print(e)
        print('Failed to connect to Moku:Pro devices. Closing program')
        exit()

    waves = [
        Waveform(ch, cfg['F_START'], cfg['F_STOP'], cfg['DELAYS'][ch-1], cfg['REL_RAMP_DURATION'], cfg['N_POINTS'], cfg['PHASES'][ch-1]) for ch in range(1, 9)
    ]

    for wave in waves:
        devices[fncs.findCorrespondingMoku(wave.channel)].setupChannel(
            fncs.selectMokuChannel(wave.channel),
            wave.wave_array
        )

    fncs.showExampleWave(waves[0])

    for name, device in devices.items():
        device.closeConnection()

    print('Finished setting up Moku:Pro devices')


if __name__ == "__main__":
    main()
