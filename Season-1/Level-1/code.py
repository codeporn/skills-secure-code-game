'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ORDER_VALUE = 100000
MIN_ORDER_VALUE = 0
MIN_QUANTITY = 0
MAX_QUANTITY = 100

def validorder(order: Order):

    payments = Decimal(0)
    orderValue = Decimal(0)

    for item in order.items:

        if item.type == 'payment':
            if -MAX_ORDER_VALUE <= item.amount <= MAX_ORDER_VALUE:
                payments += Decimal(str(item.amount))
        elif item.type == 'product':
            if type(item.quantity) is int and MIN_QUANTITY < item.quantity <= MAX_QUANTITY and MIN_ORDER_VALUE < item.amount <= MAX_ORDER_VALUE:
                orderValue += Decimal(str(item.amount)) * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    if abs(payments) > MAX_ORDER_VALUE or orderValue > MAX_ORDER_VALUE:
        return "Total amount payable for an order exceeded"

    if payments != orderValue:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payments - orderValue)
    else:
        return "Order ID: %s - Full payment received!" % order.id