import click
import serial.rs485

@click.command()
@click.option('--port', type=str, default='/dev/ttyAMA0')
@click.option('--baudrate', type=int, default=9600)
def run(port, baudrate):
  ser = serial.rs485.RS485(
      port=port,
      baudrate=baudrate,
      bytesize=serial.EIGHTBITS,
      parity=serial.PARITY_EVEN,
      stopbits=serial.STOPBITS_ONE,
      timeout=1.0,
      write_timeout=0.5,
  )
  ser.rs485_mode = serial.rs485.RS485Settings()

  while True:
      c = ser.read(1)
      ser.write(c)
      print(c, end='')

if __name__ == '__main__':
  run()
