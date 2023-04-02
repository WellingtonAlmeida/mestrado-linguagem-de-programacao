# -*- coding: utf-8 -*-

def get_children_data(number_of_children):
    children = []
    for _ in range(number_of_children):
        name, number = input().split()
        children.append({"name": name, 'number': int(number)})
    return children


def play_right(children, origin, moves):
    child_to_remove = children[(children.index(origin)+moves) % len(children)]
    if child_to_remove['number'] % 2 == 0:
        next_child = children[(children.index(
            child_to_remove)+1) % len(children)]
    else:
        next_child = children[children.index(child_to_remove)-1]
    children.remove(child_to_remove)
    moves = child_to_remove['number']
    return next_child, moves


def play_left(children, origin, moves):
    child_to_remove = children[(children.index(origin)-moves) % len(children)]
    next_child = get_new_origin(children, child_to_remove)
    children.remove(child_to_remove)
    moves = child_to_remove['number']
    return next_child, moves


def get_new_origin(children, child_to_remove):
    if child_to_remove['number'] % 2 == 0:
        next_child = children[(children.index(
            child_to_remove)+1) % len(children)]
    else:
        next_child = children[children.index(child_to_remove)-1]
    return next_child


n = int(input())
while n != 0:
    children = get_children_data(n)
    child_with_token = children[0]
    moves = child_with_token['number']
    while len(children) > 1:
        if moves % 2 == 0:
            child_with_token, moves = play_left(
                children, child_with_token, moves)
        else:
            child_with_token, moves = play_right(
                children, child_with_token, moves)
    n = int(input())
    winner = children.pop()
    print(f"Vencedor(a): {winner['name']}")
