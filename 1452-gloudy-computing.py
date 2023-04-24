# -*- coding: utf-8 -*-
number_of_servers, number_of_clients = [int(p) for p in input().split()]
while number_of_servers != 0 and number_of_clients != 0:
    total_connections = 0
    servers = {}
    clients = {}
    for s in range(number_of_servers):
        servers[s] = input().split()[1:]
    for c in range(number_of_clients):
        clients[c] = input().split()[1:]
    for c in clients:
        connections = set()
        for client in clients[c]:
            for server in servers:
                if client in servers[server]:
                    connections.add(server)
        total_connections += len(connections)
    print(total_connections)
    number_of_servers, number_of_clients = [int(p) for p in input().split()]