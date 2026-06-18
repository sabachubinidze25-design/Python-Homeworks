# 1
import math

a = int(input("პირველი კათეტის სიგრძე: "))
b = int(input("მეორე კათეტის სიგრძე: "))

c = math.sqrt(a**2 + b**2)
print("ჰიპოტენუზა =", c)

area = (a*b)/2
print("ფართობი = ", area)

# 2

seconds = int(input("წამების რაოდენობა: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print(hours, "საათი,", minutes, "წუთი,", remaining_seconds, "წამი")
