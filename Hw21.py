import threading
import math


def is_prime(num):
    if num < 2:
        print(f"{num} -> არ არის მარტივი")
        return

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(f"{num} -> არ არის მარტივი")
            return

    print(f"{num} -> მარტივია")


num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

threads = []

for num in num_list:
    t = threading.Thread(target=is_prime, args=(num,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("ყველა შემოწმება დასრულდა.")
