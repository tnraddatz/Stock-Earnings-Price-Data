from datetime import datetime

class SpreadGenerator: 
    #['Date',       'Open',      'High',      'Low',       'Close',     'Adj Close', 'Volume']
    #['1997-06-19', '15.687500', '16.000000', '15.500000', '16.000000', '16.000000', '13100']

    #stockData = #['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    #reportData = ['NVR', oldest ... most recent]

    #StockData = daily values 
    #ReportData = Quarterly Reporting Dates (Earnings)
    def generate(self, stockData, reportData, ticker): 
        final_hash = {ticker : []}

        sd_i = 2 
        rd_i = 1 
        prev_date = stockData[1][0] #[1][0] = dates
        prev_date = datetime.strptime(prev_date, '%Y-%m-%d')
        queue = [float(stockData[1][4])]
        while sd_i + 1 < len(stockData) and rd_i < len(reportData):
            #GET DATES AND CONVERSIONS
            cur_stockdate = stockData[sd_i][0]
            report_date = reportData[rd_i]
            cur_stockdate = datetime.strptime(cur_stockdate, '%Y-%m-%d')
            report_date = datetime.strptime(report_date, '%m-%d-%Y')
            #Add to queue
            #print("cur_stockdate: " + str(cur_stockdate) + " report_date: " + str(report_date))
            if len(queue) < 11:
                queue.insert(0, float(stockData[sd_i][4])) #closing price 
            else: 
                queue.pop(-1)
                queue.insert(0, float(stockData[sd_i][4]))

            if cur_stockdate == report_date:
                #We found the date! 
                #we will append information to the hash in the form 
                #[report_date, price_after, [queue of previous 10 days prices...]]
                final_hash[ticker].append([report_date, float(stockData[sd_i + 1][4]), queue])
                queue = []
                rd_i += 1
            elif prev_date < report_date and cur_stockdate > report_date:
                queue.pop(0)
                final_hash[ticker].append([report_date, float(stockData[sd_i][4]), queue])
                rd_i += 1
                queue = []
            
            prev_date = cur_stockdate
            sd_i += 1

        return final_hash