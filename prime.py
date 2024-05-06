def prime(x):
    start = 0
    while start <= x:
        for i in range(2, x + 1):
            if x % i != 0:
                start += 1
                if round(x / i, 0) == 1:
                    print(f"The number {x} is prime! ")
                    break
            elif x % i == 0:
                print(f"The number {x} is not prime. ")
                break
        break

number = int(input("Enter a number to check if it is prime: "))
prime(number)

