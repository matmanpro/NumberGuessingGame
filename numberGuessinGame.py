import random
alt = int(input('Alt siniri giriniz: '))
ust = int(input('Ust siniri giriniz: '))
sayi = random.randint(alt, ust)
print(sayi)
a = 1
while True:
    tahmin = int(input('Lutfen giridigiz aralikta sayi giriniz: '))
    if (tahmin < sayi):
        print('Girdiginiz sayi istenen sayidan kucuktur...')
    elif (tahmin > sayi):
        print('Girdiginiz sayi istenen sayidan buyuktur... ')
    elif ( tahmin == sayi):
        print('Tebrikler iyi tahmin ettiniz...')
        break
    a += 1
print('Sonucu: ',a, 'kerede bildiniz')    
