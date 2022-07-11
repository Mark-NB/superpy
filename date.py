from datetime import date, datetime
from pathlib import Path
import os


class DateTools():

    def __init__(self):
        self.app_data_path = Path(__file__).absolute().parent / "app-data"

    def get_todays_date(self):
        return date.today()

    def check_date_validity(self, date):
        correct_format = True
        format = "%Y-%m-%d"
        try:
            correct_format = bool(datetime.strptime(str(date), format))
        except ValueError:
            correct_format = False
            print(
                f"The provided date was not valid or not in the correct format: {date} , should be YYYY-MM-DD")
        return correct_format

    def set_todays_date(self, date):
        correct_format = self.check_date_validity(date)
        if correct_format:
            date_file = open(f"{self.app_data_path}/date.txt", "w")
            date_file.write(str(date))
            date_file.close()
        else:
            pass

    def check_date_file(self):
        if not os.path.exists(f"{self.app_data_path}/date.txt"):
            self.set_todays_date(self.get_todays_date())
        else:
            date_file = open(f"{self.app_data_path}/date.txt", "r")
            format = "%Y-%m-%d"
            saved_date = datetime.strptime(date_file.read(), format)
            today_date = datetime.strptime(str(self.get_todays_date()), format)
            if saved_date < today_date:
                self.set_todays_date(self.get_todays_date())
            date_file.close()

    def check_if_expired(self, exp_date):
        date_file = open(f"{self.app_data_path}/date.txt", "r")
        format = "%Y-%m-%d"
        exp_date = datetime.strptime(exp_date, format)
        saved_date = datetime.strptime(date_file.read(), format)
        if exp_date <= saved_date:
            return True
        else:
            return False
