#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.last_transaction = 0
    self.items = []

  def add_item(self, title, price, quantity = 1):
    self.last_transaction = price * quantity
    self.total += self.last_transaction
    for _ in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    if (self.discount > 0):
      # In the next line, we don't really need to convert the discount to a float
      # because when doing division in Python, the result is automatically a float - 
      # we've included it to make what's happening more explicit
      discount_as_percent = (100 - float(self.discount)) / 100
      # In the following line, however, we **do** need to explicitly convert the total
      # to an integer if that's what we want our method to return
      self.total = int(self.total * discount_as_percent)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print('There is no discount to apply.')

  def void_last_transaction(self):
    self.total -= self.last_transaction

