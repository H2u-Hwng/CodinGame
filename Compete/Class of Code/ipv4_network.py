# Problem: https://docs.google.com/document/d/1-5qssCndhfAvlYnZZ0L7sq4Sc_7JuWtevvOItGHhXLU/edit?usp=sharing

input_count = int(input())

for i in range(input_count):
    ipaddress = input()
    
    # determine the address
    address = int(ipaddress.strip().split('/')[1])
    
    # calculate and display the max number of hosts for each network
    max_hosts = 2**(32 - address) - 2
    print(max_hosts)
