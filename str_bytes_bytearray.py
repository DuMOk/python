def bytestr_to_unicodestr(bstr):
  return bstr.decode('cp1251')

def unicodestr_to_bytestr(ustr):
  return ustr.encode('koi8-r')
  
def unicodestr_to_bytearray(ustr):
  return bytearray(ustr, 'utf-8')
  
# В Python 3 все строки - строки юникода
s = 'Python'
# Отдельный тип - строка байтов
bs = b'Python'

# Отдельный тип - bytearray - изменяемая строка байтов
ba = bytearray(bs)

# Преобразования между строками
s2 = bytestr_to_unicodestr(bs)       # Из байт-строки в юникод строку
bs2 = unicodestr_to_bytestr(s)        # Из юникод-строки в строку байтов
ba2 = unicodestr_to_bytearray(s)    # Из юникод-строки в массив байтов
