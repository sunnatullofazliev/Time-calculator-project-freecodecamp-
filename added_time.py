
"""
Created on Sun Dec 29 22:44:20 2024

@author: sunnatullofazliev
"""

def add_time(start, duration, week = None):
    time, ending = start.split()
    hours_start, minutes_start = time.split(':')
    hours_dur, minutes_dur = duration.split(':')
    dayslater = ['', ' (next day)'] #initial list for same day and next day strings
    time_am = ['AM', 'PM']
    time_pm = ['PM', 'AM']
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def new_minutes(minutes): #The function takes the calculated new minutes (int) as the argument and produces ready string minutes in correct format (e.g., 01, 02 etc) and will be called later for final answer.
        if minutes < 10:
            return '0' + str(minutes)
        else:
            return str(minutes)

    def day_time(ending, daytime): #The function takes the starting time ending (am or pm) and the resulting daytime (one daytime is 12 h ) as the argument and produces final time ending in AM or PM
        if ending == 'AM':
            return time_am[daytime%2]
        else:
            return time_pm[daytime%2]
    
    def days_later(start_ending, day, daytime): #The function takes the starting time ending (am or pm), resulting day (24 h) and the resulting daytime as the argument and produces final day difference i.e., (next day,n days later)
        if ending == 'AM':
            if day <= 1:
                return dayslater[day]
            else:
                return ' (' + str(day) + ' days later)'
        elif ending == 'PM': #If starting time is in PM, it's a bit tricky with day difference, so initial AM and PM matters.
            if daytime <= 1:
                return dayslater[daytime]
            else:
                return ' (' + str((daytime + 1) // 2) + ' days later)' #In principle, one can store dayslater in a list and use it as weekdays (see below)), but it would be really large list if one wants to calculate large added time (which result in many days..)
        
    def weekday_call(ending, weekday, daytime, day):  
        if ending == 'AM':
            weekday += day
        elif ending == 'PM':
            weekday += ((daytime + 1) // 2) #again daytime for starting PM
        if weekday < 7:
            return weekdays[weekday]
        else:
            return weekdays[((weekday-7 ) % 7 )]
    
    minutes = (int(minutes_start) + int(minutes_dur)) % 60 #Calculating new minutes (int) in time, not total minutes!
    hours_new = int(hours_start) + int(hours_dur) + ((int(minutes_start) + int(minutes_dur)) // 60) #Calculating total hours
    daytime = hours_new // 12
    day = hours_new // 24
    if hours_new == 12 and minutes == 0:
        new_time = '12:00 PM, '  +' (' + days_later[day] + ')' #12:00 PM rule (without weekday)
    elif hours_new % 12 == 0: #12 am or pm rule (without weekday)
        new_time = '12:' + new_minutes(minutes) + ' ' + day_time(ending, daytime)  + days_later(ending, day, daytime)
    else: #All other times ((without weekday))            
        new_time = str(hours_new % 12) + ':' + new_minutes(minutes) + ' ' + day_time(ending, daytime)  + days_later(ending, day, daytime)
    
    if week is not None: #When weekday is given
        minutes = (int(minutes_start) + int(minutes_dur)) % 60
        hours_new = int(hours_start) + int(hours_dur) + ((int(minutes_start) + int(minutes_dur)) // 60)
        daytime = hours_new // 12
        day = hours_new // 24
        weekday = [x.lower() for x in weekdays].index(week.lower()) #Calculating starting weekday as int. Note 0 is monday, 6 - sunday
        if hours_new == 12 and minutes == 0:
            new_time = '12:00 PM, ' + weekday_call(weekday) +' (' + days_later[day] + ')'
        elif hours_new % 12 == 0:
            new_time = '12:' + new_minutes(minutes) + ' ' + day_time(ending, daytime) + ', ' + weekday_call(ending, weekday, daytime, day) + days_later(ending, day, daytime)
        else:            
            new_time = str(hours_new % 12) + ':' + new_minutes(minutes) + ' ' + day_time(ending, daytime) + ', ' + weekday_call(ending, weekday, daytime, day) + days_later(ending, day, daytime)
    return new_time

