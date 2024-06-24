import tkinter
from ..components import labels, containers, dropdowns, popups


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

    def render(self):
        self.item_selector.place(x=150, y=100)
        self.item_selector_label.place(x=150, y=80)
        self.buy_offers.place(x=150, y=150)
        # self.get_all_offers()

    # def get_all_offers(self) -> list[dict]: #TODO fix issue where running this throws an backend.exceptions.ValidationError
    #     orders = self.parent.backend.get_market_orders()
    #     return orders
