# 10 곱셈
x,y = map(int, input().split())

print(int(x * (y % 10)))
print(int(x * ((y / 10) % 10)))
print(int(x * (y / 100)))
print(x * y)
