
#nilai andi
tugas = 85
uts = 75
uas = 90

#bobot
bobot_tugas = 0.3
bobot_uts = 0.3
bobot_uas = 0.4

#nilai akhir
nilai_tugas = tugas * bobot_tugas
nilai_uts = uts * bobot_uts
nilai_uas = uas * bobot_uas

total = nilai_tugas + nilai_uts + nilai_uas

#perhitungan
print("--- Nilai yang Kamu Peroleh ---")
print("Nilai Tugas:", tugas)
print("Nilai UTS:", uts)
print("Nilai UAS:", uas)
print("===============================")
print("Nilai akhir dari Tugas (30%):", nilai_tugas)
print("Nilai akhir dari UTS (30%):", nilai_uts)
print("Nilai akhir dari UAS (40%):", nilai_uas)
print("-------------------------------")
print("Total Nilai Akhir Kamu:", total)
