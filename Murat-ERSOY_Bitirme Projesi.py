import RPi.GPIO as pin                      # Raspberry pi üzerindeki Pinlerin I/O olarak kullanmak için gerekli kütüphane dahil edildi
import datetime                             # Gün,saat... gibi tarih kullanmak için dahil edildi
import time                                 # saat, dakika,saniye kullanmak için dahil edildi
import smtplib                              # SMTP modülü dahil edildi, sunucular arasında e-posta gönderip alırken kullanılan bir TCP/IP protokolüdür(SMTP= Simple Mail Transfer Protocol)
from time import sleep                      # delay verip saniye cinsinden sayac(timer) oluşturmak için dahil edilen modül
from datetime import timedelta              # saat dakika gibi değerlerle aritmetik işlemler için dahil edilen fonksiyon
from email.message import EmailMessage      # e-mail göndermek için dahil edilen EmailMessage modülü

ileti1 = EmailMessage()                          # "ileti1" adlı string değişken EmailMessage modülü içine atandı
ileti1["Subject"] = "Acil Durum!"                # Mailin konusu
ileti1["From"] = "okuldeneme21@gmail.com"        # Maili gönderen
ileti1["To"] = "okuldeneme20@gmail.com"          # Mail alıcısı
ileti1.set_content("2 saattir hareket yok")      # Mail içeriği

ileti2 = EmailMessage()                          # "ileti2" adlı string değişken EmailMessage modülü içine atandı
ileti2["Subject"] = "Acil Durum!"                # Mailin konusu
ileti2["From"] = "okuldeneme21@gmail.com"        # Maili gönderen
ileti2["To"] = "okuldeneme20@gmail.com"          # Mail alıcısı
ileti2.set_content("4 saattir hareket yok")      # Mail içeriği

ileti3 = EmailMessage()                          # "ileti3" adlı string değişken EmailMessage modülü içine atandı
ileti3["Subject"] = "Yeni Durum Değişikliği!"    # Mailin konusu
ileti3["From"] = "okuldeneme21@gmail.com"        # Maili gönderen
ileti3["To"] = "okuldeneme20@gmail.com"          # Mail alıcısı
ileti3.set_content("Yeniden hareket algılandı")  # Mail içeriği

ileti4 = EmailMessage()                                          # "ileti4" adlı string değişken EmailMessage modülü içine atandı
ileti4["Subject"] = "Acil Durum!"                                # Mailin konusu
ileti4["From"] = "okuldeneme21@gmail.com"                        # Maili gönderen
ileti4["To"] = "okuldeneme20@gmail.com"                          # Mail alıcısı
ileti4.set_content("+2 saat daha geçti ve hâlen hareket yok")    # Mail içeriği

ileti5 = EmailMessage()                                          # "ileti5" adlı string değişken EmailMessage modülü içine atandı
ileti5["Subject"] = "Acil Durum!"                                # Mailin konusu
ileti5["From"] = "okuldeneme21@gmail.com"                        # Maili gönderen
ileti5["To"] = "okuldeneme20@gmail.com"                          # Mail alıcısı
ileti5.set_content("+4 saat daha geçti ve hâlen hareket yok")    # Mail içeriği

 # ileti6, ileti7, ileti8 ve ileti9 Test modu içindir #

ileti6 = EmailMessage()                          # "ileti6" adlı string değişken EmailMessage modülü içine atandı
ileti6["Subject"] = "Acil Durum!"                # Mailin konusu
ileti6["From"] = "okuldeneme21@gmail.com"        # Maili gönderen
ileti6["To"] = "okuldeneme20@gmail.com"          # Mail alıcısı
ileti6.set_content("2 dakikadır hareket yok")    # Mail içeriği

ileti7 = EmailMessage()                          # "ileti7" adlı string değişken EmailMessage modülü içine atandı
ileti7["Subject"] = "Acil Durum!"                # Mailin konusu
ileti7["From"] = "okuldeneme21@gmail.com"        # Maili gönderen
ileti7["To"] = "okuldeneme20@gmail.com"          # Mail alıcısı
ileti7.set_content("4 dakikadır hareket yok")    # Mail içeriği

ileti8 = EmailMessage()                                           # "ileti8" adlı string değişken EmailMessage modülü içine atandı
ileti8["Subject"] = "Acil Durum!"                                 # Mailin konusu
ileti8["From"] = "okuldeneme21@gmail.com"                         # Maili gönderen
ileti8["To"] = "okuldeneme20@gmail.com"                           # Mail alıcısı
ileti8.set_content("+2 dakika daha geçti ve hâlen hareket yok")   # Mail içeriği

