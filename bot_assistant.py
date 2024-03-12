from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    start_next_week = today + timedelta(days=-today.weekday(), weeks=1)
    end_next_week = start_next_week + timedelta(days=7)

    birthdays = defaultdict(list)
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if start_next_week <= birthday_this_year < end_next_week:
            weekday = birthday_this_year.weekday()
            if weekday >= 5:  # If it's Saturday or Sunday
                weekday = 0  # Move to Monday
            weekday_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][weekday]
            birthdays[weekday_name].append(name)
    
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        if birthdays[day]:
            print(f"{day}: {', '.join(birthdays[day])}")

# Usage example
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    
]

get_birthdays_per_week(users)

