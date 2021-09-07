import phonenumbers
from phonenumbers import carrier,geocoder,timezone
import time


 ------------------- Detaylı Telefon Bilgisi Programı -------------------


def getregionandcountry():     # Telefon Numarasının Bulunduğu Coğrafi Bölge

    while True:

        try:

            mobile_no = "+"  + input("Lütfen Ülke Kodu ile Birlikte Telefon Numaranızı Giriniz:")
            mobile_no = phonenumbers.parse(mobile_no)

            return timezone.time_zones_for_number(mobile_no)

        except:

            time.sleep(1)
            print("Lütfen Doğru Telefon Kodunu Giriniz !")
            continue

        break


def get_carrier_name():   # Telefon Numarasının Operetörü

    while True:

        try:

            mobile_no = "+" + input("Lütfen Ülke Kodu ile Birlikte Telefon Numaranızı Giriniz:")
            mobile_no = phonenumbers.parse(mobile_no)

            return "Telefon Numarasının Bağlı Olduğu Operatör: " + carrier.name_for_number(mobile_no,"en")

        except:

            time.sleep(1)
            print("Lütfen Doğru Telefon Kodunu Giriniz !")
            continue

        break


def getcountry():           # Telefon Numarasının Ait Olduğu Ülke

    while True:

        try:

            mobile_no = "+" + input("Lütfen Ülke Kodu ile Birlikte Telefon Numaranızı Giriniz:")
            mobile_no = phonenumbers.parse(mobile_no)

            return "Telefon Numarasının Aktif Olduğu Ülke: " + geocoder.description_for_number(mobile_no,"en")

        except:

            time.sleep(1)
            print("Lütfen Doğru Telefon Kodunu Giriniz !")
            continue

        break



def isphonenumbervalid():    # Telefon Numarasının Geçerliliği

    while True:

        try:

            mobile_no = "+" + input("Lütfen Ülke Kodu ile Birlikte Telefon Numaranızı Giriniz:")
            mobile_no = phonenumbers.parse(mobile_no)

            valid_process = phonenumbers.is_valid_number(mobile_no)

            if valid_process == True:

                return "Telefon numarası geçerlidir."

            else:
                return "Telefon numarası geçerli değildir."

        except:

            time.sleep(1)
            print("Lütfen Doğru Telefon Kodunu Giriniz !")
            continue

        break



def application_process():   # Uygulamayı Çalıştırma

    while True:


        process = input("""Lütfen Gerçekleştirmek İstediğiniz İşlemi Seçiniz:
        
        - Telefon Numarasının Ait Olduğu Bölgeyi Öğrenmek İçin: 1
         
        -- Telefon Numarasının Operatörünü Öğrenmek İçin: 2"
        
        --- Telefon Kodunun Ait Olduğu Ülkeyi Öğrenmek İçin: 3
        
        ---- Telefon Numarasının Geçerliliğini Öğrenmek İçin: 4""")

        if process == "1":

            print(getregionandcountry())

        elif process == "2":

            print(get_carrier_name())

        elif process == "3":

            print(getcountry())

        elif process =="4":

            print(isphonenumbervalid())

        else:

            print ("Lütfen Geçerli İşlem Birimini Seçiniz !")
            continue

        process_again = input("Yeniden İşlem Gerçekleştirmek İster Misiniz ?")


        if process_again == "E" or process_again == "e" or process_again =="Evet" or process_again == "EVET":

            continue
        else:

            print("Program Kapanıyor...")
            time.sleep(1)
            print("Program Kapanıyor...")
            break



application_process()