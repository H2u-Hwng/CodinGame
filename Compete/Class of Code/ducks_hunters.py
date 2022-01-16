# Problem: https://docs.google.com/document/d/16Ymftq3qRHNbH-hGX8hx6gEPvQ4zp_MPY-uNKFoqMds/edit?usp=sharing

hunters_count = int(input())
ducks_count = [0 for _ in range(int(input()))]

for i in range(hunters_count):
    shootduck = int(input())
    ducks_count[shootduck] = 1

print(ducks_count.count(0))
