#DNA-RNA Dönüşüm Kodu
#Gökhan Şener

def rnaToDna(rna): #RNA'nın DNA'ya dönüşümü
    rna = rna.replace("U","T") #Urasil, Timine dönüşecek.
    return rna

def dnaToRna(dna):
    dna = dna.replace("T", "U") #Timin, Urasile dönüşecek.
    return dna

data = input("Dizini giriniz: ") #input ile veriyi aldık.
data = data.upper() #Alınan verileri büyük harfe dönüştürdük.
print("DNA Veriniz: " + rnaToDna(data))
print("RNA Veriniz: " + dnaToRna(data))
