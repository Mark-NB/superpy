from pathlib import Path
import csv
from date import DateTools
from inventory import Inventory
from report import Reporter


class Seller():
    def __init__(self):
        self.sales_file = Path(
            __file__).absolute().parent / "csv-data/sales.csv"

    def last_current_id(self):
        with open(self.sales_file, "r") as csv_inventory:
            dictreader = csv.DictReader(csv_inventory)
            last_line = ""
            for line in dictreader:
                last_line = line
            last_id = int(last_line["id"])
            return last_id

    def sell(self, sell_args):
        datetools = DateTools()
        inventory = Inventory()
        reporter = Reporter()
        sell_dict = {
            "id": sell_args.id[0],
            "product": "",
            "quantity": sell_args.quantity[0],
            "buy_price": "",
            "sell_price": sell_args.price[0],
            "exp_date": "",
            "sell_date": datetools.get_todays_date(),
            "total_price": ""
        }
        sell_inv_check = inventory.check(sell_dict)
        print(sell_inv_check)
        if sell_inv_check["stock"] == False:
            print("Product id unknown or insufficient stock")
        else:
            sell_dict["product"] = sell_inv_check["product"]
            sell_dict["buy_price"] = sell_inv_check["buy_price"]
            sell_dict["exp_date"] = sell_inv_check["exp_date"]
            sell_dict["total_price"] = sell_dict["quantity"] * \
                sell_dict["sell_price"]
            reporter.sale_report(sell_dict)
            inventory.remove(sell_dict)
            self.add_to_sales(sell_dict)

    # remove total_price and exp_date from dict? add profit?
    def add_to_sales(self, sales_dict):
        with open(self.sales_file, "a", newline="") as csv_sales:
            fieldnames = ["id", "product", "quantity",
                          "buy_price", "sell_price", "profit", "sell_date"]
            dictwriter = csv.DictWriter(csv_sales, fieldnames=fieldnames)
            sales_dict["id"] = str(self.last_current_id()+1)
            dictwriter.writerow(sales_dict)
