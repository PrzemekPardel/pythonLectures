#creation
a = 'krowa'
b = "koń"
print(a)
print(b)
#new line and other special chars
a = 'kro\nwa'
b = "ko\nń"
print(a)
print(b)
#concatenation
c = 'a' + 'b'
print(c)
d = 'ooo' 'aaa'
print(d)
#string duplication
print(3 * 'abc')
print(3 * 'abc''sss')
#chars indexations
slowo = 'starW'
print(slowo[0])
#print(slowo[20])
print(slowo[-1])
#sybstring
print(slowo[0:3])
print(slowo[-3:4])
#chars replacement
#slowo[0] = 'F'
print(slowo)
slowo = slowo[:2] + 'X' + slowo[2+1:]
print(slowo)
#string length
print(len(slowo))
#capitalize
print(slowo.capitalize());
#string completion
print(slowo.center(15, 'O'))
#counting occurencies
slowo = 2 * slowo
print(slowo.count('tX'))
print(slowo.count('tX',5))
print(slowo.count('tX',0,4))
#search occurencies
print(slowo.find('tX'))
print(slowo.find('tX',5))
print(slowo.find('tX',0,4))
print(slowo.find('tX',7,9))
#search occurencies
print('tX' in slowo)
print('aX' in slowo)
#alpphanumeric
print(slowo.isalnum())
slowo = 's1a!'
print(slowo.isalnum())
#alpha
print(slowo.isalpha())
slowo = 'abc'
print(slowo.isalpha())
#digit
print(slowo.isdigit())
slowo = '0011'
print(slowo.isdigit())
#small letter
print(slowo.islower())
slowo = 'asd'
print(slowo.islower())
#big letter
print(slowo.isupper())
slowo = 'AASS'
print(slowo.isupper())
#replace to small
slowo = 'AAss11'
print(slowo.lower())
#replace to big
print(slowo.upper())
#reverse size
print(slowo.swapcase())
#Title
slowo = 'jak nie tak to mak'
print(slowo.title())
#split string
print(slowo.split())
print(slowo.split(' '))
print(slowo.split('k'))
print(slowo.split('k', 2))
print(slowo.split(maxsplit = 2))
#split lines
slowo = 'jak nie \n tak to \n mak'
print(slowo.splitlines())
#strip string
slowo = '    jjjjjak nie nak to najjjjj    '
print(slowo.strip())
slowo = 'jjjjjak nie nak to najjjjj'
print(slowo.strip('j'))