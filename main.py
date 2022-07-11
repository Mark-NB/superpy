# Imports
import argparse
from date import DateTools
from report import Reporter
from inventory import Inventory
from buy import Buyer
from sell import Seller

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
FUNCTIONALITIES = {"buy": "Buy product",
                   "sell": "Sell product",
                   "report": "Generate report",
                   "change_date": "Change the current date"
                   }

REPORTS = {"inventory": "Inventory report",
           "buy": "Buy report",
           "sales": "Sales report",
           "loss": "Loss report"
           }


def main(parsed_args):

    date_tools = DateTools()
    # check if date file is made and sets to today if date is in the past
    date_tools.check_date_file()
    functionality = parsed_args.functionality[0]

    if functionality == "buy":
        buyer = Buyer()
        buyer.buy(parsed_args)

    if functionality == "sell":
        seller = Seller()
        seller.sell(parsed_args)

    if functionality == "report":
        reporter = Reporter()
        report_type = parsed_args.report[0]
        if report_type == "inventory":
            inventory = Inventory()
            reporter.inventory_report(inventory.show())

    if functionality == "change_date":
        date_tools.set_todays_date(parsed_args.date[0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="SuperPy, Stock and Sales tool. Follow instructions below...")
    parser.add_argument(
        "functionality",
        type=str,
        nargs=1,
        choices=FUNCTIONALITIES.keys(),
        help="choose the desired functionality"
    )
    parser.add_argument(
        "-n",
        type=str,
        dest="product",
        nargs=1,
        help="when using buy, enter the name of the item"
    )
    parser.add_argument(
        "-i",
        type=int,
        dest="id",
        nargs=1,
        help="when using sell, enter the id of the item"
    )
    parser.add_argument(
        "-a",
        type=int,
        dest="quantity",
        nargs=1,
        help="when using buy or sell, enter the amount of items"
    )
    parser.add_argument(
        "-p",
        type=float,
        dest="price",
        nargs=1,
        help="when using buy or sell, enter the price of the item"
    )
    parser.add_argument(
        "-d",
        type=str,
        dest="date",
        nargs=1,
        help="when using buy, enter the experation date of the item, when using change_date, enter the desired date for today, in yyyy-mm-dd format"
    )
    parser.add_argument(
        "-r",
        type=str,
        dest="report",
        nargs=1,
        choices=REPORTS.keys(),
        help="when using report, enter the type of report(sales/loss/inventory)"
    )

    parsed_args = parser.parse_args()

    main(parsed_args)

    print("at least the program ran till the end")
