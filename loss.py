from pathlib import Path
import csv
from date import DateTools
from datetime import datetime
from inventory import Inventory
from report import Reporter


class Loss:
    def __init__(self):
        self.loss_file = Path(
            __file__).absolute().parent / "csv-data/loss.csv"

    def last_current_id(self):
        with open(self.loss_file, "r") as csv_loss:
            dictreader = csv.DictReader(csv_loss)
            last_line = ""
            for line in dictreader:
                last_line = line
            last_id = int(last_line["id"])
            return last_id

    def show(self, report_date="", report_second_date=""):
        with open(self.loss_file, "r") as csv_loss:
            dictreader = csv.DictReader(csv_loss)
            list_of_dics = list(dictreader)
            csv_loss.seek(0)
            total_loss = 0.00
            for line in dictreader:
                if not line["total_loss"] == "total_loss":
                    total_loss = total_loss + float(line["total_loss"])
            total_loss_dict = {
                "id": "*****",
                "product": "Total loss",
                "quantity": "*****",
                "buy_price": "*****",
                "total_loss": round(total_loss, 2),
                "loss_date": "*****",
            }
            list_of_dics.append(total_loss_dict)
            if report_second_date and report_date:
                format = "%Y-%m-%d"
                first_date = datetime.strptime(report_date, format)
                second_date = datetime.strptime(report_second_date, format)
                filtered_list = []
                for dic in list_of_dics:
                    if dic["loss_date"] == "*****":
                        continue
                    current_dic_date = datetime.strptime(dic["loss_date"], format)
                    if current_dic_date <= second_date and current_dic_date >= first_date:
                        filtered_list.append(dic)
                filtered_total_loss = 0.00
                for line in filtered_list:
                    if not line["total_loss"] == "total_loss":
                        filtered_total_loss = filtered_total_loss + \
                            float(line["total_loss"])
                filtered_total_loss_dict = {
                    "id": "*****",
                    "product": "Total loss",
                    "quantity": "*****",
                    "buy_price": "*****",
                    "total_loss": round(filtered_total_loss, 2),
                    "loss_date": "*****",
                }
                filtered_list.append(filtered_total_loss_dict)
                return filtered_list
            elif report_date:
                filtered_list = []
                for dic in list_of_dics:
                    if dic["loss_date"] == report_date:
                        filtered_list.append(dic)
                filtered_total_loss = 0.00
                for line in filtered_list:
                    if not line["total_loss"] == "total_loss":
                        filtered_total_loss = filtered_total_loss + \
                            float(line["total_loss"])
                filtered_total_loss_dict = {
                    "id": "*****",
                    "product": "Total loss",
                    "quantity": "*****",
                    "buy_price": "*****",
                    "total_loss": round(filtered_total_loss, 2),
                    "loss_date": "*****",
                }
                filtered_list.append(filtered_total_loss_dict)
                return filtered_list
            return list_of_dics

    def add_to_loss(self, losses_list):
        date_tools = DateTools()
        reporter = Reporter()
        list_for_reporter = []
        for dic in losses_list:
            with open(self.loss_file, "a", newline="") as csv_loss:
                fieldnames = [
                    "id",
                    "product",
                    "quantity",
                    "buy_price",
                    "total_loss",
                    "loss_date",
                ]
                dictwriter = csv.DictWriter(csv_loss, fieldnames=fieldnames)
                del dic["exp_date"]
                del dic["buy_date"]
                dic["total_loss"] = round(
                    float(dic["buy_price"])
                    * float(dic["quantity"]),
                    2,
                )
                dic["id"] = str(self.last_current_id() + 1)
                dic["loss_date"] = date_tools.get_system_date()
                dictwriter.writerow(dic)
                list_for_reporter.append(dic)
        reporter.loss_report(list_for_reporter)

    def check_inventory_expiration(self):
        inventory = Inventory()
        date_tools = DateTools()
        current_inventory = inventory.show()
        list_of_expired_products = []
        anything_expired = False
        for dic in current_inventory:
            has_expired = date_tools.check_if_expired(dic["exp_date"])
            if has_expired:
                list_of_expired_products.append(dic)
                anything_expired = True
        if anything_expired:
            discard_products = input(
                "\n----- One or more products in stock have reached their expiration date, do you wish to discard these products? (yes/no)\n")
            if discard_products == "yes":
                for dic in list_of_expired_products:
                    inventory.remove(dic)
                self.add_to_loss(list_of_expired_products)
