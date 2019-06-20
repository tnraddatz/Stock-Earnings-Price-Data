import os.path
from os import path
import csv

class StockDates: 

    def __init__(self, ticker):
        self.filename = ticker + ".csv"
    
    #Read from CSV and get the stock dates
    def readCSV(self):
        data = []
        if path.exists(self.filename):
            with open(self.filename,'r') as f:
                reader = csv.reader(f)
                for i, line in enumerate(reader):
                    data.append(line)
        return data