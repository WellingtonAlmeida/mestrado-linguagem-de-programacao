# -*- coding: utf-8 -*-
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def insert(self, new_value):
        if new_value < self.value:
            if self.left:
                self.left.insert(new_value)
            else:
                self.left = Node(new_value)
        elif new_value > self.value:
            if self.right == None:
                self.right = Node(new_value)
            else:
                self.right.insert(new_value)
        else:
            raise ValueError('Erro: Colisão de valores')
    # def __str__(self):
    #     return str(self.value)
    def get_children(self, value):
        node = self.get_node(value)
        left_value = node.left.value if node.left else None
        right_value = node.right.value if node.right else None
        return left_value, right_value
    def get_node(self, value):
        if (self.value == value):
            return self
        else:
            if (value < self.value):
                return self.left.get_node(value)
            else:
                return self.right.get_node(value)
    # def ordered(self, output):
    #     if self.left:
    #         self.left.ordered(output)
    #     output.append(self.value)
    #     if self.right:
    #         self.right.ordered(output)
    # def imprime(self):
    #     print(self.value)
    #     if self.left:
    #         self.left.imprime()
    #     if self.right:
    #         self.right.imprime()

class Tree:
    root: Node
    def __init__ (self):
        self.root = None
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.root.insert(value)
    def get_children(self, value):
        return self.root.get_children(value)
    def level_ordered(self):
        values = []
        output = []
        values.append(self.root.value)
        while len(values) > 0:
            value = values[0]
            values.remove(value)
            output.append(value)
            node = self.root.get_node(value)
            if node.left:
                values.append(node.left.value)
            if node.right:
                values.append(node.right.value)
        return output
    # def ordered(self):
    #     output = []
    #     self.root.ordered(output)
    #     return output
    # def imprime(self):
    #     self.root.imprime()

n = int(input())
for case in range(1, n+1):
    number_of_elements = int(input())
    elements = [int(i) for i in input().split()]
    tree = Tree()
    for node in elements:
        tree.insert(node)
    elements_ordered_by_level = tree.level_ordered()
    output = [str(e) for e in elements_ordered_by_level]
    output = ' '.join(output)
    print('Case '+str(case)+':')
    print(output)
    print()
