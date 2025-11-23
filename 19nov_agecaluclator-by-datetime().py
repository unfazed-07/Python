from datetime import datetime
from dateutil.relativedelta import relativedelta

while (1):
    user_birthdate = input("Enter your Birthdate: (DDMMYYYY)")
    birthday = datetime.strptime(user_birthdate, "%d%m%Y")
    today=datetime.now()

    difference = relativedelta(today,birthday)
    print("Years:",difference.years," Months:",difference.months," Days:",difference.days)