ileti9 = EmailMessage()                                           # "ileti9" adlı string değişken EmailMessage modülü içine atandı
ileti9["Subject"] = "Acil Durum!"                                 # Mailin konusu
ileti9["From"] = "okuldeneme21@gmail.com"                         # Maili gönderen
ileti9["To"] = "okuldeneme20@gmail.com"                           # Mail alıcısı
ileti9.set_content("+4 dakika daha geçti ve hâlen hareket yok")   # Mail içeriği

pin.setmode(pin.BOARD)       # Raspberry Pi üzerindeki fiziksel numaralandırma seçildi
pin.setwarnings(False)       # Kullanılmayan pinlerin açıkta kalmış uyarısı vermemesi için

pin.setup(11, pin.IN)        # 11.pini giriş pini olarak seçtik,Sensörden gelen lojik sinyallerin bağlandığı pin



sayac1 = 0  # ilk 12 saatlik dilimde kullanılacak sayac başlangıç değeri 0 olarak atandı +1 saniye şeklinde artacak 2 saat için değeri 7200 saniye (7200 saniye = 2 saat)
sayac2 = 0  # son 12 saatlik dilimde kullanılacak sayac başlangıç değeri 0 olarak atandı +1 saniye şeklinde artacak 4 saat için değeri 14400 saniye (14400 saniye = 4 saat)
sayac3 = 0  # ilk 12 saatlik dilimde durum güncellemesi için kullanılan sayaç başlangıç değeri 0 olarak atandı mail gönderildikten sonra değeri +1 artacak
sayac4 = 0  # son 12 saatlik dilimde durum güncellemesi için kullanılan sayaç başlangıç değeri 0 olarak atandı mail gönderildikten sonra değeri +1 artacak

 # sayac6, sayac7, sayac8 ve sayac9 Test Modu içindir

sayac6 = 0  # ilk 30 dk lık kısımda kullanılacak sayac başlangıç değeri 0 olarak atandı +1 saniye şeklinde artacak 2 dakika için değeri 120 saniye (120 saniye= 2 dakika)
sayac7 = 0  # son 30 dk lık kısımda kullanılacak sayac başlangıç değeri 0 olarak atandı +1 saniye şeklinde artacak 4 dakika için değeri 240 saniye (240 saniye= 4 dakika)
sayac8 = 0  # ilk 30 dk lık kısımda durum güncellemesi için kullanılan sayaç başlangıç değeri 0 olarak atandı mail gönderildikten sonra değeri +1 artacak
sayac9 = 0  # son 30 dk lık kısımda durum güncellemesi için kullanılan sayaç başlangıç değeri 0 olarak atandı mail gönderildikten sonra değeri +1 artacak

print(" Lütfen Mod seçiniz ; ")  # Mod seçilmesi için uyarı

mod = int(input(" \n Normal_Mod'u seçmek için= 1 değerini giriniz, Test_modu'nu seçmek için= 2 değerini giriniz : "))    # Bir satır boşluk bırakarak klavyeden girilen değere göre Test modu veya Normal mod başlangıç seçimi


