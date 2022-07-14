<h1>A short report on making this SuperPy app.</h1>

As a general learning point for myself I found that I once again didn't spend enough time during the planning fase. I did lay out more of a design plan now, as opposed to some of the earlier assignments(both front-end and back-end), but I found myself redoing quite a few data flows and argument "standards" as i was building the app. I feel like I could have saved a fair bit of overall time if I had spend a bit more time planning.

<h2>3 technical elements of note.</h2>

1. O.O.P.

I've really set out to make the app in a full o.o.p. design. This was the first time I did this and it brought me quite a few  valuable insights for the future. I feel like I have too much duplicate code throughout my app which, with slightly better planning, I could have reduced more. As I have no real world experience with o.o.p. I am curious to hear how well I did on this specific element in the feedback.

2. check_date_validity

Inside the DateTools class I have made a helper method which can check if the provided date is actually a valid date. I've used strptime with the provided date and desired format into a bool inside a try statement to either return a True value, or throw and exception with a clear error message.
~~~python
def check_date_validity(self, date):
        correct_format = True
        format = "%Y-%m-%d"
        try:
            correct_format = bool(datetime.strptime(str(date), format))
        except ValueError:
            correct_format = False
            print(
                f"\n**ERROR** The provided date was not valid or not in the correct format: {date} , should be YYYY-MM-DD **ERROR**\n")
            exit()
        return correct_format
~~~

3. sell

Inside the Sales class is the sell method. The sell method on its own doesm't hold anything very interesting, but I do think it shows how well the different Classes can create a very clear and readable piece of code. The sell method receives the sell_args from the main function in super.py. It creates a sell_dict based on these arguments. The datetools.get_system_date() method is used to add the system date to the sell_dict. We then send that dict into the inventory.check() method which return a new dict with either a True or False value in the "stock" key, depending if the item is in stock, plus the other needed values which it obtained from the inventory file. If the "stock" value returned False the program will print a ERROR message and the sale will be aborted. Otherwise the missing values are added to the sell_dict which is then send into the reporter.sale() method to print a small sale report, into the inventory.remove() method to remove said item(s) from the inventory, and into the self.add_to_sales() method to add the sale into the sales.csv file.
~~~python
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
~~~