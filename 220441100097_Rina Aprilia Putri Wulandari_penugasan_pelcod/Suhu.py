print("1. Konversi Fahrenheit ke Reamur")
print("2. Konversi Fahrenheit ke Celcius")
print("3. Konversi Celcius ke Reamur")
print("4. Konversi Celcius ke Kelvin")
print("5. Konversi Celcius ke Fahrenheit")
print("6. Konversi Reamur ke Kelvin")
print("7. Konversi Reamur ke Celcius")
print("8. Konversi Kelvin ke Celcius")
print("9. Konversi Kelvin ke Reamur")

pilih = int(input("pilih nomor yang anda inginkan"))

if pilih == 1:
     Fahrenheit = float(input("masukan Fahrenheit: "))
     Reamur = (4/9)*Fahrenheit-32
     print("hasil Reamurnya adalah=", Reamur, "Reamur")

if pilih == 2:
     Fahrenheit = float(input("masukan Fahrenheit: "))
     Celcius = (5/9)*Fahrenheit-32
     print("hasil Celciusnya adalah=", Celcius, "Celcius")

if pilih == 3:
     Celcius = float(input("masukan Celcius"))
     Reamur = (4/5)*Celcius
     print("hasil Reamurnya adalah=", Reamur, "Reamur")

if pilih == 4:
     Celcius = float(input("masukan Celcius"))
     Kelvin = Celcius+273
     print("hasil Kelvinnya adalah=", Kelvin, "Kelvin")

if pilih == 5:
     Celcius = float(input("masukan Celcius"))
     Fahrenheit = (9/5)*Celcius+32
     print("hasil Fahrenheitnya adalah=", Fahrenheit, "Fahrenheit")

if pilih == 6:
     Reamur = float(input("masukan Reamur")) 
     Kelvin = (5/4)*Reamur+273
     print(input("hasil Kelvinnya adalah=", Kelvin, "Kelvin")) 

if pilih == 7:
     Reamur = float(input("masukan Reamur")) 
     Celcius = (5/4)*Reamur
     print(input("hasil Celciusnya adalah=", Celcius, "Celcius")) 

if pilih == 8:
     Kelvin = float(input("masukan Kelvin")) 
     Celcius = Kelvin-273
     print(input("hasil Celciusnya adalah=", Celcius, "Celcius")) 

if pilih == 9:
     Kelvin = float(input("masukan Kelvin")) 
     Reamur = (4/5)*Kelvin-273
     print(input("hasil Kelvinnya adalah=", Kelvin, "Kelvin")) 