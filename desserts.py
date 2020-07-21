"""Dessert classes."""


class AbstractBakedGoods:

    cache = {}

    @staticmethod
    def scale_recipe(ingredients, amount):

      result = []
      single_ingredient = []

      for item in ingredients:
        
        single_ingredient = list()

        ingredient_name = item[0]
        ingredient_qty = item[1]

        single_ingredient.append(ingredient_name)
        single_ingredient.append(ingredient_qty * amount)

        single_ingredient = tuple(single_ingredient)
        
        result.append(single_ingredient)

      return result

    @classmethod
    def get(cls, name):
      cache = cls.cache
      if name in cache:
        print(cache[name])
      else:
        cache.get(name, 0)
        print("Sorry, that cupcake doesn't exist")


    def __init__(self, name, price, qty=0):
      self.name = name
      self.price = price
      self.qty = qty
      self.cache[name] = self

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def add_stock(self, amount):
      self.amount = amount
      self.qty += amount

    def sell(self, amount):

      if self.qty == 0:
        print("Sorry, these cupcakes are sold out")

      self.qty -= amount 

      if self.qty < 0:
        self.qty = 0

class Cupcake(AbstractBakedGoods):

  def __init__(self, name, price, flavor, qty=0):
    super().__init__(name, price, qty=0)
    self.flavor = flavor


class Brownie(AbstractBakedGoods):

  def __init__(self, name, price, qty=0):
    super().__init__(name, price, qty=0)



#######################################################

# if __name__ == '__main__':
#     import doctest

#     result = doctest.testfile('doctests.py',
#                               report=False,
#                               optionflags=(
#                                   doctest.REPORT_ONLY_FIRST_FAILURE
#                               ))
#     doctest.master.summarize(1)
#     if result.failed == 0:
#         print('ALL TESTS PASSED')












