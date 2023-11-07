import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stockABC, bid_priceABC, ask_priceABC, priceABC = getDataPoint(quotes[0])
    assert stockABC == "ABC", "stock name should be the same as that passed in"
    assert bid_priceABC == 120.48, "bid price should be the same as that passed in"
    assert ask_priceABC == 121.2, "ask price should be the same as that passed in"
    assert priceABC == (120.48 + 121.2) / 2, "final price should be the mean of the bid and ask prices"

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    assert getRatio(1, 0) == None, "getRatio should return nothing if b is 0"
    assert getRatio(1, 1) == 1, "getRatio should return 1 if  a == 1 and b == 1"
    assert getRatio(1, -1) == None, "getRatio should return nothing if b < 0"
    assert getRatio(-1, 1) == None, "getRatio should return nothing if a < 0"
    assert getRatio(501, 2) == 250.5, "getRatio should return a float when a / b is not an integer"



if __name__ == '__main__':
    unittest.main()
