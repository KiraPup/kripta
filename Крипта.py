import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def update_currency_label(event):
    code.combobox.get()
    name = currencies[code]
    currency_label.config(text=name)




p = pprint.PrettyPrinter(indent=4)

result = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency={currency}&ids={i")
data = json.loads(result.text)
p.pprint(data)

window = Tk()
window.title("Чайник в крипте -  Курсы криптовалют")
window.geometry('500x400')


label = Label(text='Актуальные курсы криптовалют',fg='green', font="Arial 14 bold")
label.pack(pady=10)

v_label = Label(text='Выберите код валюты: ',fg = '#20F560')
v_label.pack(padx=10, pady=10)

popular_currencies = ["EUR", "RUB","USD"]
combobox = ttk.Combobox(values=popular_currencies)
combobox.pack(padx=5,pady=5)

currencies= {
    "BTC": 'Bitcoin',
    "ETH": 'Ethereum',
    "XRP":'XRP',
    'USDT':'Tether',
    'BNB':'BNB',
    'SOL': 'Solana'
}

window.mainloop()
#CG-Y2YcC3ioomGudnMsjsbpoDVd