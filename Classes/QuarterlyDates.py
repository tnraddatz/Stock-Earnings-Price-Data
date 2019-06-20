from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os.path
from os import path
import csv

class QuarterlyDates: 
    
    def __init__(self, ticker_urls):
        self.ticker_urls = ticker_urls
        self.quarterly_dates = []

    def scrape_dates(self):
        self.driver = webdriver.Chrome()
        for ticker, url in self.ticker_urls.items():
            quarterly_reporting_dates = self.scrape_company_quarters(ticker, url)
            self.quarterly_dates.append(quarterly_reporting_dates)


    def scrape_company_quarters(self, ticker, url):
        qDates = [ticker]
        self.driver.get(url)
        while len(qDates) <= 80:
            table_id = self.driver.find_element_by_class_name('tableFile2')
            rows = table_id.find_elements_by_tag_name('tr') 
            for row in rows[1:-1]:      
                col = row.find_elements_by_tag_name('td')
                if col[0].text == "10-Q" or col[0].text == "10-K":
                    qDates.append(col[3].text)

            next_page_button = self.SEC_next_button('//*[@id="contentDiv"]/div[3]/form/table/tbody/tr/td[2]/input')
            next_page_button.click()

        return qDates


    def SEC_next_button(self, xpath):
        #The page will have one button on the first page "Next"
        #And two buttons on the second page "Back", "Next"
        #We need to make sure to click "Next"
        next_page = self.driver.find_elements_by_xpath(xpath)
        if len(next_page) > 1:
            next_page = next_page[1]
        else:
            next_page = next_page[0]
        return next_page 


    def writeCSV(self):
        with open("QuarterlyDates.csv",'w') as resultFile:
            wr = csv.writer(resultFile)
            wr.writerows(self.quarterly_dates)


    def closeDriver(self):
        self.driver.close()

    def readCSV(self):
        script_dir = os.path.dirname(__file__)  # Script directory
        full_path = os.path.join(script_dir, "../Data/QuarterlyDates.csv")
        print(full_path)
        data = []
        if path.exists(full_path):
            with open(full_path,'r') as f:
                reader = csv.reader(f)
                for i, line in enumerate(reader):
                    data.append(line)
        else: 
            raise Exception("Cannot find CSV folder, you may need to generate one using the '.scrape_dates' function")
        return data
            
