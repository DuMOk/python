from socket import *
import time
from datetime import datetime
import argparse
import json
import logging
import log.server_log_config

def main():
  logger = logging.getLogger('server')

  logger.debug('Start main server function!')
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', action='store', help='TCP-порт для работы (по умолчанию 7777)')
  parser.add_argument('-a', action='store', help='IP адрес для прослушивания(по умолчанию слушает все доступные адреса)')
  
  port = 7777
  address = ''
  
  if (parser.parse_args().p):
    port = int(parser.parse_args().p)
  if (parser.parse_args().a):
    address = parser.parse_args().a
  
  server = socket(AF_INET, SOCK_STREAM)  
  server.bind((address, port))                
  server.listen(10)                       
  
  
  msgOK = {
    "response": 200,
    "time": 0,
    "alert": ""
  }
  
  msgError = {
    "response": 400,
    "time": 0,
    "alert": "Error in JSON request"
  }
  
  while True:
    client, addr = server.accept()
    data = client.recv(1000000)
    msg = json.loads(data.decode('utf-8'))
    
    if (msg.get('action') == 'presence'):
      if (msg.get('user').get('status') == 'online'):
        user_time = datetime.utcfromtimestamp(msg.get('time')).strftime('%Y-%m-%d %H:%M:%S')
        msg_cl = f"User {msg.get('user').get('account_name')} is now {msg.get('user').get('status')}! Time: {user_time} "
        print(msg_cl)
        logger.info(msg_cl)
        msgOK['alert'] = f"Welcome to world, {msg.get('user').get('account_name')}!"
        msgOK['time'] = int(time.time())
        msg = msgOK
      else: 
        msgError['time'] = int(time.time())
        msg = msgError
    else: 
      msgError['time'] = int(time.time())
      msg = msgError
     
    client.send(json.dumps(msg).encode('utf-8'))
    client.close()

if __name__ == '__main__':
  main()



