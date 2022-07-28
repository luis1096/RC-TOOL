import os
import sys
import time
import serial



from config import BAUDRATE, DRIVER

class Printer:
    def __init__(self):
        self.start_connection()

    def __del__(self):
        """
        Closes connection on object deletion 
        """
        self.connection.close()

    def start_connection(self):
        try:
            self.connection = serial.Serial(
                port=DRIVER,
                baudrate=BAUDRATE
            )

            time.sleep(1)
            
            # removes initial status codes
            while self.connection.inWaiting() > 0:
                self.connection.read(1).decode()

        except Exception as e:
            return False

    # mm pertains to the amount extruder moves in milimeters, while the rate pertains to 
    # the rate of extrusion at mm/min. 1500mm/min seems like a good default.
    def send_extrusion(self, mm: float, rate: float) -> str:
        cmd = f'G1 E{mm} F{rate}'

        # send the character to the device
        self.connection.write(cmd.encode())

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while self.connection.inWaiting() > 0:
            message += self.connection.read(1).decode()

        return message

    # Acts as a "continue on" hint for the printer if it is looping or waiting on some condition
    def break_and_continue(self) -> str:
        cmd = f'M108'

        # send the character to the device
        self.connection.write(cmd.encode())

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while self.connection.inWaiting() > 0:
            message += self.connection.read(1).decode()

        return message

    # homes the extruder motor if needed
    def home_extruder(self) -> str:
        cmd = f'G92 E0\n'
        message = ''

        # send the character to the device
        self.connection.write(cmd.encode())

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while self.connection.inWaiting() > 0:
            message += self.connection.read(1).decode()

        return message

    # Option for enabling/disabling hotend temperature checking or setting a minimum extrusion temperature
    def cold_extrude(self, enableFlag: bool, minTemp: float) -> str:
        cmd = ''
        if enableFlag == True:
            cmd = f'M302 P0\n'
        elif(minTemp > 0):
            cmd = f'M302 S{minTemp}\n'
        else:
            cmd = f'M302 P1\n'
        message = ''

        # send the character to the device
        self.connection.write(cmd.encode())

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while self.connection.inWaiting() > 0:
            message += self.connection.read(1).decode()

        return message

    # Getting current hotend temperature checking configuration
    def cold_extrude_status(self) -> str:
        cmd = f'M302'
        message = ''

        # send the character to the device
        self.connection.write(cmd.encode())

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while self.connection.inWaiting() > 0:
            message += self.connection.read(1).decode()

        return message

    def send_temperature(self, celsius: float) -> str:
        cmd = f'M104 S{celsius}'
        message = ''

        # send the character to the device
        self.connection.write(cmd.encode())

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while self.connection.inWaiting() > 0:
            message += self.connection.read(1).decode()

        return message

    # This will prevent the printer from moving on untill the desired temperature is reached
    def send_temperature_and_wait(self, celsius: float) -> str:
        cmd = f'M109 S{celsius}'
        message = ''

        # send the character to the device
        self.connection.write(cmd.encode())

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while self.connection.inWaiting() > 0:
            message += self.connection.read(1).decode()

        return message

    def check_temperature(self) -> int:
        cmd = f'M105\n'
        message = ''

        # send the character to the device
        self.connection.write(cmd.encode())

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while self.connection.inWaiting() > 0:
            message += self.connection.read(1).decode()

        return message

    # This will set it so the printer returns its temperature on the provided time interval in seconds
    def auto_check_temperature(self, interval: int) -> str:
        cmd = f'M155 S{interval}\n'
        message = ''

        # send the character to the device
        self.connection.write(cmd.encode())

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while self.connection.inWaiting() > 0:
            message += self.connection.read(1).decode()

        return message
    
    def set_fan(self, speed: int) -> str:
        cmd = f'M106 S{speed}' if speed > 0 else f'M107'

        # send the character to the device
        self.connection.write(cmd.encode())

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while self.connection.inWaiting() > 0:
            message += self.connection.read(1).decode()

        return message

    # Let the return for this method be agnostic
    def send_general_gcode(self, cmd: str):
        cmd.strip()
        message = ''

        # send the character to the device
        self.connection.write(cmd.encode())

        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while self.connection.inWaiting() > 0:
            message += self.connection.read(1).decode()

        return message