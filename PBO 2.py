class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_mahasiswa(self):
        print("\nNama: ", self.nama)
        print("NIM: ", self.nim)
        print("Jurusan: ", self.jurusan.NamaJurusan)

#Pada kode diatas ialah Kelas mahasiswa dimana saya membuat variabel objek nama, nim, dan jurusan dan membuat variabel daftar mahasiswa jika ingin menampilkan semua daftar mahasiswa yang ada di dalam universitas tersebut. 

class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("\nDaftar Mahasiswa di Jurusan :", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("Nama: ", mahasiswa.nama)
            print("NIM: ", mahasiswa.nim)

#Pada kode diatas saya membuat Kelas jurusan yang mana akan menampilkan daftar mahasiswa yang masuk kedalam jurusan yang ada di dalamnya

class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("\nDaftar Jurusan di Universitas :", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print("Nama Jurusan: ", jurusan.NamaJurusan)

#Pada kode ketiga ini saya membuat Kelas universitas yang berisikan objek nama universitas lalu didalam kelas ini ada variabel tambah jurusan dan daftar jurusan.

# Membuat objek Universitas
universitas = Universitas("XYZ University")

# Membuat objek Jurusan
jurusan1 = Jurusan("Teknik Informatika")
jurusan2 = Jurusan("Teknik Sipil")

# Menambahkan jurusan ke daftar jurusan di universitas
universitas.tambah_jurusan(jurusan1)
universitas.tambah_jurusan(jurusan2)

# Membuat objek Mahasiswa
mahasiswa1 = Mahasiswa("M.Hafidz Ashshidiqi", "G1A022079", jurusan1)

# Menambahkan mahasiswa ke daftar mahasiswa di jurusan
jurusan1.tambah_mahasiswa(mahasiswa1)

# Menampilkan daftar jurusan di universitas
universitas.tampilkan_daftar_jurusan()

#Menampilkan daftar mahasiswa dalam jurusan
jurusan1.tampilkan_daftar_mahasiswa()

# Menampilkan informasi mahasiswa
mahasiswa1.tampilkan_mahasiswa()

