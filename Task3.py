#слова в стоковом формате
word1 = 'attribute'
word2 = 'класс'
word3 = 'функция'
word4 = 'type'

#проверка на возможность записать слово в байтовом типе (ASCII)
print('Check word "attribute": {0}'.format(all(ord(char) < 128 for char in word1)))
print('Check word "класс": {0}'.format(all(ord(char) < 128 for char in word2)))
print('Check word "функция": {0}'.format(all(ord(char) < 128 for char in word3)))
print('Check word "type": {0}'.format(all(ord(char) < 128 for char in word4)))