ogrenciler={}

number=input("öğrenci no: ")
name=input("öğrenci adı: ")
surname=input("öğrenci soyadı: ")
phone=input("öğrenci tel: ")
#
#ogrenciler[number]={
#    'ad':name,
#    'soyad':surname,
#    'telefon':phone
#}                       #list e bu bilgileri ekledik




ogrenciler.update({
    number:{
    'ad':name,
    'soyad':surname,
    'telefon': phone
    }
})          #bu şekilde de ekleyebiliriz. farkı ise
            # böyle yapınca birden çok ekleme yapabilriiz
            #son süslü parantezden önce virgül koyup
print(ogrenciler)