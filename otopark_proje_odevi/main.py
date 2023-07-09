#sabit değerler
bir_ton_fiyat=2.5
motorsiklet_katsayısı=1
binek_katsayısı=2
minibüs_katsayısı=3
otobüs_katsayısı=3
kamyon_katsayısı=4
tır_katsayısı=4
#toplanılacak değerler
motorsiklet_sayısı=0
motorsiklet_geliri=0
motorsiklet_suresi=0
otuz_dakikadan_az_motorsiklet=0

binek_sayısı=0
binek_geliri=0
binek_suresi=0
otuz_dakikadan_az_binek=0
bir_tondan_az_binek=0
max_gelir_binek=-1

minibus_sayısı=0
minibus_geliri=0
minibus_suresi=0
bir_günden_fazla_minibus=0

otobüs_sayısı=0
otobüs_geliri=0
otobüs_suresi=0
bir_günden_fazla_otobüs=0
on_tondan_fazla_otobüs=0

kamyon_sayısı=0
kamyon_geliri=0
kamyon_suresi=0
on_tondan_fazla_kamyon=0

tır_sayısı=0
tır_geliri=0
tır_suresi=0
on_tondan_fazla_tır=0

otoparktaki_tum_araclar=0
otopark_toplam_gelir=0
otuz_gun_bin_tl=0
ozel_durum_motorsiklet_sayısı=0
ozel_durum_motorsiklet_dakika=0
ozel_durum_binek_sayısı=0
ozel_durum_binek_dakika=0
ozel_durum_toplam_arac=0
ozel_durum_toplam_dakika=0
uc_saatten_fazla_ozel_durum_motorsiklet=0
uc_saatten_fazla_ozel_durum_binek=0
uc_saatten_fazla_ozel_durum_toplam=0

max_dakika_kalan_arac=-1


gazi_indirim_oranı=100
engelli_indirim_oranı=50
yok_indirim_oranı=0

