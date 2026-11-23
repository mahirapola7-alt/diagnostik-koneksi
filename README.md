# Diagnostik koneksi HTTPS

Layanan uji koneksi untuk Render. GET `/health` mengembalikan `diagnostic_only` dan `claims_enabled: false`. POST ditolak. Layanan ini tidak melakukan klaim voucher dan tidak boleh digunakan untuk mengirim cookie atau data akun.

Di Render buat Web Service Python pada paket Free dari repositori ini. Build command: `python -m compileall -q app.py`. Start command: `python app.py`. HTTPS disediakan Render. Jangan arahkan APK yang membawa data akun ke layanan uji ini.
