#thinkpython chapter 16: time

import copy
from datetime import date, timedelta

class Time(object):
	""" represents time of day

	attributes: hour, minute, second"""

#16.1 print time

def print_time(time):
	"""prints Time from time object in format hh:mm:ss"""

	print('%.2d:%.2d:%.2d' % (time.hours, time.minutes, time.seconds))

#16.2 is_after

def is_after(time1, time2):
	"""Takes two time objects, returns true if time1 follows time2 
	chronologically, False otherwise"""

	t1 = (time1.hours, time1.minutes, time1.seconds)

	t2 = (time2.hours, time2.minutes, time2.seconds)
	
	return t1 > t2

#16.3

def increment_modifier(time, seconds):
	"""object time, is incremented by the number of secondes (int).
	not pure"""

	minutes = seconds / 60
	hours = minutes / 60
	
	minutes_add = minutes % 60
	seconds_add = seconds % 60

	time.seconds += seconds_add
	time.minutes += minutes_add
	time.hours += hours

#16.4

def increment_pure(time, seconds):
	"""object time, is incremented by the number of secondes (int).
	is pure"""

	minutes = seconds / 60
	hours = minutes / 60
	
	minutes_add = minutes % 60
	seconds_add = seconds % 60
	
	time_copy = copy.copy(time)	

	time_copy.seconds += seconds_add
	time_copy.minutes += minutes_add
	time_copy.hours += hours
	
	return time_copy

#16.5

def time_to_int(time):
	minutes = time.hours * 60 + time.minutes
	seconds = minutes * 60 + time.seconds
	return seconds

def int_to_time(seconds):
	time = Time()
	minutes, time.seconds = divmod(seconds, 60)
	time.hours, time.minutes = divmod(minutes, 60)
	return time

def increment3(time, seconds):
	"""increment using int_to_time and time_to_int"""

	time_copy = copy.copy(time)
	increment_time = int_to_time(seconds)
	
	time_copy.hours += increment_time.hours
	time_copy.minutes += increment_time.minutes
	time_copy.seconds += increment_time.seconds

	return time_copy

#16.6

def mul_time(time, multiplier):
	"""given time object, multiplies it. returns object"""

	totalseconds = int((time_to_int(time)) * multiplier)

	return int_to_time(totalseconds)
	 
def average_time(totaltime, distance):
	"""totaltime is time object, divide it by int distance to get
	average time. returns time object"""

	return mul_time(totaltime, 1/float(distance))

#16.7

def date_day():
	"""returns current date and day of week, using datetime module"""

	dd = date.today()
	day = dd.weekday()

	if day == 0:
		day_str = 'Monday'
	elif day == 1:
		day_str = 'Tuesday'
	elif day == 2:
		day_str = 'Wednesday'
	elif day == 3:
		day_str = 'Thursday'
	elif day == 4:
		day_str = 'Friday'
	elif day == 5:
		day_str = 'Saturday'
	elif day == 6:
		day_str = 'Sunday'

	return (dd.isoformat(), day_str)


def time_to_birthday(birthday):
	"""Takes a birthday date objectas input and outputs days, hours, min, sec
	until next birthday"""

	today = date.today()
	thisyear_birthday =birthday.replace(year=today.year)
	if thisyear_birthday < today:
		next_birthday = thisyear_birthday.replace(year=today.year+1)
	else:
		next_birthday = thisyear_birthday
 
	time_until = next_birthday - today
	
	return time_until


def double_day(bday1, bday2):
	"""given two birthdays, computes the day where one is twice as
	old as the other"""


def n_day(bday1, bday2, n=2):
	"""Given two birthdays, computes day when one person is n times
	older than the other. Just brute force it. Too hard to 
	represent dates for multiplying right now."""

	#bday1 is older person, earlier date	

	if bday1 > bday2:
		bday1, bday2 = bday2, bday1
	
	day = bday2

	while True:
		diff1 = day - bday1
		diff2 = day - bday2
		if diff1 == n * diff2:
			return day
		day += timedelta(days=1)


if __name__ == '__main__':
	#time1 = Time()
	#time1.hours = 8
	#time1.minutes = 29
	#time1.seconds = 45
	
	#time2 = Time()
	#time2.hours = 1
	#time2.minutes = 1
	#time2.seconds = 2

	#increment_modifier(time1, 3670)
	#print_time(time1)
	#print_time(increment_pure(time1, 3600))
	#print_time(time1)
	#print_time(increment3(time1, 3600))
	#print_time(mul_time(time2,2))	
	#print_time(average_time(time2, 2))
	#print date_day()
	#birthday = date(1980, 8, 17)
	#print time_to_birthday(birthday)

	bday1 = date(1980, 10, 8)
	bday2 = date(1980, 12, 19)
	print n_day(bday1, bday2)
