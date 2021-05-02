"""Budget App
Create a Budget class that can instantiate objects based on different budget categories like food, clothing,
and entertainment. These objects should allow for
1.  Depositing funds to each of the categories
2.  Withdrawing funds from each category
3.  Computing category balances
4.  Transferring balance amounts between categories
"""


def validate_amount(amount):
    """Validate the amount"""
    try:
        int(amount)
    except ValueError:
        raise ValueError("Invalid amount")

    if amount <= 0:
        raise ValueError("Amount must be greater than 0")


class Budget:
    categories = ["entertainment", "food", "clothing"]
    balance = {}

    def __init__(self, category):
        if category not in self.categories:
            raise ValueError("Invalid category type")
        self.category = category

    def deposit(self, amount):
        """deposit in various categories

        Category types are food, clothing
        entertainment

        Args:
          self: (instance)
          amount: (int) The amount to be deposited

        returns:
          balance: (obj)
        """
        validate_amount(amount)

        if self.balance.get(self.category):
            self.balance[self.category] += amount
        else:
            self.balance[self.category] = amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw fund from category

        Args:
          self: (instance)
          amount: (int) The amount to be deposited

        returns:
          balance: (obj)
        """
        validate_amount(amount)

        if not self.balance.get(self.category):
            raise ValueError("No balance yet for this category - `{}`".format(self.category))

        if amount > self.balance.get(self.category):
            raise ValueError("Insufficient funds")

        self.balance[self.category] -= amount

    @classmethod
    def category_balances(cls):
        """Returns the total balances

        Args:
          cls: (class instance)

        returns:
          balances: (obj)
        """
        totalbalance = 0
        if cls.balance:
            totalbalance = sum(balance for category, balance in cls.balance.items())
        return {
            "totalbalance": totalbalance,
            "distinct balances": cls.balance
        }

    def transfer(self, amount, to):
        """Transfer amount between categories

        Args:
          self: (instance)
          amount: (int) The amount to be transferred
          to: (string) The recipient category

        returns:
          balance: (obj)
        """

        if not Budget.balance.get(self.category):
            raise ValueError("`{}` category has no balance yet".format(self.category))

        if self.balance[self.category] < amount:
            raise ValueError("Insufficient funds")

        self.balance[self.category] -= amount
        if self.balance.get(to):
            self.balance[to] += amount
        else:
            # no balance yet, therefore create a new balance
            self.balance[self.category] = amount
        return self.balance

"""
entertainment = Budget(category="entertainment")

entertainment.deposit(100)


food = Budget(category="food")
food.deposit(37)


clothing = Budget(category="clothing")
clothing.deposit(63)
print(food.category_balances())

clothing.withdraw(20)
print("Balance After withdrawal /n", Budget.category_balances())

clothing.transfer(30, "food")
print("/n After transfer")
print(Budget.category_balances())
"""
