from socket import *
from select import select
import sys
import json 

def recv_json(bytestr, encoding: str = "utf-8"):
  return json.loads(bytestr.decode(encoding))
 
def echo_client():
  ADDRESS = ('localhost', 7777)
  
  if (len(sys.argv) == 1):
    sys.exit()
  elif (len(sys.argv) == 2):
    try: 
      ADDRESS = (sys.argv[1], 7777)
    except ConnectionRefusedError:
      sys.exit()  
  elif (len(sys.argv) == 3):
    try:
      ADDRESS = (sys.argv[1], int(sys.argv[2]))
    except ConnectionRefusedError:
      sys.exit()
  else:
    print('Слишком много параметров!')
    sys.exit()
  
  with socket(AF_INET, SOCK_STREAM) as sock:  
    sock.connect(ADDRESS) 
    while True:	  
      data = sock.recv(1000000)
      msg = recv_json(data, 'utf-8')
      if data:
        print(f"Сообщение от пользовтаеля {msg.get('from')}: {msg.get('message')}")
 
if __name__ == '__main__':
  echo_client()