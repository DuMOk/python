from socket import *
import sys
import json
import time, datetime
import logging, inspect
import log.client_log_config
from functools import wraps

logger = logging.getLogger('client')

def decorator(func):
  @wraps(func)
  def decorated(*args, **kwargs):
    logger.debug(f"Function name is {func.__name__} called with args {args} and named args {kwargs}")
    logger.debug(f"<{datetime.datetime.now()}> Function {func.__name__} call of function {inspect.stack()[1].function}")
    return func(*args, **kwargs)
  
  return decorated
  

@decorator
def recv_json(bytestr, encoding: str = "utf-8"):
  return json.loads(bytestr.decode(encoding))

def echo_client():
  with socket(AF_INET, SOCK_STREAM) as sock: 
    sock.connect(ADDRESS) 
    while True:
      msg = input('Ваше сообщение: ')
      if msg == 'exit':
        break
      sock.send(msg.encode('utf-8')) 
  
def main():   
  logger.info('Start main client function!')
  client = socket(AF_INET, SOCK_STREAM)
  
  if (len(sys.argv) == 1):
    logger.fatal('Не указан IP адрес для подключения к серверу!')
    sys.exit()
  elif (len(sys.argv) == 2):
    try: 
      client.connect((sys.argv[1], 7777))
    except ConnectionRefusedError:
      logger.error(f'Не удалось подключиться к серверу {sys.argv[1]} по TCP порту 7777')
      sys.exit()  
  elif (len(sys.argv) == 3):
    try:
      client.connect((sys.argv[1], int(sys.argv[2])))
    except ConnectionRefusedError:
      logger.error(f'Не удалось подключиться к серверу {sys.argv[1]} по TCP порту {sys.argv[2]}')
      sys.exit()
  else:
    print('Слишком много параметров!')
    sys.exit()
          
  timestamp = int(time.time())
  
  msg = {
    "action": "presence",
    "time": timestamp,
    "type": "status",
    "user": {
      "account_name": "SendingUser",
      "status": "online"
    }
  }

  usermsg = {
    "action": "msg",
    "time": timestamp,
    "to": "ListeningUser",
	"from": "SendingUser",
    "encoding": "utf-8",
	"message": "" 
  }
  
  client.send(json.dumps(msg).encode('utf-8'))
  data = client.recv(1000000)
  msg = recv_json(data, 'utf-8')
  
  if (msg.get('response') == 200):
    print('Сообщение от сервера: ', msg.get('alert'))
  elif (msg.get('response') == 400):
    print('Сообщение от сервера: ', msg.get('alert'))

  while True:
    msg = input('Ваше сообщение: ')
    if msg == 'exit':
      client.close()
      logger.info('Stop main client function!')
      break
    usermsg['message'] = msg
    client.send(json.dumps(usermsg).encode('utf-8')) 

if __name__ == '__main__':
  main()


