import unittest

from main import getNextProbableWords


class TestMethod(unittest.TestCase):

  def test_simple(self):
    self.assertEqual(True, True)

  def test_method(self):
    classDefinitions = [{
      "Order": {
        "orderId": "String",
        "version": "Long",
        "orderType": "OrderType",
        "orderSide": "OrderSide",
        "status": "Status",
        "allocations": "List<Allocation>"
      }
    }, {
      "OrderType": ["MarketOrderType", "LimitOrderType"]
    }, {
      "MarketOrderType": ""
    }, {
      "LimitOrderType": {
        "price": "Double"
      }
    }, {
      "OrderSide": ["Buy", "Sell"]
    }, {
      "Status": [
        "New", "Verifying", "Pending", "Working", "PartiallyFilled", "Filled",
        "Cancelled"
      ]
    }, {
      "Allocation": ["LongAllocation", "EmptyAllocation"]
    }, {
      "LongAllocation": {
        "clientName": "String"
      }
    }, {
      "EmptyAllocation": ""
    }]

    statements = [
      "Order.", "Order.order", "Order.allocations.", "Status.P",
      "MarketOrderType."
    ]

    expectedOutput = {
      "Order.": ["allocations", "orderId", "orderSide", "orderType", "status"],
      "Order.order": ["orderId", "orderSide", "orderType"],
      "Order.allocations.": [""],
      "Status.P": ["PartiallyFilled", "Pending"],
      "MarketOrderType.": [""]
    }

    self.assertDictEqual(
      getNextProbableWords(classes=classDefinitions, statements=statements),
      expectedOutput)


if __name__ == '__main__':
  unittest.main()
  # print("Running Test...")
  # actual = getNextProbableWords(classes=classDefinitions, statements=statements)
  # print(actual)
  # print("Test completed.")
