from socket import *
import time
from datetime import datetime
import argparse
import json
import logging
import log.server_log_config
import select

logger = logging.getLogger('server')

def new_listen_socket(addr, tcpport):
  server_sock = socket(AF_INET, SOCK_STREAM)  
  server_sock.bind((addr, tcpport))                
  server_sock.listen(10)                       
  server_sock.settimeout(0.2)
  
  return server_sock

def read_requests(r_clients, all_clients):
  responses = {} 
  
  for sock in r_clients:
    try:
      data = json.loads(sock.recv(1000000).decode('utf-8'))
      responses[sock] = data
    except:
      print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
      all_clients.remove(sock)
      
  return responses

def write_responses(requests, w_clients, all_clients):
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
     
  for k in requests:
    msg = requests[k]
    
    if (msg.get('action') == 'presence'):
      if (msg.get('user').get('status') == 'online'):
        user_time = datetime.utcfromtimestamp(msg.get('time')).strftime('%Y-%m-%d %H:%M:%S')
        msg_cl = f"User {msg.get('user').get('account_name')} is now {msg.get('user').get('status')}! Time: {user_time} "
        logger.info(msg_cl)
        msgOK['alert'] = f"Welcome to world, {msg.get('user').get('account_name')}!"
        msgOK['time'] = int(time.time())
        message = msgOK
      else: 
        msgError['time'] = int(time.time())
        message = msgError
    elif (msg.get('action') == 'msg'): 
      message = msg  
    else: 
      msgError['time'] = int(time.time())
      message = msgError
  
    for sock in w_clients:
      if ((sock == k)):
        try:
          resp = json.dumps(message).encode('utf-8')
          sock.send(resp)
        except:
          print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
          sock.close()
          all_clients.remove(sock) 	 
      elif (msg.get('action') == 'msg'):
        try:
          resp = json.dumps(message).encode('utf-8')
          sock.send(resp)
        except:
          print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
          sock.close()
          all_clients.remove(sock)  	 

def main():
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
  
  server = new_listen_socket(address, port)
 
  clients = []
  while True:
    try:
      client, addr = server.accept()
    except OSError as e:
      pass
    else:
      print("Получен запрос на соединение с %s" % str(addr))
      clients.append(client)
    finally:
      wait = 10
      write_client = []
      read_client = []
      try:
        read_client, write_client, e = select.select(clients, clients, [], wait)
      except Exception as e:
        pass        
                
      client_requests = read_requests(read_client, clients)
      if client_requests:
        write_responses(client_requests, write_client, clients)

if __name__ == '__main__':
  main()



