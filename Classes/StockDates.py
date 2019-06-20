import os.path
from os import path
import csv

class StockDates: 

    def __init__(self, ticker):
        self.filename = '../Data/' + ticker + ".csv"
    
    #Read from CSV and get the stock dates
    def readCSV(self):
        script_dir = os.path.dirname(__file__)  # Script directory
        full_path = os.path.join(script_dir, self.filename)
        data = []
        if path.exists(full_path):
            with open(full_path,'r') as f:
                reader = csv.reader(f)
                for i, line in enumerate(reader):
                    data.append(line)
        return data