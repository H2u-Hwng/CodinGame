# Problem: https://docs.google.com/document/d/1Ryda4QEPG4tW-hSrc1BHI0EJZy0txgybxbEngxGAAY0/edit?usp=sharing

me = input().split()
n = int(input())
d = {}
for i in range(n):
    date = input().split()
    result = date[0]
    count = 0
    if n == 1:
        print(result)
        break
    else:
        for i in date[1:]:
            if i in me:count += 1
        d[result] = count
print(max(d, key=d.get))
