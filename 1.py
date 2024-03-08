import serial
import time
import serial.tools.list_ports



speeds = ['1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200'] # Список скоростей передачи (бит)

ports = [p.device for p in serial.tools.list_ports.comports()] # Создание списка имен подключенных устройств вида "/dev/ttyUSB0"

port_name = ports[0] # Имя первого устройства
port_speed = int(speeds[-1]) # Скорость "115200" передачи
port_timeout = 10 # значениеv времени ожидания чтения в секундах.

ard = serial.Serial(port_name, port_speed, timeout = port_timeout) # Создание объекта с заданым именем, скоростью, временем

time.sleep(1) # Задержка
ard.flushInput() # Очистки входного буфера перед чтением новых данных.
try:
  msg_bin = ard.read(ard.inWaiting()) #

  # .inWaiting() - Получить количество байтов во входном буфере
  # .read - количество байт для чтения.

  msg_bin += ard.read(ard.inWaiting())
  msg_bin += ard.read(ard.inWaiting())
  msg_bin += ard.read(ard.inWaiting())
  msg_str_ = msg_bin.decode() # Преобразование в строку
  print(len(msg_bin)) # длина
except Exception as e:
  print('Error!')

ard.close() # Закрыть подключение порта
time.sleep(1)
print(msg_str_) # вывести строку полученную выше
