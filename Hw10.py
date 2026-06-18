# 1

from functools import reduce
my_list = [(1, 3), (4, 2), (2, 5)]

sorted_list = sorted(my_list, key=lambda x: x[1])

print(sorted_list)


# 2

def divide_numbers():
    try:
        num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

        result = num1 / num2
        print("შედეგი:", result)

    except ValueError:
        print("გთხოვთ შეიყვანოთ მხოლოდ მთელი რიცხვები!")

    except ZeroDivisionError:
        print("ნულზე გაყოფა არ შეიძლება!")


divide_numbers()


# 3


products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

cheap_products = list(filter(lambda product: product["price"] < 100, products))
print("ფასი 100-ზე ნაკლები:")
print(cheap_products)

product_info = list(
    map(lambda product: f"{product['name']} - {product['price']}", products)
)
print("\nყველა პროდუქტი:")
for item in product_info:
    print(item)

sorted_products = sorted(products, key=lambda product: product["price"])
print("\nდასორტირებული ფასის მიხედვით:")
print(sorted_products)

total_price = reduce(
    lambda total, product: total + product["price"],
    products,
    0
)
print("\nფასების ჯამი:", total_price)


# 4

def sum_numbers(n):
    if n == 1:
        return 1

    return n + sum_numbers(n - 1)


number = int(input("შეიყვანეთ რიცხვი: "))
print("ჯამი:", sum_numbers(number))
