import argparse
from date import DateTools
from report import Reporter
from inventory import Inventory
from buy import Buyer
from sell import Sales
from loss import Loss

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
FUNCTIONALITIES = {"buy": "Buy product",
                   "sell": "Sell product",
                   "report": "Generate report",
                   "advance_date": "Advance from today's date",
                   "set_date": "Set the current date"
                   }

REPORTS = {"inventory": "Inventory report",
           "buy": "Buy report",
           "sales": "Sales report",
           "loss": "Loss report",
           "profit": "Profit report"
           }


def main(parsed_args):

    print(f"\n----- SuperPy, Stock and Sales tool -----\n")

    date_tools = DateTools()
    # check if date file is correctly present
    date_tools.check_date_file()

    functionality = parsed_args.functionality[0]

    # if no date based functionality is chosen, checks if system date is behind today's date and prompts user if update is wanted
    if not functionality == "set_date" and not functionality == "advance_date":
        date_tools.check_if_set_to_today()

    if functionality == "advance_date":
        date_tools.advance_todays_date(parsed_args.quantity[0])

    if functionality == "set_date":
        date_tools.set_todays_date(parsed_args.date[0])

    # checks current inventory for expired products, then prompts user for discarding
    loss = Loss()
    loss.check_inventory_expiration()

    # buys product, adds to inventory, shows buy report
    if functionality == "buy":
        buyer = Buyer()
        buyer.buy(parsed_args)

    # checks stock, sells product, removes from inventory, shows sale report
    if functionality == "sell":
        sales = Sales()
        sales.sell(parsed_args)

    # get's correct data from csv depending on report type/parameters, shows corresponding report
    if functionality == "report":
        reporter = Reporter()
        report_type = parsed_args.report[0]
        report_date = ""
        report_second_date = ""
        if parsed_args.date:
            report_date = parsed_args.date[0]
        if parsed_args.second_date:
            report_second_date = parsed_args.second_date[0]
        if parsed_args.second_date and not parsed_args.date:
            print(
                f"\n**ERROR** Only a second date was provided (-t), please also provide a first date (-d). **ERROR**\n")
            exit()
        if report_date:
            date_tools.check_date_validity(report_date)
        if report_second_date:
            date_tools.check_date_validity(report_second_date)
        if report_type == "inventory":
            inventory = Inventory()
            reporter.inventory_report(inventory.show(
                report_date, report_second_date))
        if report_type == "sales":
            sales = Sales()
            reporter.sales_report(sales.show(report_date, report_second_date))
        if report_type == "loss":
            loss = Loss()
            reporter.losses_report(loss.show(report_date, report_second_date))
        if report_type == "profit":
            sales = Sales()
            loss = Loss()
            sales_show = sales.show(report_date, report_second_date)
            total_revenue = sales_show[-1]["total_revenue"]
            total_margin = sales_show[-1]["total_margin"]
            loss_show = loss.show(report_date, report_second_date)
            total_loss = loss_show[-1]["total_loss"]
            profit_dict = {
                "total_revenue": total_revenue,
                "total_margin": total_margin,
                "total_loss": total_loss,
                "total_profit": round((total_margin - total_loss), 2)
            }
            reporter.profit_report(profit_dict)

    print(
        f"\n----- SuperPy system date: {date_tools.get_system_date()} -----\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="SuperPy, Stock and Sales tool. Follow the instructions below... A complete manual is available in the manual.txt file.")
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
        help="using buy: item name"
    )
    parser.add_argument(
        "-i",
        type=int,
        dest="id",
        nargs=1,
        help="using sell: item id"
    )
    parser.add_argument(
        "-a",
        type=int,
        dest="quantity",
        nargs=1,
        help="using buy or sell: amount of items, using advance_date: amount of days from today"
    )
    parser.add_argument(
        "-p",
        type=float,
        dest="price",
        nargs=1,
        help="using buy or sell: price of item"
    )
    parser.add_argument(
        "-d",
        type=str,
        dest="date",
        nargs=1,
        help="using buy: expiration date of item, using change_date: desired system date, using report: desired report date (yyyy-mm-dd format)"
    )
    parser.add_argument(
        "-t",
        type=str,
        dest="second_date",
        nargs=1,
        help="using report: second date to get report over a period of time (yyyy-mm-dd format)"
    )
    parser.add_argument(
        "-r",
        type=str,
        dest="report",
        nargs=1,
        choices=REPORTS.keys(),
        help="using report: type of report(sales/loss/inventory/profit)"
    )

    parsed_args = parser.parse_args()
    main(parsed_args)
