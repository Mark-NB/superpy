from inventory import Inventory
from report import Reporter
from date import DateTools


class Buyer():
    def __init__(self):
        pass

    def buy(self, buy_args):
        datetools = DateTools()
        add_dict = {
            "product": buy_args.product[0],
            "quantity": buy_args.quantity[0],
            "buy_price": buy_args.price[0],
            "exp_date": buy_args.date[0],
            "buy_date": datetools.get_system_date()
        }
        inventory = Inventory()
        inventory.add(add_dict)
        reporter = Reporter()
        reporter.buy_report(add_dict)
