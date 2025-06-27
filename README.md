# Bank Harapan Palsu - Eksploitasi Error Messages & IDOR

> Web CTF Challenge | by [ctflabs-id](https://github.com/ctflabs-id)


---

## 📖 Scenario

Sebuah bank palsu memiliki sistem internet banking yang rentan. Peserta harus memanfaatkan error messages yang bocor informasi sensitif dan IDOR untuk mendapatkan akses tak berwenang.

---

## 🎯 Challenge Overview
**Target:** `http://bank-palsu.local:5000`<br>
**Vulnerability:** Information Disclosure melalui error messages, Insecure Direct Object Reference (IDOR)<br>
**Objective:** Eksploitasi kerentanan untuk mendapatkan akses ke akun admin (ID: 1001) dan temukan flag<br>
**Difficulty:** ⭐⭐⭐☆☆ (Intermediate)

---
## 🛠️ Setup Instructions

Prerequisites:

    Python 3.8+
    Flask
    SQLite3
    
Langkah-langkah:

  1. Clone repository ini
```bash
git clone https://github.com/ctflabs-id/Bank-Palsu-CTF.git
cd Bank-Palsu-CTF
```
  2. Install dependencies
```bash
pip install flask
```
  3. Start Server
```bash
python app.py
```
  5. Server akan berjalan di http://localhost:5000 atau http://127.0.0.1:5000

---

## 💡 Hints
    🔍 Error messages bisa membocorkan informasi sensitif
    🕵️‍♂️ Coba input khusus di form login untuk melihat respon error
    💉 SQL Injection mungkin bisa dilakukan
    🔢 Perhatikan pola ID user
    🚩 Flag hanya muncul di akun admin (ID 1001)

---

## 🎓 Tujuan Tantangan Ini
  1. Memahami bahaya information disclosure
  2. Belajar mengidentifikasi IDOR
  3. Menganalisis error messages untuk mendapatkan informasi
  4. Teknik eksploitasi kerentanan di sistem perbankan

---

## ⚠️ Disclaimer

Challenge ini dibuat hanya untuk edukasi dan simulasi keamanan siber. Jangan gunakan teknik serupa terhadap sistem yang tidak kamu miliki atau tidak diizinkan.

---
<details><summary><h2>🏆 Solusi yang Diharapkan - (Spoiler Allert)</h2></summary>

Peserta harus:

Langkah 1: Information Disclosure
  1. Coba login dengan username acak:
     ```txt
     Username: test
     Password: test
     ```
  2. Dapatkan error message yang mengungkap username valid:
     ```txt
     Error: Login failed for user: test
     ```
Langkah 2: SQL Injection
  1. Gunakan SQL Injection untuk bypass login:
     ```sql
     Username: admin' --
     Password: [kosongkan]
     ```
  2. Akan di-redirect ke /account/1001
Alternatif: IDOR
  1. Login dengan user biasa:
     ```txt
     Username: user1
     Password: weakpass123
     ```
  2. Akan diarahkan ke /account/1000
  3. Modifikasi URL ke /account/1001 untuk mengakses akun admin
</details>

---

## 🤝 Kontribusi Pull request & issue welcome via: ctflabs-id/EBook-Premium-CTF
## 🧠 Maintained by:
```
GitHub: @ctflabs-id
Website: ctflabsid.my.id
```
