import time
import random

x = random.randint(0, 1000000)

password = f"Password{x}"
attempt = "Password"
number = 0

start = time.time()

while attempt != password:
    attempt = f"Password{number}"
    print(attempt)
    number += 1

end = time.time()

totaltime = round((end - start), 2)
if password == attempt:
    print(f"Password cracked. Password: {attempt}\nTime elapsed: {totaltime} s. ")

# just wanted to learn how to print out time elapsed


