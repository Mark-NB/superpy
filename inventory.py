from pathlib import Path
from datetime import datetime
import csv


class Inventory():
    def __init__(self):
        self.inventory_file = Path(
            __file__).absolute().parent / "csv-data/inventory.csv"

    def last_current_id(self):
        with open(self.inventory_file, "r") as csv_inventory:
            dictreader = csv.DictReader(csv_inventory)
            last_line = ""
            for line in dictreader:
                last_line = line
            last_id = int(last_line["id"])
            return last_id

    def show(self, report_date="", report_second_date=""):
        with open(self.inventory_file, "r") as csv_inventory:
            dictreader = csv.DictReader(csv_inventory)
            list_of_dics = list(dictreader)
            if report_second_date and report_date:
                format = "%Y-%m-%d"
                first_date = datetime.strptime(report_date, format)
                second_date = datetime.strptime(report_second_date, format)
                filtered_list = []
                for dic in list_of_dics:
                    current_dic_date = datetime.strptime(dic["buy_date"], format)
                    if current_dic_date <= second_date and current_dic_date >= first_date:
                        filtered_list.append(dic)
                return filtered_list        
            elif report_date:
                filtered_list = []
                for dic in list_of_dics:
                    if dic["buy_date"] == report_date:
                        filtered_list.append(dic)
                return filtered_list
            return list_of_dics

    def check(self, item_dict):
        item_id = str(item_dict["id"])
        item_quantity = int(item_dict["quantity"])
        with open(self.inventory_file, "r") as csv_inventory:
            dictreader = csv.DictReader(csv_inventory)
            for line in dictreader:
                if line["id"] == item_id:
                    if int(line["quantity"]) >= item_quantity:
                        return {"stock": True,
                                "product": line["product"],
                                "buy_price": line["buy_price"],
                                "exp_date": line["exp_date"]
                                }
        return {"stock": False}

    def add(self, add_dict):
        with open(self.inventory_file, "a", newline="") as csv_inventory:
            fieldnames = ["id", "product", "quantity",
                          "buy_price", "exp_date", "buy_date"]
            dictwriter = csv.DictWriter(csv_inventory, fieldnames=fieldnames)
            add_dict["id"] = str(self.last_current_id()+1)
            dictwriter.writerow(add_dict)

    def remove(self, remove_dict):
        item_id = str(remove_dict["id"])
        item_quantity = int(remove_dict["quantity"])
        with open(self.inventory_file, "r+") as csv_inventory:
            dictreader = csv.DictReader(csv_inventory)

            dicts = []
            for dic in dictreader:
                if dic["id"] == item_id:
                    dic["quantity"] = int(dic["quantity"]) - item_quantity
                if int(dic["quantity"]) > 0:
                    dicts.append(dic)
                else:
                    pass

            with open(self.inventory_file, "w", newline="") as csv_inventory_write:
                fieldnames = ["id", "product", "quantity",
                              "buy_price", "exp_date", "buy_date"]
                dictwriter = csv.DictWriter(
                    csv_inventory_write, fieldnames=fieldnames)
                dictwriter.writeheader()
                dictwriter.writerows(dicts)
