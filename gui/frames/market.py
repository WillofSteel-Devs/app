import tkinter
from ..components import labels, containers, dropdowns, popups, inputs
from models import order

class MarketFrame(tkinter.Frame):
    def __init__(self, parent, bg="gray"):
        super().__init__(parent, width=650, height=600, bg=bg)
        self.parent = parent
        self.bg = bg

        self.item_selector = dropdowns.Dropdown(
            self, ["Placeholder One", "Placeholder Two", "Placeholder Three"]
        )
        self.item_selector_label = labels.InputLabel(self, "Item", bg="white")

        self.buy_offers = tkinter.Listbox(self, bg=self.bg)
        self.buy_offers_label = labels.InputLabel(self, "Buy Offers", bg="white")
        
        self.sell_offers = tkinter.Listbox(self, bg=self.bg)
        self.sell_offers_label = labels.InputLabel(self, "Sell Offers", bg="white")

        self.refresh_button = tkinter.Button(self, bg="green", text="Refresh", command=self.get_all_offers)

        self.amount = inputs.IntergerOnlyEntry(self, 0, 100)
        self.amount_label = labels.InputLabel(self, "Amount", bg=self.bg)

        self.price_per = inputs.IntergerOnlyEntry(self, 0, 2000)
        self.price_per_label = labels.InputLabel(self, "Price Per Item", bg=self.bg)

        self.instant_buy_button = tkinter.Button(self, bg="green", text="Buy Instantly")
        self.instant_sell_button = tkinter.Button(self, bg="red", text="Sell Instantly")

        self.accept_offer_button = tkinter.Button(self, bg="yellow", text="Accept Offer")

        self.create_offer_button = tkinter.Button(self, bg="green", text="Create Offer")



    def render(self):
        self.item_selector.place(x=100, y=50)
        self.item_selector_label.place(x=100, y=20)
        
        self.buy_offers.place(x=100, y=190)
        self.buy_offers_label.place(x=100, y=160)
        self.sell_offers.place(x=275, y=190)
        self.sell_offers_label.place(x=275, y=160)
        
        self.refresh_button.place(x=500, y=30)
        
        self.amount.place(x=500, y=100)
        self.amount_label.place(x=500, y=80)

        self.instant_buy_button.place(x=500, y=200)
        self.instant_sell_button.place(x=500, y=230)

        self.accept_offer_button.place(x=500, y=260)

        self.price_per.place(x=350, y=450)
        self.price_per_label.place(x=350, y=420)

        self.create_offer_button.place(x=500, y=420)

        self.get_all_offers()

    def get_all_offers(self, item_type = None) -> list[dict]: #TODO make this use actual data from the api
        ...
        # orders = self.parent.backend.get_market_orders()
        # return orders