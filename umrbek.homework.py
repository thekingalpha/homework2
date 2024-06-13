joriy_yil = 2024
tugilgan_yil = joriy_yil - yosh
return tugilgan_yil
ism = input("Ismingizni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))
print(f"{ism}, siz {tugilgan_yilni_hisobla(ism, yosh)}-yilda tug'ilgansiz.")
def kattasi_chiqar(son1, son2):
    if son1 > son2:
        print(f"Katta son: {son1}")
    elif son1 < son2:
        print(f"Katta son: {son2}")
    else:
        print("Sonlar teng")
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
kattasi_chiqar(son1, son2)
def kattasi_chiqar(son1, son2, y=10):
    if son1 > son2:
        if son1 > y:
            print(f"Birinchi son ({son1}) katta {y} dan")
        else:
            print(f"Katta son: {son1}")
    elif son1 < son2:
        if son2 > y:
            print(f"Ikkinchi son ({son2}) katta {y} dan")
        else:
            print(f"Katta son: {son2}")
    else:
        print("Sonlar teng")
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
kattasi_chiqar(son1, son2)
def qoldiqsiz_bolinishni_tekshir(son):
    if 2 <= son <= 10:
        for i in range(2, 11):
            if son % i == 0:
                print(f"{son} {i} ga qoldiqsiz bo'linadi")
            else:
                print(f"{son} {i} ga qoldiqsiz bo'linmaydi")
    else:
        print(f"{son} 2 dan 10 gacha bo'lmagan son")
son = int(input("Sonni kiriting: "))
qoldiqsiz_bolinishni_tekshir(son)
