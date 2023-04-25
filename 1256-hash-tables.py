# -*- coding: utf-8 -*-
n = int(input())
for step in range(n):
    key, size = [int(i) for i in input().split()]
    hash_table = [[] for _ in range(key)]
    for value in [int(i) for i in input().split()]:
        hash_table[value % key].append(str(value))
    for i in range(key):
        output = hash_table[i]
        output.insert(0,str(i))
        output.append('\\')
        print(' -> '.join(output))
    if step != (n-1):
        print()