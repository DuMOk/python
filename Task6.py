#подключаем модуль codecs для открытия файлов с возможностью обработки ошибок
import codecs

#создаем файл
fh = open("test_file.txt", "w", encoding = "cp866")

#записываем три строки
fh.write("сетевое программирование\nсокет\nдекоратор\n")

#закрываем файл
fh.close()

#выводим кодировку файла
print('Encoding of the file: {0}'.format(fh.encoding))

print('//////////////////////////////////////')

#открываем файл в кодировке Unicode
with codecs.open("test_file.txt", "r", encoding = "utf-8", errors = "replace") as file:
  for line in file:
    print(line)

