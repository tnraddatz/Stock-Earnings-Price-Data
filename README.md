# Stock Earnings Price Data 

This project was used as a proof of concept for an investment thesis: "The daily closing stock prices leading up to a company's earnings report can predict if that earnings report will be negative or positive. 

# Program 

The program scrapes data from the SEC.gov website to collect past quarterly earnings dates of the five labeled companies NVR, MMM, MSFT, CAT, and NKE.  The quarterly earnings dates are written to a CSV file that is parsed into a list when called upon. To compare the *pre-earnings-report* stock prices to *post-earnings-report* stock prices, the program uses Yahoo Finance daily stock data in CSV form, which can be downloaded from Yahoo Finance's website and are located within the "Data" folder.  Once the monthly earnings dates and daily stock prices are collected for a specific company, the program reads these values into memory. The program compares the pre-earnings stock prices to a single post-earnings stock price, writing the +/- data to a graph, which is located in the "Graph" folder. 

# Output 

The alogrithm to generate the graph is straight forward: If we see the stock price *drop* in the 10 days leading up to the earnings report, we *expect* the day after the earnings report to *drop*. If we see the stock price *raise* in the 10 days leading up to the earnings report, we *expect* the day after the earnings report to *raise*. 

# Libraries 
- Selenium 
- Mathplotlib
