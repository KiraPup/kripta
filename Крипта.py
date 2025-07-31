import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb


result = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency={currency}&ids={i")
data = json.loads(result.text)
p = pprint.PrettyPrinter(indent=4)
p.pprint(data)

window = Tk()
window.title("Чайник в крипте -  Курсы криптовалют")
window.geometry('500x400')

label = Label(text='Актуальные курсы криптовалют',fg='green', font="Arial 14 bold")
label.pack(pady=10)





window.mainloop()
#CG-Y2YcC3ioomGudnMsjsbpoDVd