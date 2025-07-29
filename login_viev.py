import tkinter as tk
from tkinter import messagebox

# Kayıtlı kullanıcı adı ve şifre
USERNAME = "admin"
PASSWORD = "12345"

def sign_in():
    username = entry_username.get()
    password = entry_password.get()
    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Başarılı", "Giriş başarılı!")
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış.")

# Ana pencere
root = tk.Tk()
root.title("Giriş Yap")
root.geometry("300x180")
root.configure(bg="yellow")  # Arka planı sarı yap

# Kullanıcı adı etiketi ve giriş kutusu
tk.Label(root, text="Kullanıcı Adı:", bg="yellow").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Şifre etiketi ve giriş kutusu
tk.Label(root, text="Şifre:", bg="yellow").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Giriş yap butonu
tk.Button(root, text="Giriş Yap", command=sign_in, bg="yellow").pack(pady=15)

root.mainloop()