baska_arac_var_mı='e'
while baska_arac_var_mı=='e' or baska_arac_var_mı=='E':

    arac_plakası=input("aracın plakası giriniz:")
    arac_sinif_kodu=int(input("araç sınıf kodu:"))
    arac_agirlik=float(input("aracın ağırlığı:"))
    dakika=int(input("Otoparkta kadığı süre (dk):"))
    ad_soyad=input("sürücünün adı-soyadı:")

    giris_ucreti=(arac_agirlik/1000)*bir_ton_fiyat


    if arac_sinif_kodu==1:
        ozel_durum=input("sürücünün özel durumu (Yok/Gazi/Engelli (Y/y/G/g/E/e)):")
        arac_sınıf_adı='motorsiklet'

        if dakika<60:
            otopark_ucreti=giris_ucreti+(3*motorsiklet_katsayısı)
        elif dakika<180:
            otopark_ucreti = giris_ucreti + (5 * motorsiklet_katsayısı)
        elif dakika<300:
            otopark_ucreti = giris_ucreti + (7 * motorsiklet_katsayısı)
        elif dakika<600:
            otopark_ucreti = giris_ucreti + (10 * motorsiklet_katsayısı)
        elif dakika<1440:
            otopark_ucreti = giris_ucreti + (14 * motorsiklet_katsayısı)
        if dakika>=1440:
            if dakika % 1440 == 0: #
                otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * motorsiklet_katsayısı)
            else: #24' ün modundan kalan dakikayı ekleme
                if dakika % 1440< 60:
                    otopark_ucreti = giris_ucreti + (15* (dakika//1440)* motorsiklet_katsayısı) + (3 * motorsiklet_katsayısı)
                elif dakika % 1440< 180:
                    otopark_ucreti = giris_ucreti + (15* (dakika//1440)* motorsiklet_katsayısı) + (5 * motorsiklet_katsayısı)
                elif dakika % 1440 < 300:
                    otopark_ucreti = giris_ucreti + (15* (dakika//1440)* motorsiklet_katsayısı)+ (7 * motorsiklet_katsayısı)
                elif dakika % 1440 < 600:
                    otopark_ucreti = giris_ucreti + (15* (dakika//1440)* motorsiklet_katsayısı)+ (10 * motorsiklet_katsayısı)
                elif dakika % 1440 < 1440:
                    otopark_ucreti = giris_ucreti + (15* (dakika//1440)* motorsiklet_katsayısı) + (14 * motorsiklet_katsayısı)

        if dakika < 30:
            otuz_dakikadan_az_motorsiklet += 1

        if ozel_durum=='gazi' or ozel_durum=='G' or ozel_durum=='g':
            otopark_ucreti=0
            indirim_oranı=gazi_indirim_oranı
        elif ozel_durum=='engelli' or ozel_durum=='E' or ozel_durum=='e':
            otopark_ucreti=otopark_ucreti/2
            indirim_oranı=engelli_indirim_oranı
        else:
            indirim_oranı=yok_indirim_oranı

        if dakika>180:
            uc_saatten_fazla_ozel_durum_motorsiklet+=1

        if ozel_durum=='gazi' or ozel_durum=='G' or ozel_durum=='g' or  ozel_durum=='engelli' or ozel_durum=='E' or ozel_durum=='e':
            ozel_durum_motorsiklet_sayısı+=1
            ozel_durum_toplam_dakika+=dakika

        motorsiklet_sayısı+=1
        motorsiklet_geliri+=otopark_ucreti
        motorsiklet_suresi+=dakika



    if arac_sinif_kodu==2:
        ozel_durum = input("sürücünün özel durumu:")
        arac_sınıf_adı = 'binek'

        if dakika < 60:
            otopark_ucreti = giris_ucreti + (3 * binek_katsayısı)
        elif dakika < 180:
            otopark_ucreti = giris_ucreti + (5 * binek_katsayısı)
        elif dakika < 300:
            otopark_ucreti = giris_ucreti + (7 * binek_katsayısı)
        elif dakika < 600:
            otopark_ucreti = giris_ucreti + (10 * binek_katsayısı)
        elif dakika < 1440:
            otopark_ucreti = giris_ucreti + (14 * binek_katsayısı)

        if dakika>=1440:
            if dakika%1440==0:
                otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * binek_katsayısı)

            else:

                if dakika % 1440 < 60:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * binek_katsayısı) + (3 * binek_katsayısı)
                elif dakika % 1440 < 180:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * binek_katsayısı) + (5 * binek_katsayısı)
                elif dakika % 1440 < 300:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * binek_katsayısı) + (7 * binek_katsayısı)
                elif dakika % 1440 < 600:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * binek_katsayısı) + (10 * binek_katsayısı)
                elif dakika % 1440 < 1440:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * binek_katsayısı) + (14 * binek_katsayısı)

        if dakika < 30:
            otuz_dakikadan_az_binek += 1

        if ozel_durum == 'gazi' or ozel_durum == 'G' or ozel_durum == 'g':
            indirim_oranı=gazi_indirim_oranı
            otopark_ucreti = 0
        elif ozel_durum == 'engelli' or ozel_durum == 'E' or ozel_durum == 'e':
            indirim_oranı=engelli_indirim_oranı
            otopark_ucreti = otopark_ucreti / 2
        else:
            indirim_oranı=yok_indirim_oranı
        if dakika>180:
            uc_saatten_fazla_ozel_durum_binek+=1

        if ozel_durum=='gazi' or ozel_durum=='G' or ozel_durum=='g' or  ozel_durum=='engelli' or ozel_durum=='E' or ozel_durum=='e':
            ozel_durum_binek_sayısı+=1
            ozel_durum_binek_dakika+=dakika

        binek_sayısı+=1
        binek_geliri+=otopark_ucreti
        binek_suresi+=dakika

        if arac_agirlik<1000:
            bir_tondan_az_binek+=1

        if otopark_ucreti>max_gelir_binek:
            max_gelir_binek=otopark_ucreti
            max_gelir_binek_dakika=dakika

    ozel_durum_toplam_arac=ozel_durum_motorsiklet_sayısı+ozel_durum_binek_sayısı
    ozel_durum_toplam_dakika=ozel_durum_motorsiklet_dakika+ozel_durum_binek_dakika
    uc_saatten_fazla_ozel_durum_toplam=uc_saatten_fazla_ozel_durum_motorsiklet+uc_saatten_fazla_ozel_durum_binek


    if arac_sinif_kodu == 3:
        arac_sınıf_adı = 'minibüs'

        if dakika < 60:
            otopark_ucreti = giris_ucreti + (3 * minibüs_katsayısı)
        elif dakika < 180:
            otopark_ucreti = giris_ucreti + (5 * minibüs_katsayısı)
        elif dakika < 300:
            otopark_ucreti = giris_ucreti + (7 * minibüs_katsayısı)
        elif dakika < 600:
            otopark_ucreti = giris_ucreti + (10 * minibüs_katsayısı)
        elif dakika < 1440:
            otopark_ucreti = giris_ucreti + (14 * minibüs_katsayısı)

        if dakika>=1440:
            if dakika % 1440 == 0:
                otopark_ucreti = (giris_ucreti + (15 * (dakika // 1440) * minibüs_katsayısı))
            else:
                if dakika % 1440< 60:
                    otopark_ucreti =(giris_ucreti + (15 * (dakika // 1440) * minibüs_katsayısı)) + (3 * minibüs_katsayısı)
                elif dakika % 1440 < 180:
                    otopark_ucreti = (giris_ucreti + (15 * (dakika // 1440) * minibüs_katsayısı)) + (5 * minibüs_katsayısı)
                elif dakika % 1440 < 300:
                    otopark_ucreti = (giris_ucreti + (15 * (dakika // 1440) * minibüs_katsayısı)) + (7 * minibüs_katsayısı)
                elif dakika % 1440 < 600:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * minibüs_katsayısı) + (10 * minibüs_katsayısı)
                elif dakika % 1440 < 1440:
                    otopark_ucreti = (giris_ucreti + (15 * (dakika // 1440) * minibüs_katsayısı)) + (14 * minibüs_katsayısı)

            bir_günden_fazla_minibus += 1

        minibus_sayısı+=1
        minibus_geliri+=otopark_ucreti
        minibus_suresi+=dakika

    if arac_sinif_kodu == 4:
        arac_sınıf_adı = 'otobüs'
        if dakika < 60:
            otopark_ucreti = giris_ucreti + (3 * otobüs_katsayısı)
        elif dakika < 180:
            otopark_ucreti = giris_ucreti + (5 * otobüs_katsayısı)
        elif dakika < 300:
            otopark_ucreti = giris_ucreti + (7 * otobüs_katsayısı)
        elif dakika < 600:
            otopark_ucreti = giris_ucreti + (10 * otobüs_katsayısı)
        elif dakika < 1440:
            otopark_ucreti = giris_ucreti + (14 * otobüs_katsayısı)

        if dakika >= 1440:
            if dakika % 1440 ==0:
                otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * otobüs_katsayısı)

            else:
                if dakika % 1440< 60:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * otobüs_katsayısı) + (3 * otobüs_katsayısı)
                elif dakika % 1440 < 180:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * otobüs_katsayısı) + (5 * otobüs_katsayısı)
                elif dakika % 1440 < 300:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * otobüs_katsayısı) + (7 * otobüs_katsayısı)
                elif dakika % 1440< 600:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * otobüs_katsayısı) + (10 * otobüs_katsayısı)
                elif dakika % 1440 < 1440:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * otobüs_katsayısı) + (14 * otobüs_katsayısı)


            bir_günden_fazla_otobüs += 1

        otobüs_sayısı+=1
        otobüs_geliri+=otopark_ucreti
        otobüs_suresi+=dakika

        if arac_agirlik>10000: #ağırlığı 10 tondan fazla otobüs
            on_tondan_fazla_otobüs+=1

    if arac_sinif_kodu == 5:
        arac_sınıf_adı = 'kamyon'
        if dakika < 60:
            otopark_ucreti = giris_ucreti + (3 * kamyon_katsayısı)
        elif dakika < 180:
            otopark_ucreti = giris_ucreti + (5 * kamyon_katsayısı)
        elif dakika < 300:
            otopark_ucreti = giris_ucreti + (7 * kamyon_katsayısı)
        elif dakika < 600:
            otopark_ucreti = giris_ucreti + (10 * kamyon_katsayısı)
        elif dakika < 1440:
            otopark_ucreti = giris_ucreti + (14 * kamyon_katsayısı)
        if dakika >= 1440:
            if dakika % 1440 == 0:
                otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * kamyon_katsayısı)
            else:
                if dakika % 1440 < 60:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * kamyon_katsayısı) + (3 * kamyon_katsayısı)
                elif dakika % 1440 < 180:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * kamyon_katsayısı) + (5 * kamyon_katsayısı)
                elif dakika % 1440 < 300:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * kamyon_katsayısı) + (7 * kamyon_katsayısı)
                elif dakika % 1440 < 600:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * kamyon_katsayısı) + (10 * kamyon_katsayısı)
                elif dakika % 1440 < 1440:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * kamyon_katsayısı) + (14 * kamyon_katsayısı)

        kamyon_sayısı+=1
        kamyon_geliri+=otopark_ucreti
        kamyon_suresi+=dakika
        if arac_agirlik>10000:  #ağırlığı 10 tondan fazla kamyon
            on_tondan_fazla_kamyon+=1

    if arac_sinif_kodu == 6:
        arac_sınıf_adı = 'tır'
        if dakika < 60:
            otopark_ucreti = giris_ucreti + (3 * tır_katsayısı)
        elif dakika < 180:
            otopark_ucreti = giris_ucreti + (5 * tır_katsayısı)
        elif dakika < 300:
            otopark_ucreti = giris_ucreti + (7 * tır_katsayısı)
        elif dakika < 600:
            otopark_ucreti = giris_ucreti + (10 * tır_katsayısı)
        elif dakika < 1440:
            otopark_ucreti = giris_ucreti + (14 * tır_katsayısı)
        if dakika>=1440:
            if dakika % 1440 == 0:
                otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * tır_katsayısı)
            else:
                if dakika % 1440 < 60:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * tır_katsayısı) + (3 * tır_katsayısı)
                elif dakika % 1440 < 180:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * tır_katsayısı) + (5 * tır_katsayısı)
                elif dakika % 1440 < 300:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * tır_katsayısı) + (7 * tır_katsayısı)
                elif dakika % 1440 < 600:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * tır_katsayısı) + (10 * tır_katsayısı)
                elif dakika % 1440 < 1440:
                    otopark_ucreti = giris_ucreti + (15 * (dakika // 1440) * tır_katsayısı) + (14 * tır_katsayısı)

        tır_sayısı+=1
        tır_geliri+=otopark_ucreti
        tır_suresi+=dakika
        if arac_agirlik>10000:  #ağırlığı 10 tondan fazla kamyon
            on_tondan_fazla_tır+=1

    otoparktaki_tum_araclar = motorsiklet_sayısı+binek_sayısı+minibus_sayısı+otobüs_sayısı+kamyon_sayısı+tır_sayısı
    otopark_toplam_gelir =motorsiklet_geliri+binek_geliri+minibus_geliri+otobüs_geliri+kamyon_geliri+tır_geliri
    if dakika>43200 or otopark_ucreti>1000:
        otuz_gun_bin_tl+=1

    if dakika>max_dakika_kalan_arac:
        max_dakika_kalan_arac=dakika
        max_dakika_kalan_arac_geliri=otopark_ucreti

    print(f"araç plakası: {arac_plakası}" )
    print(f"araç sınıf adı: {arac_sınıf_adı}")
    print(f"araç ağırlığı: {arac_agirlik} kg")
    print(f"otoparkta kaldığı gün: {dakika//1440} saat: {(dakika%1440)//60} dakika: {dakika%60}")
    print(f"sürücünün adı soyadı:{ad_soyad}")
    if arac_sinif_kodu==1 or arac_sinif_kodu==2:
        print(f"sürücünün özel durumu:{ozel_durum}")
        print(f"uygulanan indirim oranı: {indirim_oranı}")
    print(f"otopark ücreti:{otopark_ucreti:.2f} TL")


    baska_arac_var_mı=input("otoparkta başka araç var mı(e/E/h/H):")


print(f"otoparkı kullanan toplam araç sayısı:{otoparktaki_tum_araclar} ")
print(f"motorsiklet sayısı:{motorsiklet_sayısı} motorsiklet oranı: %{motorsiklet_sayısı/otoparktaki_tum_araclar*100:.2f}")
print(f"binek sayısı:{binek_sayısı} binek oranı: %{binek_sayısı/otoparktaki_tum_araclar*100:.2f}")
print(f"minibüs sayısı:{minibus_sayısı} minibüs oranı: %{minibus_sayısı/otoparktaki_tum_araclar*100:.2f}")
print(f"otobüs sayısı:{otobüs_sayısı} otobüs oranı: %{otobüs_sayısı/otoparktaki_tum_araclar*100:.2f}")
print(f"kamyon sayısı:{kamyon_sayısı} kamyon oranı: %{kamyon_sayısı/otoparktaki_tum_araclar*100:.2f}")
print(f"tır sayısı:{tır_sayısı} tır oranı: %{tır_sayısı/otoparktaki_tum_araclar*100:.2f}")

print(f"otoparkın toplam geliri: {otopark_toplam_gelir:.2f} TL")
print(f"motorsiklet toplam geliri: {motorsiklet_geliri:.2f} Tl , motorsiklet gelir oran: %{motorsiklet_geliri/otopark_toplam_gelir*100:.2f}  ")
print(f"binek toplam geliri: {binek_geliri:.2f} TL , binek gelir oran: %{binek_geliri/otopark_toplam_gelir*100:.2f}")
print(f"minibüs toplam geliri: {minibus_geliri:.2f} TL , minibüs gelir oran: %{minibus_geliri/otopark_toplam_gelir*100:.2f}")
print(f"otobüs toplam geliri: {otobüs_geliri:.2f} TL , otobüs gelir oran: %{otobüs_geliri/otopark_toplam_gelir*100:.2f}")
print(f"kamyon toplam geliri: {kamyon_geliri:.2f} TL , kamyon gelir oran: %{kamyon_geliri/otopark_toplam_gelir*100:.2f}")
print(f"tır toplam geliri: {tır_geliri:.2f} TL,  tır gelir oran: %{tır_geliri/otopark_toplam_gelir*100:.2f}")

print(f"motorsiklet araç başına ortalama gün: {(motorsiklet_suresi/motorsiklet_sayısı)//1440} saat: {((motorsiklet_suresi/motorsiklet_sayısı)%1440)//60} dakika: {(motorsiklet_suresi/motorsiklet_sayısı)%60} motorsiklet araç başına ortalama gelir: {motorsiklet_geliri/motorsiklet_sayısı:.2f}")
print(f"binek araç başına ortalama gün: {(binek_suresi/binek_sayısı)//1440} saat: {((binek_suresi/binek_sayısı)%1440)//60} dakika: {(binek_suresi/binek_sayısı)%60}  binek araç başına ortalama gelir: {binek_geliri/binek_sayısı:.2f}")
print(f"minibüs araç başına ortalama gün: {(minibus_suresi/minibus_sayısı)//1440} saat: {((minibus_suresi/minibus_sayısı)%1440)//60} dakika: {(minibus_suresi/minibus_sayısı)%60} minibüs araç başına ortalama gelir: {minibus_geliri/minibus_sayısı:.2f}")
print(f"otobüs araç başına ortalama gün: {(otobüs_suresi/otobüs_sayısı)//1440} saat: {((otobüs_suresi/otobüs_sayısı)%1440)//60} dakika: {(otobüs_suresi/otobüs_sayısı)%60} otobüs araç başına ortalama gelir: {otobüs_geliri/otobüs_sayısı:.2f}")
print(f"kamyon araç başına ortalama gün: {(kamyon_suresi/kamyon_sayısı)//1440} saat: {((kamyon_suresi/kamyon_sayısı)%1440)//60} dakika: {(kamyon_suresi/kamyon_sayısı)%60}  kamyon araç başına ortalama gelir: {kamyon_geliri/kamyon_sayısı:.2f}")
print(f"tır araç başına ortalama gün: {(tır_suresi/tır_sayısı)//1440} saat: {((tır_suresi/tır_sayısı)%1440)//60} dakika: {(tır_suresi/tır_sayısı)%60}  tır araç başına ortalama gelir: {tır_geliri/tır_sayısı:.2f}")

print(f"ağırlığı 1 tondan az olan binek araçların, tüm binek araçlar içindeki oranı: %{bir_tondan_az_binek/binek_sayısı*100:.2f}")
print(f"ağırlığı 10 tondan fazla olan otobüs, kamyon ve tır sınıfı araçların, tüm otobüs, kamyon ve tır sınıfı araçlar içindeki oranı: % {((on_tondan_fazla_otobüs+on_tondan_fazla_kamyon+on_tondan_fazla_tır)/(otobüs_sayısı+kamyon_sayısı+tır_sayısı))*100:.2f}")
print(f"otoparkta 30 dakika veya daha kısa süre kalan motosiklet ve binek tipi araçların, tüm motosiklet ve binek tipi araçlar içindeki oranı: %{((otuz_dakikadan_az_motorsiklet+otuz_dakikadan_az_binek)/(motorsiklet_sayısı+binek_sayısı))*100:.2f}")
print(f"otoparkta 1 günden daha uzun süre kalan minibüs ve otobüs tipi araçların, tüm minibüs ve otobüs tipi araçlar içindeki oranı: % {((bir_günden_fazla_otobüs+bir_günden_fazla_minibus)/(minibus_sayısı+otobüs_sayısı))*100:.2f}")
print(f"otoparkta 30 günden daha uzun süre kalan veya 1000 TL’den daha yüksek gelir edilen araçların, tüm araçlar içindeki oranı:{(otuz_gun_bin_tl/otoparktaki_tum_araclar)*100:.2f}")
print(f"sürücüsü gazi veya engelli olan araçların sayıları, tüm araçlar içindeki oranları: % {(ozel_durum_toplam_arac/otoparktaki_tum_araclar)*100:.2f}  araç başına ortalama otoparkta kalma süreleri gün: {(ozel_durum_toplam_dakika/ozel_durum_toplam_arac)//1440}  saat:{((ozel_durum_toplam_dakika/ozel_durum_toplam_arac)%1440)//60}  dakika: {(ozel_durum_toplam_dakika/ozel_durum_toplam_arac)%60}")
print(f"otoparkta 3 saatten daha uzun süre kalan indirim uygulanan araçların, tüm indirim uygulanan araçlar içindeki oranı: % {(uc_saatten_fazla_ozel_durum_toplam/ozel_durum_toplam_arac)*100:.2f}")
print(f"en uzun süre otoparkta kalan aracın otoparkta kaldığı  gün: {max_dakika_kalan_arac//1440} saat: {((max_dakika_kalan_arac)%1440)//60} dakika: {(max_dakika_kalan_arac)%60}  elde edilen gelir: {max_dakika_kalan_arac_geliri:.2f}")
print(f"en çok gelir elde edilen binek aracın otoparkta kaldığı gün: {(max_gelir_binek_dakika)//1440} saat: {(max_gelir_binek_dakika%1440)//60} dakika: {max_gelir_binek_dakika%60}  elde edilen gelir:{max_gelir_binek:.2f}")
