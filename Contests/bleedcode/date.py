from datetime import datetime, timedelta

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

for _ in range(int(input())):
	date1, date2 = [str(x) for x in input().strip().split()]
	d1,m1,y1 = date1.split('/')
	d2,m2,y2 = date2.split('/')
	days = days_between(y1+'-'+m1+'-'+d1, y2+'-'+m2+'-'+d2)
	gap = timedelta(days=days-1)
	ans = datetime.strptime("0001-01-01", "%Y-%m-%d") + gap
	
	month = str(ans.month-1)
	mpadding = "0"*(2-len(month))
	month=mpadding+month

	year = str(ans.year-1)
	ypadding = "0"*(4-len(year))
	year=ypadding+year

	print("{0}/{1}/{2:4}".format(ans.day,month,year))