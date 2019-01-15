import data_server
import unittest
from socket import *

# Модульные тесты
class TestMyFunction(unittest.TestCase):
  def test_receive_msg(self):
    s = socket(AF_INET, SOCK_STREAM)
    r = data_server.receive_msg(s)
    self.assertIsInstance(r, str)

# Запустить тестирование
if __name__ == '__main__':
    unittest.main()