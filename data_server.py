# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import time

def receive_msg(data):
  msg = data.recv(1000000)
  return msg.decode('utf-8')

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind(('', 8007))                # Присваивает порт 8888
s.listen(5)                       # Переходит в режим ожидания запросов;
                                  # Одновременно обслуживает не более
                                  # 5 запросов.
while True:
    client, addr = s.accept()
    print(client)
    client_msg = receive_msg(client)
    print('Сообщение: ', client_msg, ', было отправлено клиентом: ', addr)
    msg = 'Привет, клиент'
    client.send(msg.encode('utf-8'))
    client.close()