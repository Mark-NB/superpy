from rich.console import Console
from rich.table import Table


class Reporter:
    def __init__(self):
        pass

    def inventory_report(self, inventory):
        table = Table(title="Current Inventory")

        table.add_column("Inv. id", style="orchid")
        table.add_column("Product", style="bright_yellow")
        table.add_column("Quantity", style="bright_cyan")
        table.add_column("Buy price", style="bright_red")
        table.add_column("Expiration date", style="bright_blue")
        table.add_column("Purchase date", style="orange3")

        for dic in inventory:
            table.add_row(
                str(dic["id"]),
                str(dic["product"]),
                str(dic["quantity"]),
                str(dic["buy_price"]),
                str(dic["exp_date"]),
                str(dic["buy_date"]),
            )

        console = Console()
        console.print(table)

    def buy_report(self, buy_dict):
        table = Table(title="Product bought")

        table.add_column("Product", style="bright_yellow")
        table.add_column("Quantity", style="bright_cyan")
        table.add_column("Buy price", style="bright_red")
        table.add_column("Expiration date", style="bright_blue")

        table.add_row(
            str(buy_dict["product"]),
            str(buy_dict["quantity"]),
            str(buy_dict["buy_price"]),
            str(buy_dict["exp_date"]),
        )

        console = Console()
        console.print(table)

    def loss_report(self, loss_list):
        table = Table(title="Products discarded")

        table.add_column("Loss id", style="orchid")
        table.add_column("Product", style="bright_yellow")
        table.add_column("Quantity", style="bright_cyan")
        table.add_column("Buy price", style="bright_red")
        table.add_column("Total loss", style="hot_pink3")
        table.add_column("Loss date", style="orange3")
        for dic in loss_list:
            table.add_row(
                str(dic["id"]),
                str(dic["product"]),
                str(dic["quantity"]),
                str(dic["buy_price"]),
                str(dic["total_loss"]),
                str(dic["loss_date"]),
            )

        console = Console()
        console.print(table)

    def sale_report(self, sale_dict):
        table = Table(title="Product sold")

        table.add_column("Product", style="bright_yellow")
        table.add_column("Quantity", style="bright_cyan")
        table.add_column("Sale price", style="bright_green")
        table.add_column("Expiration Date", style="bright_blue")
        table.add_column("Sale date", style="orange3")
        table.add_column("Total price", style="deep_pink3")

        table.add_row(
            str(sale_dict["product"]),
            str(sale_dict["quantity"]),
            str(sale_dict["sell_price"]),
            str(sale_dict["exp_date"]),
            str(sale_dict["sell_date"]),
            str(sale_dict["total_price"]),
        )

        console = Console()
        console.print(table)

    def losses_report(self, loss):
        table = Table(title="Loss Report")

        table.add_column("Loss id", style="orchid")
        table.add_column("Product", style="bright_yellow")
        table.add_column("Quantity", style="bright_cyan")
        table.add_column("Buy price", style="bright_red")
        table.add_column("Total loss", style="hot_pink3")
        table.add_column("Loss date", style="orange3")

        for dic in loss:
            table.add_row(
                str(dic["id"]),
                str(dic["product"]),
                str(dic["quantity"]),
                str(dic["buy_price"]),
                str(dic["total_loss"]),
                str(dic["loss_date"]),
            )

        console = Console()
        console.print(table)

    def sales_report(self, sales):
        table = Table(title="Sales/profit Report")

        table.add_column("Sale id", style="orchid")
        table.add_column("Product", style="bright_yellow")
        table.add_column("Quantity", style="bright_cyan")
        table.add_column("Buy price", style="bright_red")
        table.add_column("Sale price", style="bright_green")
        table.add_column("Total profit", style="deep_pink3")
        table.add_column("Sale date", style="orange3")

        for dic in sales:
            table.add_row(
                str(dic["id"]),
                str(dic["product"]),
                str(dic["quantity"]),
                str(dic["buy_price"]),
                str(dic["sell_price"]),
                str(dic["total_profit"]),
                str(dic["sell_date"]),
            )

        console = Console()
        console.print(table)
