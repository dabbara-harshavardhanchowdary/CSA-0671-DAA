def order(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count

def is_armstrong(n, order_val):
    if n == 0:
        return 0
    else:
        return ((n % 10) ** order_val + is_armstrong(n // 10, order_val))

num = int(input("Enter a number: "))
order_val = order(num)

if num == is_armstrong(num, order_val):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