if mod == 1:    # Mod=1 ise Normal Modda Çalışır

    print(" \n girilen değer : ",mod)        # Bir satır boşluk bırakarak klaveyeden girilen değeri göster
    print(" mod=1, Normal Mod seçildi ")     # Hangi modda çalıştığına dair bilgilendirme
                                             # mod 1 ve Normal modda çalışıyor

    while True:  # Döngü doğru olduğu sürece çalışır

        zaman_farki = datetime.timedelta(hours=24)     # Zaman farkı 1 günü kapsaycak şekilde 24 saat olarak ayarlandı
        suan = datetime.datetime.now()                 # anlık zaman
        t = (suan - zaman_farki).hour                  # Zaman döngüsünün değişkeni 0=<t<24 saat cinsinden olacak şekilde
        sensorden_gelen_sinyal = pin.input(11)         # 11.pin hareket sensöründen gelen lojik sinyal "sensorden_gelen_sinyal" değişkene atandı

        if 12 >= t:                                 # gündüz döngüsü t=<12 saat için olan bölüm

            if sensorden_gelen_sinyal == 0:  # sensörden gelen sinyal 0 mı kontrol et eğer 0 ise
                sayac1 = sayac1 + 1  # sayac1'i +1 arttır 1 saniye bekle alta geç
                sleep(1)  # alttaki koşul geçerli değil ise döngüyü tekrar et
                pass

                if sayac1 == 7200:          # sayac1=7200 oldumu yani 7200 saniye(2 saat) geçti ve hiç hareket yoksa aşağıdaki satıları çalıştır

                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:   # smtp protokolü ile 465.portu kullanarak gmail serverlarına bağlan
                        smtp.login("okuldeneme21@gmail.com","hk2675510")   # tanımlanan mail adresi ve şifre ile gmail hesabına giriş yap
                        smtp.send_message(ileti1)                          # "ileti1" adlı mesajı mail olarak gönder
                        sayac3 = sayac3 + 1                                # acil durum maili gönderilirse sayac3'ün değerini +1 arttır

                if sayac1 >= 14400 and sayac1 % 7200 == 0:   # acil durum maili atıldıktan sonra yine üstüne +2 saat geçti ve yine hiç hareket yoksa(yani toplamda 4 saat geçti(14400 saniye))
                                                             # sayac1'nin 14400'den büyük veya eşit olması yani ilk acil durum mailinden sonra en az +2 saat daha geçmesi gerekli
                                                             # ayrıca sayac1 7200'ün tam katı olması lazım ki başka bir zamanda mail atmasın yani aynı süre geçtikten sonra ve ilk koşul gerçekleştikten sonra
                                                             # bu durum iki koşula bağlı olarak çalışır ve her iki koşulda geçerli ise bu kod satırı aktif olur
                                                             # hem ilk acil durum maili atılmış olmalı hemde tekrar aynı süre geçmiş ve hiç bir hareket algılanmamış olması lazım

                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:   # smtp protokolü ile 465.portu kullanarak gmail serverlarına bağlan
                        smtp.login("okuldeneme21@gmail.com","hk2675510")   # tanımlanan mail adresi ve şifre ile gmail hesabına giriş yap
                        smtp.send_message(ileti4)                          # "ileti4" adlı mesajı mail olarak gönder

            else:
                sensorden_gelen_sinyal == 1                               # sensörden gelen sinyal 1 ise sayac1'i sıfırla ve döngüyü tekrar kontrol et
                sayac1 = 0                                                # sayac1'i sıfırla ve döngüyü tekrar kontrol et

                if sensorden_gelen_sinyal == 1 and sayac3 > 0:        # acil durum mailinden sonra yeniden hareket algılanırsa durum güncellemesi için

                    sayac3 = 0                                        # sayac3'ü sıfırla
                    sayac1 = 0                                        # sayac1'i sıfırla
                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:  # smtp protokolü ile 465.portu kullanarak gmail serverlarına bağlan
                        smtp.login("okuldeneme21@gmail.com","hk2675510")  # tanımlanan mail adresi ve şifre ile gmail hesabına giriş yap
                        smtp.send_message(ileti3)                         # "ileti3" adlı mesajı mail olarak gönder
                    continue                                              # döngüye devam et




        elif 12 < t:                            # gece döngüsü 24>t>12 saat arası için olan bölüm

            if sensorden_gelen_sinyal == 0:     # sensörden gelen sinyal 0 mı kontrol et eğer 0 ise
                sayac2 = sayac2 + 1             # sayac2'yi +1 arttır 1 saniye bekle alta geç
                sleep(1)                        # alttaki koşul geçerli değil ise döngüyü tekrar et
                pass

                if sayac2 == 14400:             # sayac2=14400 oldumu yani 14400 saniye(4 saat) geçti ve hiç hareket yoksa aşağıdaki satıları çalıştır

                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:   # smtp protokolü ile 465.portu kullanarak gmail serverlarına bağlan
                        smtp.login("okuldeneme21@gmail.com","hk2675510")   # tanımlanan mail adresi ve şifre ile gmail hesabına giriş yap
                        smtp.send_message(ileti2)                          # "ileti2" adlı mesajı mail olarak gönder
                    sayac4 = sayac4 + 1                                    # acil durum maili gönderilirse sayac4'ün değerini +1 arttır

                if sayac2 >= 28800 and sayac2 % 14400 == 0:   # acil durum maili atıldıktan sonra yine üstüne +4 saat geçti ve yine hiç hareket yoksa(yani toplamda 8 saat geçti(28800 saniye))
                                                              # sayac2'nin 28800'den büyük veya eşit olması yani ilk acil durum mailinden sonra en az +4 saat daha geçmesi gerekli
                                                              # ayrıca sayac2 14400'ün tam katı olması lazım ki başka bir zamanda mail atmasın yani aynı süre geçtikten sonra ve ilk koşul gerçekleştikten sonra
                                                              # bu durum iki koşula bağlı olarak çalışır ve her iki koşulda geçerli ise bu kod satırı aktif olur
                                                              # hem ilk acil durum maili atılmış olmalı hemde tekrar aynı süre geçmiş ve hiç bir hareket algılanmamış olması lazım

                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:  # smtp protokolü ile 465.portu kullanarak gmail serverlarına bağlan
                        smtp.login("okuldeneme21@gmail.com","hk2675510")  # tanımlanan mail adresi ve şifre ile gmail hesabına giriş yap
                        smtp.send_message(ileti5)                         # "ileti5" adlı mesajı mail olarak gönder

            else:
                sensorden_gelen_sinyal == 1      # sensörden gelen sinyal 1 ise
                sayac2 = 0                       # sayac2'i sıfırla ve döngüyü tekrar kontrol et

                if sensorden_gelen_sinyal == 1 and sayac4 > 0:   # acil durum mailinden sonra yeniden hareket algılanırsa durum güncellemesi için
                    sayac4 = 0                                   # sayac4'i sıfırla
                    sayac2 = 0                                   # sayac2'i sıfırla
                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:   # smtp protokolü ile 465.portu kullanarak gmail serverlarına bağlan
                        smtp.login("okuldeneme21@gmail.com","hk2675510")   # tanımlanan mail adresi ve şifre ile gmail hesabına giriş yap
                        smtp.send_message(ileti3)                          # "ileti3" adlı mesajı mail olarak gönder
                    continue                                               # döngüye devam et


                                                   # Test Modu #


