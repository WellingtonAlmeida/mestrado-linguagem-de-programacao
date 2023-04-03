# -*- coding: utf-8 -*-
number_of_cashiers, number_of_clients = input().split()
times = input().split()
items = input().split()
total_time = [0]*len(times)
current_cashier_index = 0
for client_index in range(len(items)):
    total_time[current_cashier_index] += int(items[client_index])*int(times[current_cashier_index])
    current_cashier_index = current_cashier_index + 1 if current_cashier_index < len(times) - 1 else 0
total_time.sort()
print(total_time.pop())
