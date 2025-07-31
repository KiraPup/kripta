from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_b_label(event):
    code = base_combobox.get()
    name = currencies_b[code]
    b_label.config(text=name)

def update_t_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = target_combobox.get()
    name = currencies_names[code]
    t_label.config(text=name)

currencies_b ={
    'USD':"Американский доллар",
    'EUR':"Евро",
    'RUB':"Российский рубль"
}
currencies= {
    "BTC": 'bitcoin',
    "ETH": 'ethereum',
    "XRP":'ripple',
    'USDT':'tether',
    'BNB':'binancecoin',
    'SOL': 'solana'
}
currencies_names = {
    "BTC": 'Bitcoin',
    "ETH": 'Ethereum',
    "XRP": 'XRP',
    'USDT': 'Tether',
    'BNB': 'BNB',
    'SOL': 'Solana'
}

window = Tk()
window.title("Актуальная информация о криптовалюте")
window.geometry("400x300")

Label(text="Базовая валюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies_b.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Криптовалюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)



Button(text="Получить цену на криптовалюту", command=exchange).pack(padx=10, pady=10)

window.mainloop()