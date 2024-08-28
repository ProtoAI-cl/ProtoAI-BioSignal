import adafruit_ads1x15.ads1115 as ADS
import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn


def get_interface():
    try:
        # initialize the I2C interface
        i2c = busio.I2C(board.SCL, board.SDA)

        # creating ADS1115 object
        ads = ADS.ADS1115(i2c)

        # analog input channel
        channel = AnalogIn(ads, ADS.P0)

        return channel

    except Exception as e:
        raise e

    finally:
        pass

    # while True:
    #     print("AnalogValue: ", channel.value, "Voltage: ", channel.voltage)
    #     time.sleep(0.2)
