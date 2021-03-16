import StockDataRetriever
import Stock

def parse52WeekRange(stock):
    summaryTable = StockDataRetriever.get52WeekRange(stock)

    _52weekRangeValue = summaryTable[5].text
    startofRange = _52weekRangeValue.find('range')
    endofRange = _52weekRangeValue.find('range') + len('range')

    return _52weekRangeValue[:endofRange] + ': ' + _52weekRangeValue[endofRange:]



