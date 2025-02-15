NIU = int(input("Masukkan NIU: "))
tugas = float(input("Masukkan nilai tugas: "))
laporan = float(input("Masukkan nilai laporan: "))
rata_rata = (tugas+laporan)/2
if rata_rata < 40:
    print("Nilai Mahasiswa adalah K. Selesai.")
else:
    nilai_ujian = int(input("Masukkan nilai ujian:"))
nilai_akhir = (tugas * 0.25) + (laporan * 0.25) + (nilai_ujian * 0.50)
if nilai_akhir >= 80:
        print("Nilai : A")
elif nilai_akhir >= 70:
        print("Nilai : B")
elif nilai_akhir >= 60:
        print("Nilai : C")
elif nilai_akhir >= 50:
        print("Nilai : D")
else:
       print("Nilai : E")
