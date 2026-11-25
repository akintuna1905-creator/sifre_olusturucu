import random
harfler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk=int(input("Parolaniz kac haneli olsun"))
sifre=""
for i in range(uzunluk):
    sifre += random.choice(harfler)
print("Oluşturulan şifreniz:",sifre)
