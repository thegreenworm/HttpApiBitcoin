import requests
from datetime import date, timedelta

class API:

    def getDateRange(self,start,end):
        startString = start.split("-")
        endString = end.split("-")
        startDate = date(int(startString[0].replace("'","")),int(startString[1].replace("'","")),int(startString[2].replace("'","")))
        endDate = date(int(endString[0].replace("'","")),int(endString[1].replace("'","")),int(endString[2].replace("'","")))
        delta = endDate - startDate
        dateRange = int(delta.days + 1)
    
        if dateRange > 45:
            print("\nCan not search for more than 45 dates\n")
            return
        else:
            newStart = startDate - timedelta(days=1)
            url = f"https://api.coindesk.com/v1/bpi/historical/close.json?start={newStart}&end={end}"
            data = requests.get(url).json()
            dates = data["bpi"]
            firstDay = dates[start]
            lastDay = dates[end]
            totalIncrease = int(lastDay) - int(firstDay)
            totalPercent = totalIncrease/ int(lastDay)
            floatTotalPercent = "%.2f" % totalPercent
            totalClosingPrice = 0
            priceList = []
            for i in range(delta.days +1):
                day = startDate + timedelta(days=i)
                totalClosingPrice += int(dates[str(day)]) 
                priceList.append(float(dates[str(day)]))
                increase = int(dates[str(day)]) - int(dates[str(day - timedelta(days=1))])
                dailyPercent = (increase/dates[str(day - timedelta(days=1))])
                percent = "%.2f" % dailyPercent
                print(f"""
                Date :{day} 
                Closing price: ${dates[str(day)]} 
                Daily percent: {percent}%
                """)
            totalClosingAverage = totalClosingPrice / dateRange
            shortClosingAverage = "%.2f" % totalClosingAverage
            slope = None
            if totalPercent > 0:
                slope = "Increase"
            elif totalPercent < 0:
                slope = "Decrease"
            else:
                slope = "No Change"
            print(f"------------------------------------------------------")
            print(f"""
            Total percent during period: {floatTotalPercent}%
            Average closing price: ${shortClosingAverage}
            Max closing price: ${max(priceList)}
            Min closing price: ${min(priceList)}
            Trend Slope: {slope}
            Powered by CoinDesk:  https://www.coindesk.com/price/bitcoin
            """)
            
                

        # for i in range(delta.days + 1):
        #     day = startDate + timedelta(days=i)
        #     print(day)


        #
        