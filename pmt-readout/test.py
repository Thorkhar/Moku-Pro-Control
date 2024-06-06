from config import settings as cfg
from Moku import Moku

def main():
    moku_tirith = Moku(cfg["MOKU_B_IP"])
    moku_tirith.closeConnection()

main()