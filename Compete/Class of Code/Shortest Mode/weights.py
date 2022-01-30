# Problem: https://docs.google.com/document/d/1_Z9_z7szxpcNixJuV8wQw2K6yJHSFKdxjHtJ0DQ_CrQ/edit?usp=sharing

g=input()
w=int(input())
if g not in ['F','M']:
    print('UNKNOWN')
else:
    print(int(w*1.2) if g=='F' else int(w/1.2))
