# Problem: https://docs.google.com/document/d/1Rcf7RWJ54E1UD-TUfoXhvNu4l6kzeRDg-rZocz4UCD8/edit?usp=sharing

n, t0, t1, t2 = [int(i) for i in input().split()]

corns_list = [t0, t1, t2]

for i in range(n - 2):
    corns_list += [corns_list[i] + corns_list[i+1] + corns_list[i+2]]

print(corns_list[-1] % 1000000007)
