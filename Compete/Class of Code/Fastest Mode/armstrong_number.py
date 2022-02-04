# Problem: https://docs.google.com/document/d/1hMiD6w01DZIMkVU0HJi9ezwWbE53No4Xi-Z9t_ODf9s/edit?usp=sharing


n = int(input())

for num in range(1, n):
    order = len(str(num))

    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)
