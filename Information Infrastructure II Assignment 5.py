#importing modules
import urllib, csv, datetime, re

#function that returns string with stock data
def getStockData(company):
        baseurl = "http://quote.yahoo.com/d/quotes.csv?s={0}&f=sl1d1t1c1ohgvj1pp2owern&e=.csv"
        url = baseurl.format(company)
        web_page = urllib.urlopen(url)
        read = csv.reader(web_page)
        row = read.next()
        web_page.close()
        new_date = row[2].split("/")
        d = datetime.date(int(new_date[2]), int(new_date[0]), int(new_date[1]))
        print "The last trade for", row[0], "was $", round(float(row[1]), 2), "and the change was", row[4], "on", d.strftime("%b %d, %Y"), ". The open was $",
        try:
                print round(float(row[5]), 2),
        except ValueError:
                print "unknown",

        print "and the previous close was $",

        try:
                print round(float(row[6]), 2), "."
        except ValueError:
                print "unknown."

#main
#list of stocks
companies = ["GE", "WTW", "BAC", "PMCS", "VSS", "MS", "NFLX", "INTC", "TWTR", "AAPL"]

for company in companies:
	getStockData(company)

