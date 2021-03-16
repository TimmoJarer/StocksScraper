from bs4 import BeautifulSoup
import requests

def get52WeekRange(stock):
    summarySource = requests.get('https://uk.finance.yahoo.com/quote/{x}.L?p={x}.L'.format(x = stock)).text
    summaryPage = BeautifulSoup(summarySource, 'lxml')
    summaryTable = summaryPage.body.table.tbody.contents

    return summaryTable

def retrievePriceHistory(stock, suffix):
    historySource = requests.get('https://uk.finance.yahoo.com/quote/{x}.{y}/history?p={x}.{y}'.format(x = stock, y = suffix)).text
    historyPage = BeautifulSoup(historySource, 'lxml')
    historyTable = historyPage.body.table.tbody.contents

    return historyTable

def retrieveNDPs(stock, suffix):
    summarySource = requests.get('https://uk.finance.yahoo.com/quote/{x}.{y}?p={x}.{y}'.format(x = stock, y = suffix)).text
    summaryPage = BeautifulSoup(summarySource, 'lxml')
    NDPs = summaryPage.find('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
    NDPs = len(NDPs.split('.')[1])
    return NDPs







    

