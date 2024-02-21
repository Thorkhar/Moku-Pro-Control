# General settings
SAMPLE_RATE = '312.5Ms'
MOKU_A_NAME = 'moku_morgul'
MOKU_B_NAME = 'moku_tirith'
MOKU_A_IP = ''  # Moku Morgul IP
MOKU_B_IP = ''  # Moku Tirith IP

# Waveform settings
CHIRP_DURATION = 0.04  # Chirp duration in ms
N_POINTS = 65536
F_START = 15000 * CHIRP_DURATION  # Multiply by chirp duration so Moku gets it right
F_STOP = 3000 * CHIRP_DURATION  # Multiply by chirp duration so Moku gets it right
REL_RAMP_DURATION = 0.05  # Relative durations of ramp up and down
PHASES = [
    ch * 45 for ch in range(0, 7)  # Phase per channel in degrees
]
DELAYS = [
    0, 0, 0, 0, 0, 0, 0, 0  # Delay per channel in microseconds
]
