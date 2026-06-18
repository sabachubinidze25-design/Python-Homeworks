# 1


def sum_numbers(times=5):
    total = 0

    for i in range(times):
        num = int(input("შეიყვანეთ რიცხვი: "))
        total += num

    return total


print(sum_numbers())

# 2


def odd_even_lists(*numbers):
    odd = []
    even = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return odd, even


odd_numbers, even_numbers = odd_even_lists(1, 2, 3, 4, 5, 6, 7)

print("კენტი:", odd_numbers)
print("ლუწი:", even_numbers)

# 3


def count_words(sentence):
    sentence = sentence.lower()

    for char in ".,!?;:":
        sentence = sentence.replace(char, "")

    words = sentence.split()

    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result


text = "This is a test. This test is fun."
print(count_words(text))
