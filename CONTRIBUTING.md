# Contributing to light-utils-py

Terima kasih sudah tertarik berkontribusi!  
Project ini dibuat agar siapa pun bisa ikut menambahkan utilitas kecil yang berguna.

## Cara Berkontribusi

### 1. Fork Repository
Klik tombol **Fork** di kanan atas repositori.

### 2. Clone Fork Kamu
git clone https://github.com/
<username>/light-utils-py.git
git clone https://github.com/
<username>/light-utils-py.git

### 3. Buat Branch Baru
git checkout -b feature/nama-fitur

### 4. Install Project (mode editable)
pip install -e .

### 5. Tambahkan Fitur / Perbaikan
Contoh kontribusi yang diterima:
- menambah fungsi utilitas baru
- memperbaiki bug
- meningkatkan dokumentasi
- menambah contoh penggunaan (examples/)
- menambah unit test

### 6. Jalankan Test
pytest

### 7. Commit & Push
git add .
git commit -m "Add: util baru untuk ..."
git push origin feature/nama-fitur

### 8. Buat Pull Request
Masuk ke GitHub → buka repo kamu → klik **Compare & Pull Request**.

Pastikan PR kamu jelasin:
- apa yang ditambah
- kenapa bermanfaat
- file mana saja yang berubah

## Aturan Koding
- Ikuti gaya kode PEP8.
- Gunakan nama fungsi yang jelas dan deskriptif.
- Kalau menambah file baru, letakkan di folder yang sesuai.

## Tambahan
- Jangan ubah versi project secara manual.
- Jangan hapus file orang lain tanpa alasan kuat.
- Semua fungsi baru wajib punya minimal 1 test sederhana.

Terima kasih sudah membantu project ini berkembang!
