# Tugas Besar IF2124 Teori Bahasa Formal dan Otomata
# Compiler Bahasa Python
<h2>Deskripsi Permasalahan</h2>
<p>Python adalah bahasa interpreter tingkat tinggi (high-level), dan juga general-purpose. Python diciptakan oleh Guido van Rossum dan dirilis pertama kali pada tahun 1991. Filosofi desain pemrograman Python mengutamakan code readability dengan penggunaan whitespace-nya. Python adalah bahasa multiparadigma karena mengimplementasi paradigma fungsional, imperatif, berorientasi objek, dan reflektif.</p>
<p>Dalam proses pembuatan program dari sebuah bahasa menjadi instruksi yang dapat dieksekusi oleh mesin, terdapat pemeriksaan sintaks atau kompilasi bahasa yang dibuat oleh programmer. Kompilasi ini bertujuan untuk memastikan instruksi yang dibuat oleh programmer mengikuti aturan yang sudah ditentukan oleh bahasa tersebut. Baik bahasa berjenis interpreter maupun compiler, keduanya pasti melakukan pemeriksaan sintaks. Perbedaannya terletak pada apa yang dilakukan setelah proses pemeriksaan (kompilasi/compile) tersebut selesai dilakukan.</p>
<p>Dibutuhkan grammar bahasa dan algoritma parser untuk melakukan kompilasi. Sudah sangat banyak grammar dan algoritma yang dikembangkan untuk menghasilkan compiler dengan performa yang tinggi. Terdapat CFG, CNF-e, CNF+e, 2NF, 2LF, dll untuk grammar yang dapat digunakan, dan terdapat LL(0), LL(1), CYK, Earley’s Algorithm, LALR, GLR, Shift-reduce, SLR, LR(1), dll untuk algoritma yang dapat digunakan untuk melakukan parsing.</p>
<p>Pada tugas besar ini, implementasikanlah compiler untuk Python untuk statement-statement dan sintaks-sintaks bawaan Python. Gunakanlah konsep CFG untuk pengerjaan compiler yang mengevaluasi syntax program. Untuk nama variabel dalam program, gunakanlah FA.</p>
<p>Algoritma yang dipakai dibebaskan, namun tim asisten menyarankan menggunakan algoritma CYK (Cocke-Younger-Kasami). Algoritma CYK harus menggunakan grammar CNF (Chomsky Normal Form) sebagai grammar masukannya. Oleh karena itu, jika ingin menggunakan CYK buatlah terlebih dahulu grammar dalam CFG (Context Free Grammar), kemudian konversikan grammar CFG tersebut ke grammar CNF.</p>

## Cara Penggunaan Program
```
/* 1. Apabila ingin menggunakan testcase yang sudah ada */

cd src  
python main.py testcase/<nama-file>

/* 2. Apabila ingin menggunakan file yang baru */

/* Upload file yang ingin dijalankan ke dalam folder testcase */

cd src
python main.py testcase/<nama-file>

```
## REFERENSI
'''
https://www.w3schools.com/python/python_regex.asp
https://github.com/RobMcH/CYK-Parser
https://www.tutorialspoint.com/compiler_design/compiler_design_syntax_analysis.htm
'''
## Kelompok 19 Kelas K03
## Anggota Kelompok:
| NIM      | NAMA                     |
|----------|--------------------------|
| 13520137 | Muhammad Gilang Ramadhan | 
| 13520160 | Willy Wilsen             | 
| 13520165 | Ghazian Tsabit Alkamil   |
