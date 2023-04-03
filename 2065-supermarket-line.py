# -*- coding: utf-8 -*-
number_of_cashiers, number_of_clients = input().split()
times = [int(i) for i in input().split()]
items = [int(i) for i in input().split()]
total_time = [0]*len(times)
current_cashier_index = 0
for client_items in items:
    total_time[current_cashier_index] += client_items*times[current_cashier_index]
    current_cashier_index = total_time.index(min(total_time))
print(max(total_time))
