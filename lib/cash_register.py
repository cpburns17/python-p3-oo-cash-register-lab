#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount='') -> None:
    self.total = 0
    self.items = []
    self.discount = discount