elif mod == 2:   # Eğer mod=2 ise Test Modunda Çalışır

    print(" \n girilen değer : ",mod)                   # Bir satır boşluk bırakarak klavyeden girilen değeri göster
    print(" mod=2, Test Modu seçildi ")                 # Hangi modda çalıştığına dair bilgilendirme
                                                        # mod 2 ve Test Modunda  çalışıyor

    while True:    # Döngü doğru olduğu sürece çalışır

        zaman_farki = datetime.timedelta(minutes=60)    # zaman farkı 1 saat kapsaycak şekilde 60 dakika olarak ayarlandı
        suan = datetime.datetime.now()                  # anlık zaman
        t = (suan - zaman_farki).minute                 # zaman döngüsünün değişkeni 0<t<60 dakika cinsinden olacak şekilde
        sensorden_gelen_sinyal = pin.input(11)          # 11.pin hareket sensöründen gelen lojik sinyal "sensorden_gelen_sinyal" değişkene atandı

        if 30 >= t:                               # gündüz döngüsü t=<30 için olan bölüm

            if sensorden_gelen_sinyal == 0:       # sensörden gelen sinyal 0 mı kontrol et eğer 0 ise
                sayac6 = sayac6 + 1               # sayac6'yı +1 arttır 1 saniye bekle alta geç
                sleep(1)                          # alttaki koşul geçerli değil ise döngüyü tekrar et
                pass

                if sayac6 == 120:  # sayac6=120 oldu mu yani 120 saniye geçti ve hiç hareket yoksa aşağıdaki satıları çalıştır

                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:   # smtp protokolü ile 465.portu kullanarak gmail serverlarına bağlan
                        smtp.login("okuldeneme21@gmail.com","hk2675510")   # tanımlanan mail adresi ve şifre ile gmail hesabına giriş yap
                        smtp.send_message(ileti6)                          # "ileti6" adlı mesajı mail olarak gönder
                        sayac8 = sayac8 + 1                                # acil durum maili gönderilirse sayac8'in değerini +1 arttır

                if sayac6 >= 240 and sayac6 % 120 == 0:   # acil durum maili atıldıktan sonra yine üstüne +2 dakika geçti ve yine hiç hareket yoksa(yani toplamda 4 dakika geçti(240 saniye)
                                                          # sayac6'nın 240'dan büyük veya eşit olması yani ilk acil durum mailinden sonra en az +2 dakika daha geçmesi gerekli
                                                          # ayrıca sayac6 120'nin tam katı olması lazım ki başka bir zamanda mail atmasın yani aynı süre geçtikten sonra ve ilk koşul gerçekleştikten sonra
                                                          # bu durum iki koşula bağlı olarak çalışır ve her iki koşulda geçerli ise bu kod satırı aktif olur
                                                          # hem ilk acil durum maili atılmış olmalı hemde tekrar aynı süre geçmiş ve hiç bir hareket algılanmamış olması lazım
                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:  # smtp protokolü ile 465.portu kullanarak gmail serverlarına bağlan
                        smtp.login("okuldeneme21@gmail.com","hk2675510")  # tanımlanan mail adresi ve şifre ile gmail hesabına giriş yap
                        smtp.send_message(ileti8)                         # "ileti8" adlı mesajı mail olarak gönder


            else:
                sensorden_gelen_sinyal == 1                         # sensörden gelen sinyal 1 ise
                sayac6 = 0                                          # sayac6'yı sıfırla ve döngüyü tekrar kontrol et

                if sensorden_gelen_sinyal == 1 and sayac8 > 0:      # acil durum mailinden sonra yeniden hareket algılanırsa durum güncellemesi için
                    sayac8 = 0                                      # sayac8'i sıfırla
                    sayac6 = 0                                      # sayac6'yı sıfırla
                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:   # smtp protokolü ile 465.portu kullanarak gmail serverlarına bağlan
                        smtp.login("okuldeneme21@gmail.com","hk2675510")   # tanımlanan mail adresi ve şifre ile gmail hesabına giriş yap
                        smtp.send_message(ileti3)                          # "ileti3" adlı mesajı mail olarak gönder
                    continue                                               # döngüye devam et




        elif 30 < t:                             # gece döngüsü 60>t=>30 için olan bölüm

            if sensorden_gelen_sinyal == 0:      # sensörden gelen sinyal 0 mı kontrol et eğer 0 ise
                sayac7 = sayac7 + 1              # sayac7'yi +1 arttır 1 saniye bekle alta geç
                sleep(1)                         # alttaki koşul geçerli değil ise döngüyü tekrar et
                pass

                if sayac7 == 240:                # sayac7=240 oldumu yani 240 saniye geçti ve hiç hareket yoksa aşağıdaki satıları çalıştır

                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:   # smtp protokolü ile 465.portu kullanarak gmail serverlarına bağlan
                        smtp.login("okuldeneme21@gmail.com","hk2675510")   # tanımlanan mail adresi ve şifre ile gmail hesabına giriş yap
                        smtp.send_message(ileti7)                          # "ileti7" adlı mesajı mail olarak gönder
                    sayac9 = sayac9 + 1                                    # acil durum maili gönderilirse sayac9'un değerini +1 arttır

                if sayac7 >= 480 and sayac7 % 240 == 0:    # acil durum maili atıldıktan sonra yine üstüne +4 dakika geçti ve yine hiç hareket yoksa(yani toplamda 8 dakika geçti(480 saniye)
                                                           # sayac7'nin 480'den büyük veya eşit olması yani ilk acil durum mailinden sonra en az +4 dakika daha geçmesi gerekli
                                                           # ayrıca sayac7 240'ın tam katı olması lazım ki başka bir zamanda mail atmasın yani aynı süre geçtikten sonra ve ilk koşul gerçekleştikten sonra
                                                           # bu durum iki koşula bağlı olarak çalışır ve her iki koşulda geçerli ise bu kod satırı aktif olur
                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:   # smtp protokolü ile 465.portu kullanarak gmail serverlarına bağlan
                        smtp.login("okuldeneme21@gmail.com","hk2675510")   # tanımlanan mail adresi ve şifre ile gmail hesabına giriş yap
                        smtp.send_message(ileti9)                          # "ileti9" adlı mesajı mail olarak gönder

            else:
                sensorden_gelen_sinyal == 1                         # sensörden gelen sinyal 1 ise
                sayac7 = 0                                          # sayac7'yi sıfırla ve döngüyü tekrar kontrol et

                if sensorden_gelen_sinyal == 1 and sayac9 > 0:      # acil durum mailinden sonra yeniden hareket algılanırsa durum güncellemesi için
                    sayac9 = 0                                      # sayac9'u sıfırla
                    sayac7 = 0                                      # sayac7'yi sıfırla
                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:   # smtp protokolü ile 465.portu kullanarak gmail serverlarına bağlan
                        smtp.login("okuldeneme21@gmail.com","hk2675510")   # tanımlanan mail adresi ve şifre ile gmail hesabına giriş yap
                        smtp.send_message(ileti3)                          # "ileti3" adlı mesajı mail olarak gönder
                    continue                                               # döngüye devam et

