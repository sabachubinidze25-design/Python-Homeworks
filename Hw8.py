# 1

def text_info(text):
    count = 0

    for char in text:
        if char.isupper():
            count += 1

    return count, text.upper()


text = input("Enter text: ")

result = text_info(text)

print("Number of uppercase letters:", result[0])
print("Uppercase text:", result[1])


# 2

def camel_to_snake(word):
    result = ""

    for char in word:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char

    return result


variable = input("Enter variable name: ")

print(camel_to_snake(variable))
