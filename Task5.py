#для возможности вызвать команду ping
import subprocess
#для определиния кодировки
import chardet

youtube_check = ['ping', '-n', '4', 'youtube.com']
yandex_check = ['ping', '-n', '4', 'yandex.ru']

#ping YouTube
print('Let\'s ping yotube.com')
sp_pinger = subprocess.Popen(youtube_check, stdout=subprocess.PIPE)

for line in sp_pinger.stdout:
  result_code = chardet.detect(line)
  line = line.decode(result_code['encoding']).encode('utf-8')
  print(line.decode('utf-8'))

	
#ping Yandex
print('Let\'s ping yandex.ru')
sp_pinger = subprocess.Popen(yandex_check, stdout=subprocess.PIPE)

for line in sp_pinger.stdout:
  result_code = chardet.detect(line)
  line = line.decode(result_code['encoding']).encode('utf-8')
  print(line.decode('utf-8'))




