#tworzenie
a = 'krowa'
b = "koń"
print(a)
print(b)
#nowa linia i znaki specjalne
a = 'kro\nwa'
b = "ko\nń"
print(a)
print(b)
#sklejanie łańcuchów
c = 'a' + 'b'
print(c)
d = 'ooo' 'aaa'
print(d)
#powielanie łańcuchów
print(3 * 'abc')
print(3 * 'abc''sss')
#indeksowanie znaków
slowo = 'starW'
print(slowo[0])
#print(slowo[20])
print(slowo[-1])
#wycinannie łańcuchów
print(slowo[0:3])
print(slowo[-3:4])
#zamiana znaku
#slowo[0] = 'F'
print(slowo)
slowo = slowo[:2] + 'X' + slowo[2+1:]
print(slowo)
#dlugość łańcucha
print(len(slowo))
#kapitaliki
print(slowo.capitalize());
#uzupełnianie łańcucha
print(slowo.center(15, 'O'))
#zliczanie wystąpień
slowo = 2 * slowo
print(slowo.count('tX'))
print(slowo.count('tX',5))
print(slowo.count('tX',0,4))
#wyszukiwanie wystąpień
print(slowo.find('tX'))
print(slowo.find('tX',5))
print(slowo.find('tX',0,4))
print(slowo.find('tX',7,9))
#wyszukanie wystapienia
print('tX' in slowo)
print('aX' in slowo)
#alfanumeruczne
print(slowo.isalnum())
slowo = 's1a!'
print(slowo.isalnum())
#litery alfabetu
print(slowo.isalpha())
slowo = 'abc'
print(slowo.isalpha())
#liczby
print(slowo.isdigit())
slowo = '0011'
print(slowo.isdigit())
#małe litery
print(slowo.islower())
slowo = 'asd'
print(slowo.islower())
#duże litery
print(slowo.isupper())
slowo = 'AASS'
print(slowo.isupper())
#zamiana na małe litery
slowo = 'AAss11'
print(slowo.lower())
#zamiana duże litery
print(slowo.upper())
#zamiana wielkości liter
print(slowo.swapcase())
#Title
slowo = 'jak nie tak to mak'
print(slowo.title())
#Rozdzielanie łańcucha znaków
print(slowo.split())
print(slowo.split(' '))
print(slowo.split('k'))
print(slowo.split('k', 2))
print(slowo.split(maxsplit = 2))
#rozdzielanie linii
slowo = 'jak nie \n tak to \n mak'
print(slowo.splitlines())
#wycinanie znaków początku i końca
slowo = '    jjjjjak nie nak to najjjjj    '
print(slowo.strip())
slowo = 'jjjjjak nie nak to najjjjj'
print(slowo.strip('j'))