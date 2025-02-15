angka = int(input("Masukkan angka:"))

prima = True
if((angka == 0) or (angka == 1)):
  prima = False
else:
  for i in range(2,(angka//2)):
    if ((angka % i) == 0):
       prima = False
       break
 
if prima :
  print(angka,"adalah prima")
else:
  print(angka,"bukan prima")
