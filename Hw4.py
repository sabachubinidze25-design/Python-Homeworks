# 1

sentence = input("შეიყვანე წინადადება: ")
words = sentence.split()

first = words[0]
last = words[-1]

words[0] = last
words[-1] = first

result = " ".join(words)
print("შედეგი:", result)


# 2

sentence = input("შეიყვანე წინადადება: ")
words = sentence.split()

longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print("ყველაზე გრძელი სიტყვაა:", longest)

# 3

word1 = input("შეიყვანე პირველი სიტყვა: ")
word2 = input("შეიყვანე მეორე სიტყვა: ")

word1 = word1.lower()
word2 = word2.lower()

if sorted(word1) == sorted(word2):
    print("ეს სიტყვები ანაგრამაა")
else:
    print("ეს სიტყვები არ არის ანაგრამა")
