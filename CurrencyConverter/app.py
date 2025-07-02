import tkinter as tk
from forex_python.converter import CurrencyRates
import requests

api_key = 'ee406631f36eb591ca6d223f'
api_url = 'https://v6.exchangerate-api.com/v6/'

currencies = ['USD', 'RUB', 'EUR', 'KZT', 'GBP', 'AED', 'UZS', 'JPY', 'CAD']


class CurrencyConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Currency Converter')
        self.root.geometry('400x350')

        self.from_var = tk.StringVar()
        self.from_var.set('USD')
        tk.OptionMenu(self.root, self.from_var, *currencies).pack(pady=5)

        self.to_var = tk.StringVar()
        self.to_var.set('EUR')
        tk.OptionMenu(self.root, self.to_var, *currencies).pack(pady=5)

        # amount
        tk.Label(self.root, text='Amount', font=('Arial', 10, 'bold')).pack()
        self.entry_amount = tk.Entry(self.root)
        self.entry_amount.pack(pady=5)

        # Convert Button
        button = tk.Button(self.root,
                           text='Convert',
                           command=self.convert,
                           bg='#45a049',
                           fg='white',
                           activebackground='#45a049',
                           relief='raised',
                           padx=10)

        button.pack(pady=5)

        # result display
        self.result_label = tk.Label(self.root, text='', font=('Arial', 10, 'bold'))
        self.result_label.pack(pady=5)

        # status display
        self.status_label = tk.Label(self.root, text='', fg='red')
        self.status_label.pack(pady=5)

        self.root.mainloop()

    def convert(self):
        try:
            from_curr = self.from_var.get()
            to_curr = self.to_var.get()
            amount = float(self.entry_amount.get())

            # MAKE API request
            url = f'{api_url}{api_key}/pair/{from_curr}/{to_curr}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                rate = data['conversion_rate']
                converted = amount * rate

            self.result_label.config(text=f'Converted: {amount} {from_curr} = {converted:.2f} {to_curr}')
            self.status_label.config(text='')

        except ValueError:
            self.status_label.config(text='Enter a valid numeric amount')
            self.result_label.config(text='')

        except Exception as e:
            self.status_label.config(text=f'Error: {e}')
            self.result_label.config(text='')

CurrencyConverter()
