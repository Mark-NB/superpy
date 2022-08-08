from rich.console import Console
from rich.table import Table
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from date import DateTools


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

        save_to_pdf = input(
            "\n----- Do you want this report to also be saved to PDF? (yes/no) -----\n")
        if save_to_pdf == "yes":
            self.make_pdf_report(inventory)

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

        save_to_pdf = input(
            "\n----- Do you want this report to also be saved to PDF? (yes/no) -----\n")
        if save_to_pdf == "yes":
            self.make_pdf_report(loss)

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
        table = Table(title="Sales/margin Report")

        table.add_column("Sale id", style="orchid")
        table.add_column("Product", style="bright_yellow")
        table.add_column("Quantity", style="bright_cyan")
        table.add_column("Buy price", style="bright_red")
        table.add_column("Sale price", style="bright_green")
        table.add_column("Total revenue", style="green4")
        table.add_column("Total margin", style="deep_pink3")
        table.add_column("Sale date", style="orange3")

        save_to_pdf = input(
            "\n----- Do you want this report to also be saved to PDF? (yes/no) -----\n")
        if save_to_pdf == "yes":
            self.make_pdf_report(sales)

        for dic in sales:
            table.add_row(
                str(dic["id"]),
                str(dic["product"]),
                str(dic["quantity"]),
                str(dic["buy_price"]),
                str(dic["sell_price"]),
                str(dic["total_revenue"]),
                str(dic["total_margin"]),
                str(dic["sell_date"]),
            )

        console = Console()
        console.print(table)

    def profit_report(self, profit_dict):
        table = Table(title="Profits")

        table.add_column("Total revenue", style="green4")
        table.add_column("Total margin", style="deep_pink3")
        table.add_column("Total loss", style="hot_pink3")
        table.add_column("Total profit", style="sky_blue3")

        table.add_row(
            str(profit_dict["total_revenue"]),
            str(profit_dict["total_margin"]),
            str(profit_dict["total_loss"]),
            str(profit_dict["total_profit"]),
        )

        save_to_pdf = input(
            "\n----- Do you want this report to also be saved to PDF? (yes/no) -----\n")
        if save_to_pdf == "yes":
            profit_list = [profit_dict]
            self.make_pdf_report(profit_list)

        console = Console()
        console.print(table)

    def make_pdf_report(self, report_list):
        datetools = DateTools()
        systemdate = datetools.get_system_date()
        pdf_report = canvas.Canvas("superpy_report.pdf", pagesize=letter)
        pdf_report.setLineWidth(.3)
        pdf_report.setFont('Helvetica', 12)
        pdf_report.drawString(30, 750, 'SuperPy Report')
        pdf_report.drawString(460, 750, f"Report date: {systemdate}")
        pdf_report.setFont('Helvetica', 8)
        pdf_report.line(30, 700, 580, 700)
        line_decrement = 10
        line_increment_counter = 0
        width_increment = 85
        width_increment_counter = 0
        key_list = list(report_list[0].keys())
        for key in key_list:
            pdf_report.drawString(
                (30 + (width_increment * width_increment_counter)), (703 - (line_decrement * line_increment_counter)), str(key))
            width_increment_counter += 1
        line_increment_counter += 1
        width_increment_counter = 0
        for dic in report_list:
            value_list = list(dic.values())
            for value in value_list:
                pdf_report.drawString(
                    (30 + (width_increment * width_increment_counter)), (703 - (line_decrement * line_increment_counter)), str(value))
                width_increment_counter += 1
            line_increment_counter += 1
            width_increment_counter = 0
        pdf_report.save()
