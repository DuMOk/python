#слова в стоковом формате
word1 = 'разработка'
word2 = 'администрирование'
word3 = 'protocol'
word4 = 'standard'

#переводим слова из строкового в байтовый формате
word1_b = word1.encode('utf-16')
word2_b = word2.encode('utf-16')
word3_b = word3.encode('utf-16')
word4_b = word4.encode('utf-16')

#выводим результат
print(word1_b)
print(word2_b)
print(word3_b)
print(word4_b)

print('/////////////////////////////////////////////')

#переводим слова обратно из байтового в строковый формат
word1_s = word1_b.decode('utf-16')
word2_s = word2_b.decode('utf-16')
word3_s = word3_b.decode('utf-16')
word4_s = word4_b.decode('utf-16')

#выводим результат
print(word1_s)
print(word2_s)
print(word3_s)
print(word4_s)




