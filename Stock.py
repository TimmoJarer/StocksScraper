from bs4 import BeautifulSoup
import requests
import StockDataRetriever

class Stock:

    def __init__(self, name, title, suffix): 
        self.name = name
        self.title = title
        self.NDPs = StockDataRetriever.retrieveNDPs(name, suffix)
        self.historyTable = StockDataRetriever.retrievePriceHistory(name, suffix)
        self.openPriceList = []
        self.closePriceList = []
        self.highPriceList = []
        self.lowPriceList = []
        self.standardizedStartPoint = 9

        self.initializeStockData()
        


    def initializeStockData(self):
        print(self.name + " - " + self.title)
        print('-' * len(self.name + " - " + self.title))
        for i in range(0,len(self.historyTable)):
                price = self.historyTable[i].text
                dateBlock = price[0:11]
                priceBlock = price[11:]

                firstBlockLength = len(price[11:].split('.')[0]) + (self.NDPs + 1)
                secondBlockLength = len(price[11 + firstBlockLength:].split('.')[0]) + (self.NDPs + 1)
                thirdBlockLength = len(price[11 + firstBlockLength + secondBlockLength:].split('.')[0]) + (self.NDPs + 1)
                fourthBlockLength = len(price[11 + firstBlockLength + secondBlockLength + thirdBlockLength:].split('.')[0]) + (self.NDPs + 1)
                fifthBlockLength = len(price[11 + firstBlockLength + secondBlockLength + thirdBlockLength + 
                fourthBlockLength:].split('.')[0]) + (self.NDPs + 1)
                openPrice = priceBlock[:firstBlockLength]
                highPrice = price[11 + firstBlockLength: 11 + firstBlockLength + secondBlockLength]
                lowPrice = price[11 + firstBlockLength + secondBlockLength: 11 + firstBlockLength + secondBlockLength + thirdBlockLength]
                closePrice = price[11 + firstBlockLength + secondBlockLength + thirdBlockLength:
                11 + firstBlockLength + secondBlockLength + thirdBlockLength + fourthBlockLength]
                volume = price[11 + firstBlockLength + secondBlockLength + thirdBlockLength + fourthBlockLength + fifthBlockLength:]
                

                if (closePrice.find('.')) and (highPrice.find('.')):
                    self.openPriceList.append(openPrice)
                    self.closePriceList.append(closePrice)
                    self.highPriceList.append(highPrice)
                    self.lowPriceList.append(lowPrice)
                
                print('Date: ' + dateBlock + '| Open: ' + openPrice + '| High: ' + highPrice + '| Low: ' + lowPrice + '| Close: ' + closePrice
                + '| Volume: ' + volume)
        
        self.openPriceList = self.openPriceList[self.standardizedStartPoint:]
        self.closePriceList = self.closePriceList[self.standardizedStartPoint:]
        self.highPriceList = self.closePriceList[self.standardizedStartPoint:]
        self.lowPriceList = self.lowPriceList[self.standardizedStartPoint:]

        for i in range(0, len(self.openPriceList)):
            self.openPriceList[i] = float(self.openPriceList[i].replace(',', ''))

        

        print('Number of days on record: ' + str(len(self.openPriceList)))
        print('-' * len('Number of days on record: ' + str(len(self.openPriceList))))
               
 


