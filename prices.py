import pandas as pd

class Prices:

    def get_prices(self):

        df = pd.read_html("https://www.elbruk.se/timpriser-se4-malmo",attrs={"class":"table table-striped mb30"})

        max_price = 275
        prices = df[0].iloc[:,:]

        print(prices.loc[2])


Prices().get_prices()