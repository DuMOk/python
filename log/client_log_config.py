# Для проекта «Мессенджер» реализовать логирование с использованием модуля logging:
# В директории проекта создать каталог log, в котором для клиентской и серверной сторон в отдельных модулях 
# формата client_log_config.py и server_log_config.py создать логгеры;
# В каждом модуле выполнить настройку соответствующего логгера по следующему алгоритму:
# - Создание именованного логгера;
# - Сообщения лога должны иметь следующий формат: "<дата-время> <уровень_важности> <имя_модуля> <сообщение>";
# - Журналирование должно производиться в лог-файл;
# - На стороне сервера необходимо настроить ежедневную ротацию лог-файлов.    
# - Реализовать применение созданных логгеров для решения двух задач:
# - Журналирование обработки исключений try/except. Вместо функции print() использовать журналирование 
#   и обеспечить вывод служебных сообщений в лог-файл;
# - Журналирование функций, исполняемых на серверной и клиентской сторонах при работе мессенджера


import logging
import sys      

logger = logging.getLogger('client')

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

fh = logging.FileHandler("log/client.log", encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)





