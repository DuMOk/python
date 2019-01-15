from socket import *
import sys
import json
import time
import logging
import log.client_log_config

def main(): 
  logger = logging.getLogger('client')
  
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
      "account_name": "DuMOk",
      "status": "online"
    }
  }
  
  client.send(json.dumps(msg).encode('utf-8'))
  data = client.recv(1000000)
  msg = json.loads(data.decode('utf-8'))
  
  if (msg.get('response') == 200):
    print('Сообщение от сервера: ', msg.get('alert'))
  elif (msg.get('response') == 400):
    print('Сообщение от сервера: ', msg.get('alert'))
  
  client.close()
  logger.info('Stop main client function!')

if __name__ == '__main__':
  main()


