from QuarterlyDates import QuarterlyDates
from StockDates import StockDates
from SpreadGenerator import SpreadGenerator
from CreateGraph import CreateGraph

####### TICKER DATA #######
TICKER_URLS =  { 
                "NVR":"http://www.sec.gov/cgi-bin/browse-edgar?CIK=nvr&action=getcompany&owner=exclude",
                "MSFT":"http://www.sec.gov/cgi-bin/browse-edgar?CIK=MSFT&action=getcompany&owner=exclude",
                "CAT":"http://www.sec.gov/cgi-bin/browse-edgar?CIK=CAT&action=getcompany&owner=exclude",
                "MMM":"http://www.sec.gov/cgi-bin/browse-edgar?CIK=MMM&action=getcompany&owner=exclude",
                "NKE":"http://www.sec.gov/cgi-bin/browse-edgar?CIK=NKE&action=getcompany&owner=exclude"
              }
############################


def main():
  ######Quarterly Reporting Dates ##########
  quarterDates = QuarterlyDates(TICKER_URLS)
  #quarterDates.scrape_dates()
  #quarterDates.closeDriver()
  #quarterDates.writeCSV()
  ##########################################
  ########## Read From CSV File ############
  csv = quarterDates.readCSV()
  company = input('Choose a Company: (0) NVR | (1) MSFT | (2) CAT | (3) MMM | (4) NKE | ' )
  reportData = csv[int(company)] #CHANGE [x] TO CHANGE THE COMPANY
  ticker = reportData[0] 
  reportData = reportData[1:-1] #Need to flip dates (Least Recent -> Most Recent)
  reportData.reverse() #(Least Recent -> Most Recent)
  reportData.insert(0, ticker)
  ##########################################
  ########## DAILY STOCK DATES ##########
  stockDates = StockDates(ticker)
  stockData = stockDates.readCSV()
  #######################################
  ######## GENERATE THE SPREAD ##########
  spread = SpreadGenerator()
  final_hash = spread.generate(stockData, reportData, ticker)
  #######################################
  ############ GRAPH IT #################
  graph = CreateGraph(final_hash)
  graph.generate_scatter_plot()


#RUN THE PROGRAM# 
main()