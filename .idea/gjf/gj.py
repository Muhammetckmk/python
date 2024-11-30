arabalar=['Bmw', 'Mercedes','Opel','Mazda']

result=len(arabalar)
result=arabalar[0]
result=arabalar[-1]
arabalar[-1]='Toyota'
result=arabalar
result='Mercedes' in arabalar  #listenin bir elemeanımıdır
result=arabalar[-2]
result=arabalar[0:3]#ilk üç indeksi aldık
arabalar[-2:]=['Toyota','Renault']#son iki değeri değiştirdik
result=arabalar
result=arabalar+['Audi','Nissan']
del arabalar[-1]
result=arabalar

result=arabalar[::-1]#elemanları tersten yazdırdık

studentA=['Yiğit','Bilgi',2010,[70,60,80]]
studentB =['Sena','Turan',1999,[80,80,70]]
studentC =['Ahmet','Turan',1998,[80,70,90]]

result =studentA[0]
result =studentB[1]
result =studentC[3][1]
result=f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"




print(result)
