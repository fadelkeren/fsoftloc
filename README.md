# FSoftLoc - IP Locator 🌐

FSoftLoc adalah sebuah aplikasi sederhana berbasis Python yang digunakan untuk melacak informasi lokasi berdasarkan alamat IP dari sebuah website. Aplikasi ini dapat membantu Anda mengetahui lokasi geografis, ISP, dan detail lainnya dari alamat IP yang terkait dengan domain tertentu.

## Fitur ✨
- Melacak lokasi geografis berdasarkan alamat IP.
- Informasi mencakup: negara, kota, ISP, latitude, longitude, dan lainnya.
- Antarmuka berbasis terminal dengan tampilan berwarna untuk pengalaman yang lebih menarik.
- Interaktif: Meminta verifikasi pengguna sebelum aplikasi dijalankan.

## Prasyarat 📋
Sebelum menggunakan aplikasi ini, pastikan Anda telah menginstal:
1. **Python 3.6+**  
   Pastikan Python sudah terinstal di sistem Anda. Jika belum, silakan unduh dan instal dari [python.org](https://www.python.org/).
2. **Paket `requests` dan `colorama`**  
   Gunakan `pip` untuk menginstalnya:
   ```bash
   pip install requests colorama
Instalasi 🛠️
1. Clone atau unduh repository ini.
   ```bash
   git clone https://github.com/fadelkeren/fsoftloc.git
   cd fsoftloc

2. Pastikan semua dependensi sudah terinstal:
   ```bash
   pip install colorama
   pip install requests
3. Jalankan aplikasi menggunakan python
   ```bash
   python fsoftloc.py


# Cara Penggunaan 🚀
1. Jalankan aplikasi di terminal/command prompt:
   ```bash
   python fsoftloc.py
2. Anda akan diminta untuk mengetik fadelkeren untuk melanjutkan.
3. Setelah itu, masukkan nama domain yang ingin Anda lacak (contoh: google.com).
4. Aplikasi akan menampilkan:
   - Alamat IP domain tersebut.
   - Informasi lokasi lengkap termasuk negara, kota, ISP, latitude, dan longitude.

Contoh OUTPUT:
```plaintext
  ================================
        FSoftLoc - IP Locator
  ================================
  
  Ketik 'fadelkeren' untuk melanjutkan: fadelkeren
  Akses diterima! Selamat menggunakan FSoftLoc!
  Masukkan nama domain (contoh: google.com): google.com
  Alamat IP untuk google.com: 142.250.190.78
  Informasi Lokasi:
  IP: 142.250.190.78
  Country: United States
  Region: California
  City: Mountain View
  ISP: Google LLC
  Lat: 37.4056
  Lon: -122.0775

```

# Catatan ⚠️

Aplikasi ini menggunakan API dari ip-api.com yang memiliki batasan 45 request per menit pada versi gratis. Jika Anda melebihi batas tersebut, Anda akan mendapatkan pesan error.
Untuk keperluan yang lebih besar atau produksi, pertimbangkan untuk menggunakan layanan API geolokasi berbayar.

Dibuat dengan ❤️ oleh Fadelkeren
