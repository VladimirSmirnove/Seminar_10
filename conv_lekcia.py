from tkinter import Entry
from google_currency import convert  
import json

res = convert('rub', 'usd', 1)
u = json.loads(res)
USD = u["amount"]

res = convert('rub', 'eur', 1)
e = json.loads(res)
EUR = e["amount"]


res = convert('rub', 'gbp', 1)
g = json.loads(res)
GBP = g["amount"]

res = convert('rub', 'cny', 1)
c = json.loads(res)
CNY = c["amount"]

res = convert('rub', 'jpy', 1)
j = json.loads(res)
JPY = j["amount"]

res = convert('rub', 'pkr', 1)
p = json.loads(res)
PKR = p["amount"]

