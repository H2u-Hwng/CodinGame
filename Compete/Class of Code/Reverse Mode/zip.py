# Problem: https://docs.google.com/document/d/1tS-7_Z0VNpwO-8lgj6B3NWzIN9bHtQW7Pxqhy8U4HvQ/edit?usp=sharing

message = input()
rev = message[::-1]

for a, b in zip(message, rev):
    print(a, b)
