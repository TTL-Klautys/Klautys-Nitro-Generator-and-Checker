import requests
import random
import string
import time

print("""
▌│█║▌║▌║   142   ║▌║▌║█│▌
▌│█║▌║▌║ KLAUTYS ║▌║▌║█│▌
▌│█║▌║▌║   142   ║▌║▌║█│▌
""")
time.sleep(2)
print("Linkler Hazirlaniyor...")
time.sleep(0.3)
print("Herhangi bir sorun olursa ulasin --- Discord : kl4utys\n")
time.sleep(0.2)

num = int(input('Kac adet kod olusturulacak ve kontrol edilicek yazin: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Nitro kodlariniz hazirlandi , fazla kod istediyseniz sabirli olun!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Toplam {num} nitro kodu | Gecen sure: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Calisiyor(VALID) | {nitro} ")
            break
        else:
            print(f" Calismiyor(INVALID) | {nitro} ")

input("\nOlusturma islemi tamamlandi.Burayi kapatmak icin Enter tusuna basin.Calisan kodlari goruceksiniz.Eger hic bir sey yoksa sanssizsiniz."
      "Olumlu sonuc elde etmek icin 20 milyon ve daha uzeri kod olusturmaniz gerekir!")
