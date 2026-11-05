# auth.py

import os
from database import database_user

def register_akun():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- REGISTRASI AKUN BARU ---")
    username_baru = input("Buat Username baru: ")
    
    try:
        if len(username_baru) < 4:
            raise ValueError("Username minimal harus memiliki 4 karakter!")
        if username_baru in database_user:
            print("Username sudah terdaftar! Gunakan username lain.")
        else:
            password_baru = input("Buat Password baru (min 6 karakter): ")
            if len(password_baru) < 6:
                raise ValueError("Password terlalu pendek, minimal 6 karakter!")
            
            database_user[username_baru] = [password_baru, "Pengguna"]
            print("Registrasi berhasil! Silakan login.")
    except ValueError as e_reg:
        print(f"Gagal Registrasi: {e_reg}")
    finally:
        print("[Info]: Proses registrasi selesai diproses.")

def login_akun():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- HALAMAN LOGIN ---")
    username_input = input("Username: ")
    password_input = input("Password: ")
    
    try:
        if username_input not in database_user:
            raise KeyError("Username tidak ditemukan di dalam database!")
        
        if database_user[username_input][0] != password_input:
            raise ValueError("Password yang Anda masukkan salah!")
    except KeyError as ke:
        print(f"Error Login: {ke}")
        return None, None
    except ValueError as ve:
        print(f"Error Login: {ve}")
        return None, None
    else:
        role_login = database_user[username_input][1]
        print(f"Login berhasil sebagai {role_login}!")
        return username_input, role_login