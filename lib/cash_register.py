#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount=0) -> None:
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_trans = []

    def add_item (self, item, price, quantity = 1):
        if type(item) == str and (type(price) == float or type(price) == int) and type(quantity) == int:
            self.total += price * quantity
            for _item in range(quantity):
              self.items.append(item)
            self.previous_trans.append({'item': item, 'price':price, 'quantity': quantity })
        else:
            print("did not add")
      
    def apply_discount(self):
        if self.discount:
            self.total = int(self.total - (self.total * self.discount /100))
            print(f'After the discount, the total comes to ${self.total}.')
        else:
            print('There is no discount to apply.')

    def void_last_transaction(self):
        pass
        




# cash_register_with_discount = CashRegister(20)
# cash_register_with_discount.add_item("macbook air", 1000)
# cash_register_with_discount.apply_discount()   
# print(cash_register_with_discount.total)