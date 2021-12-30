# Problem: https://docs.google.com/document/d/1bqcjarrWxMB-2zzIxx45_THnfB3XFHUe3sa8N2B5aDA/edit?usp=sharing

slots = int(input('Enter number of slots: ')) # prompt number of slots

n_cars = int(input('Enter number of cars: ')) # prompt number of cars

cars_dict = {} # initialize a cars dict

for _ in range(n_cars):
    car_id, tip = input('Enter a car id and its tip separated by a space: ').strip().split()
    cars_dict[car_id] = float(tip)
    
car_ids = input('car IDs or -car IDs separated by a space: ')
car_ids_list = car_ids.strip().split()

parked = earning = 0 # initialize a parked and an earning

# check each car id in the car ids list
for car_id in car_ids_list:
    if int(car_id) > 0:
        if parked < slots:
            parked += 1
            earning += cars_dict[car_id]
    else:
        parked -= 1
 
# display the Peter's earning
print(f'Peter earned ${earning:,.2f}.')
