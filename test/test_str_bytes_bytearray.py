import str_bytes_bytearray
import unittest

# Модульные тесты
class TestMyFunction(unittest.TestCase):
  def test_bytestr_to_unicodestr(self):
    r = str_bytes_bytearray.bytestr_to_unicodestr(b'GeekBrains')
    self.assertEqual(r, 'GeekBrains')

  def test_unicodestr_to_bytestr(self):
    r = str_bytes_bytearray.unicodestr_to_bytestr('GeekBrains')
    self.assertEqual(r, b'GeekBrains')

  def test_unicodestr_to_bytearray(self):
    r = str_bytes_bytearray.unicodestr_to_bytearray('GeekBrains')
    self.assertNotEqual(r, 'GeekBrains')
	
# Запустить тестирование
if __name__ == '__main__':
    unittest.main()