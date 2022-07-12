from datetime import date, datetime, timedelta
from pathlib import Path
import os


class DateTools():

    def __init__(self):
        self.app_data_path = Path(__file__).absolute().parent / "app-data"

    def get_todays_date(self):
        return date.today()

    def get_system_date(self):
        date_file = open(f"{self.app_data_path}/date.txt", "r")
        system_date = ""
        for line in date_file:
            system_date = line
        date_file.close()
        return system_date

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

    def check_if_set_to_today(self):
        date_file = open(f"{self.app_data_path}/date.txt", "r")
        format = "%Y-%m-%d"
        saved_date = datetime.strptime(date_file.read(), format)
        today_date = datetime.strptime(str(self.get_todays_date()), format)
        if saved_date < today_date:
            change_date = input(
                "\n----- The SuperPy system date is currently behind today's date, do you wish to update to today's date? (yes/no)\n")
            if change_date == "yes":
                self.set_todays_date(self.get_todays_date())
            else:
                print(f"\n**WARNING** System date not updated! **WARNING**\n")
        date_file.close()

    def set_todays_date(self, date):
        correct_format = self.check_date_validity(date)
        if correct_format:
            date_file = open(f"{self.app_data_path}/date.txt", "w")
            date_file.write(str(date))
            date_file.close()
            print(f"\n----- System date updated succesfully -----\n")
        else:
            pass

    def advance_todays_date(self, amount_to_advance):
        newdate = self.get_todays_date() + timedelta(days=int(amount_to_advance))
        correct_format = self.check_date_validity(newdate)
        if correct_format:
            date_file = open(f"{self.app_data_path}/date.txt", "w")
            date_file.write(str(newdate))
            date_file.close()
            print(f"\n----- System date updated succesfully -----\n")
        else:
            pass

    def check_date_file(self):
        if not os.path.exists(f"{self.app_data_path}/date.txt"):
            self.set_todays_date(self.get_todays_date())
        else:
            date_file = open(f"{self.app_data_path}/date.txt", "r")
            format = "%Y-%m-%d"
            try:
                saved_date = datetime.strptime(date_file.read(), format)
            except ValueError:
                print(
                    "**ERROR** The date stored in the date file was corrupted and has been reset to today's date **ERROR**")
                self.set_todays_date(self.get_todays_date())
            today_date = datetime.strptime(str(self.get_todays_date()), format)

    def check_if_expired(self, exp_date):
        date_file = open(f"{self.app_data_path}/date.txt", "r")
        format = "%Y-%m-%d"
        exp_date = datetime.strptime(exp_date, format)
        saved_date = datetime.strptime(date_file.read(), format)
        if exp_date <= saved_date:
            return True
        else:
            return False
