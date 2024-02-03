# n = 7
# i = 1
# while n > 0:
#     print(i)
#     n -= 1
#     i = i * 2

n = int(input())
i = 2
is_prime = True
while i * i <= n:
    if n % i == 0:
        is_prime = False
    i = i + 1
print(is_prime)
