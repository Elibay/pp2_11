# int a[100];
# a = []
a = [1, 2, "abc", 1.12]
b = (1, 2, "abc", 1.12)
# for i in a:
#     print(i + i)

# for i in b:
#     print(i + i)

# for (int i = 1; i < 3; ++ i)
n = len(a)
# range(i, j, k) -> i..j, i += k
for i in range(n - 1, -1, -1):
    print(a[i])

range(n)  # 0...n-1
range(0, n)  # 0...n-1
range(0, n, 1)  # 0...n-1
