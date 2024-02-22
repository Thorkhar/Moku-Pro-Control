# General settings
SAMPLE_RATE = '312.5Ms'  # Do not change
N_POINTS = 65536  # Do not change
MOKU_A_NAME = 'moku_morgul'
MOKU_B_NAME = 'moku_tirith'
MOKU_A_IP = '[fe80:0000:0000:0000:7269:79ff:feb0:0d26%18]'  # Moku Morgul IP
MOKU_B_IP = ''  # Moku Tirith IP

# Waveform settings
CHIRP_DURATION = 0.04  # Chirp duration in ms
F_START = 15000 * CHIRP_DURATION  # Multiply by chirp duration so Moku gets it right
F_STOP = 3000 * CHIRP_DURATION  # Multiply by chirp duration so Moku gets it right
REL_RAMP_DURATION = 0.01  # Relative durations of ramp up and down (1 = full wave duration, 0.01 = 1% of total duration)
PHASES = [
    ch * 45 for ch in range(0, 8)  # Phase per channel in degrees
]
DELAYS = [
    0, 0, 0, 0, 0, 0, 0, 0  # Delay per channel in microseconds (functionality not implemented yet)
]
