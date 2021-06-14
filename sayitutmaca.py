import random 
sayi = random.randint(1, 10)
tahmin = input("Sayıyı tahmin ediniz : ")

while int(tahmin) != sayi :
    tahmin = input("Sayıyı tahmin ediniz : ")
    if (int(tahmin) == sayi):
     print("Tahmininiz doğru!")
    else:
     print("Yanlış tahmin ettiniz, bir daha tahmin ediniz.")
    
