# 1

def commission_decorator(func):
    def wrapper(balance, amount):
        commission = 1
        total = amount + commission

        if balance < total:
            return "Error! Insufficient balance."

        return func(balance, total)

    return wrapper


@commission_decorator
def transaction(balance, amount):
    balance -= amount
    return f"Transaction successful. Remaining balance: {balance} GEL"


print(transaction(100, 30))
print(transaction(20, 20))


print("\n-------------------------------\n")

# 2


class CheckMethods(type):
    def __new__(cls, name, bases, attrs):

        for key, value in attrs.items():
            if callable(value) and not key.startswith("_"):
                raise ValueError(f"Method '{key}' must start with '_'.")

        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=CheckMethods):
    number = 10      # Attribute (not checked)

    def _test(self):
        print("Test method")

    def _hello(self):
        print("Hello")


obj = MyClass()
obj._test()
obj._hello()


"""
class WrongClass(metaclass=CheckMethods):

    def test(self):
        print("This will cause an error")

    def _ok(self):
        print("Correct")
"""
