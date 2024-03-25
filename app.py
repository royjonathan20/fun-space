#luas segitiga
def luas_segitiga():
    a = int(input("Masukkan alas segitiga: ")) 
    t = int(input("Masukkan tinggi segitiga: ")) 
    luas = a * t / 2 
    print("luas segitiga adalah: ", luas) 
   
luas_segitiga()  

#luas persegi panjang 
def luas_persegi_panjang():
    p = int(input("Masukkan panjang persegi:" ))
    l = int(input("Masukkan lebar persegi: ")) 
    luas = p * l
    print("Luas persegi panjang adalah: ", luas) 
    
luas_persegi_panjang() 

#luas lingkaran
def luas_lingkaran():
    r = int(input("Masukkan jari-jari lingkaran: ")) 
    luas = 3.14 * r * r
    print("Luas Lingkaran adalah: ", luas) 
    
luas_lingkaran() 