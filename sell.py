from pathlib import Path
import csv
from date import DateTools
from inventory import Inventory
from report import Reporter


class Sales:
    def __init__(self):
        self.sales_file = Path(
            __file__).absolute().parent / "csv-data/sales.csv"

    def last_current_id(self):
        with open(self.sales_file, "r") as csv_sales:
            dictreader = csv.DictReader(csv_sales)
            last_line = ""
            for line in dictreader:
                last_line = line
            last_id = int(last_line["id"])
            return last_id

    def show(self, report_date=""):
        with open(self.sales_file, "r") as csv_sales:
            dictreader = csv.DictReader(csv_sales)
            list_of_dics = list(dictreader)
            csv_sales.seek(0)
            total_profit = 0.00
            for line in dictreader:
                if not line["total_profit"] == "total_profit":
                    total_profit = total_profit + float(line["total_profit"])
            total_profit_dict = {
                "id": "*****",
                "product": "Total profit",
                "quantity": "*****",
                "buy_price": "*****",
                "sell_price": "*****",
                "total_profit": round(total_profit, 2),
                "sell_date": "*****",
            }
            list_of_dics.append(total_profit_dict)
            if report_date:
                filtered_list = []
                for dic in list_of_dics:
                    if dic["sell_date"] == report_date:
                        filtered_list.append(dic)
                filtered_total_profit = 0.00
                for line in filtered_list:
                    if not line["total_profit"] == "total_profit":
                        filtered_total_profit = filtered_total_profit + \
                            float(line["total_profit"])
                filtered_total_profit_dict = {
                    "id": "*****",
                    "product": "Total profit",
                    "quantity": "*****",
                    "buy_price": "*****",
                    "sell_price": "*****",
                    "total_profit": round(filtered_total_profit, 2),
                    "sell_date": "*****",
                }
                filtered_list.append(filtered_total_profit_dict)
                return filtered_list
            return list_of_dics

    def add_to_sales(self, sell_dict):
        with open(self.sales_file, "a", newline="") as csv_sales:
            fieldnames = [
                "id",
                "product",
                "quantity",
                "buy_price",
                "sell_price",
                "total_profit",
                "sell_date",
            ]
            dictwriter = csv.DictWriter(csv_sales, fieldnames=fieldnames)
            del sell_dict["exp_date"]
            del sell_dict["total_price"]
            sell_dict["total_profit"] = round(
                (
                    (float(sell_dict["sell_price"])
                     * float(sell_dict["quantity"]))
                    - (float(sell_dict["buy_price"])
                       * float(sell_dict["quantity"]))
                ),
                2,
            )
            sell_dict["id"] = str(self.last_current_id() + 1)
            dictwriter.writerow(sell_dict)

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
            "sell_date": datetools.get_system_date(),
            "total_price": "",
        }
        sell_inv_check = inventory.check(sell_dict)
        if sell_inv_check["stock"] == False:
            print("**ERROR** Product id unknown or insufficient stock **ERROR**")
        else:
            sell_dict["product"] = sell_inv_check["product"]
            sell_dict["buy_price"] = sell_inv_check["buy_price"]
            sell_dict["exp_date"] = sell_inv_check["exp_date"]
            sell_dict["total_price"] = sell_dict["quantity"] * \
                sell_dict["sell_price"]
            reporter.sale_report(sell_dict)
            inventory.remove(sell_dict)
            self.add_to_sales(sell_dict)
