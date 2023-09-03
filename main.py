from datetime import date, datetime, timedelta



def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    days_name = {
                0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday",
                }

    if len(users) == 0:
        return {}
    today = date.today()
    #today = datetime(day=26, month=12, year=2023)
    month_today = int(today.strftime('%m'))
    day_today = int(today.strftime('%d'))
    year_today = int(today.strftime('%Y'))
    today_date = datetime(day=day_today, month=month_today,year=year_today)
    today_date_sec = today_date.timestamp()
    

    end_of_period = today + timedelta(weeks=1)
    month_end_of_period = int(end_of_period.strftime('%m'))
    day_end_of_period = int(end_of_period.strftime('%d'))
    year_end_of_period = int(end_of_period.strftime('%Y'))
    end_of_period_date = datetime(day=day_end_of_period, month=month_end_of_period,year=year_end_of_period)
    end_of_period_seconds = end_of_period_date.timestamp()
    
  
    result = {}
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    birthdays_next_week = {day: [] for day in days_of_week}
    def _append_birthdays_next_week(day_of_week, user):
            day_name = days_name.get(day_of_week)
            if day_name == "Saturday" or day_name == "Sunday":
                day_name = 'Monday'
            birthdays_next_week[day_name].append(user['name'])
    
    for user in users:
        birthday = user['birthday']
        day_birth = int(birthday.strftime('%d'))
        month_birth = int(birthday.strftime('%m'))
        birthday_this_year = datetime(day=day_birth, month=month_birth, year=year_today)
        birthday_seconds = birthday_this_year.timestamp()
        

        if year_end_of_period > year_today:
            print("year_end_of_period > year_today:")
            if month_birth == 12 and day_today <= day_birth:
                print("month_birth == 12")
                day_of_week = datetime(day=day_birth, month=month_birth, year=year_today).weekday()      
                _append_birthdays_next_week(day_of_week, user)
            elif month_birth == 1 and day_birth <= day_end_of_period:
                print("month_birth == 1")
                day_of_week = datetime(day=day_birth, month=month_birth, year=year_end_of_period).weekday()
                _append_birthdays_next_week(day_of_week, user)
            else:
                continue
                print("month_birth: " + str(month_birth))
            
           

        elif today_date_sec <= birthday_seconds and birthday_seconds <= end_of_period_seconds:
            
            day_of_week = datetime(day=day_birth, month=month_birth, year=year_today).weekday()

            _append_birthdays_next_week(day_of_week, user)
                

    users = {day: names for day, names in birthdays_next_week.items() if names}

        
    return users


        
if __name__ == "__main__":
    users = [
        {"name": "Some", "birthday": datetime(1976, 9, 9).date()},
        {"name": "Body", "birthday": datetime(1976, 9, 10).date()},
        {"name": "Fuck's", "birthday": datetime(1976, 9, 5).date()},
        {"name": " UP  ", "birthday": datetime(1976, 8, 7).date()},
        {"name": " Second  ", "birthday": datetime(1976, 12, 7).date()},
        {"name": " Third  ", "birthday": datetime(1976, 12, 24).date()},
        {"name": " Jhon  ", "birthday": datetime(1976, 12, 31).date()},
        {"name": " Homer  ", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
        
        
