#Day of the programmer | HackerRank


#given a year y. find the date of the 256th day of that year according to the official Russain Calendar during that year.
#february has 29 days in a leap year.
#leap year is a year divisible by four, according to the Julian calendar.

import datetime
def dayOfProgrammer(year):

	if year > 1918:
		if year % 4:
			d = '12'
		else:
			d = '13'
	elif year == 1918:
		return '26.09.1918'
	else:
		if year % 4 == 0:
			return '12.09'+'.'+str(year)
		else:
			return '13.09'+'.'+str(year)
	y = str(year)

	date_check = d+'.'+'09'+'.'+y
	dt = datetime.datetime.strptime(date_check, '%d.%m.%Y')
	result = ('{:%d.%m.%Y}'.format(dt))
	return result

print(dayOfProgrammer(1800))


def dayOfProgrammer(year):
    if year < 1700 or year > 2700:
        return 
           
    elif year==1918:
        return '26.09.1918'
    
    elif year < 1918:
        if year%4==0:
            return '12.09.'+str(year)
                   
        else:
            return '13.09.'+str(year)
                
    elif year > 1918:
        if year%400==0 or year%4==0 and year%100!=0:
            return '12.09.'+str(year) 
    
        else:
            return '13.09.'+str(year)