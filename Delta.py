import datetime

specific_date = datetime.datetime(1998, 10, 1)  # Change this to your desired date
today = datetime.datetime.now()

difference = today - specific_date
print(f"Difference between today and {specific_date.date()}: {difference.days} days")
