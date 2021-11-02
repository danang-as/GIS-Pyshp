# Nama : Danang Ari Subarkah
# NPM : 1194042
# Kelas : D4TI 3B
# 1194042 mod 8 = 2 -> membangun bujur sangkar, dan angka 2 terakhir npm = 4, jadi membuat 4 bujur sangkar

import shapefile
w=shapefile.Writer("soal10")
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("mat","satu")
w.record("mit","dua")
w.record("mut","tiga")
w.record("met","empat")

w.poly([[[11,5],[6.5,5], [6.5,1],[11,1], [11,5]]])
w.poly([[[1,5],[5.5,5], [5.5,1],[1,1], [1,5]]])

w.poly([[[11,6],[6.5,6], [6.5,10],[11,10], [11,6]]])
w.poly([[[1,6],[5.5,6], [5.5,10],[1,10], [1,6]]])



w.close()