# -*- coding: utf-8 -*-
def get_total_time(cashier):
    return cashier["total_time"]


def get_id(cashier):
    return cashier["id"]


number_of_cashiers, number_of_clients = list([int(i) for i in input().split()])
times = list([int(i) for i in input().split()])
items = list([int(i) for i in input().split()])
clients = []
cashiers = []
for i in range(number_of_clients):
    client = {"id": i, "items": items[i]}
    clients.append(client)
for j in range(number_of_cashiers):
    cashier = {"id": j, "time": times[j], "total_time": 0}
    cashiers.append(cashier)
while clients:
    client = clients[0]
    cashier = cashiers[0]
    cashier["total_time"] += client["items"]*cashier["time"]
    cashiers = sorted(cashiers, key=lambda c: (get_total_time(c), get_id(c)))
    clients.remove(client)
print(cashiers.pop()["total_time"])
