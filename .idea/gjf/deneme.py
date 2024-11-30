number=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']



val=min(number)#1
val=max(number)#16
val=max(letters)#y
val=min(letters)#a

number[4]=40
number.append(49)#listenin sonuna ekledi
number.insert(3,78)#belirttiğimiz index e ekledi

number.pop()#listenin sonundakini siler
number.pop(3)#listenin belirtilen indexini siler
number.remove(40)#yazılan sayıyı siler

number.sort()#listeyi küçükten büyüğe sıralar
number.reverse()#listeyi ters çevirir
letters.reverse()#listeyi ters çevirir

print(number.count(10))#number in içinde kaç 10 var diye sayar



print(number)


