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
                return self.left.get_node(value) if self.left else False
            else:
                return self.right.get_node(value) if self.right else False
    def in_order(self, output):
        if self.left:
            self.left.in_order(output)
        output.append(self.value)
        if self.right:
            self.right.in_order(output)
    def pre_order(self, output):
        output.append(self.value)
        if self.left:
            self.left.pre_order(output)
        if self.right:
            self.right.pre_order(output)
    def pos_order(self, output):
        if self.left:
            self.left.pos_order(output)
        if self.right:
            self.right.pos_order(output)
        output.append(self.value)

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
    def exists(self, value):
        return self.root.get_node(value)
    def in_order(self):
        output = []
        self.root.in_order(output)
        return output
    def pre_order(self):
        output = []
        self.root.pre_order(output)
        return output
    def pos_order(self):
        output = []
        self.root.pos_order(output)
        return output

tree = Tree()
while True:
  try:
    command = input().split()
    operation = command[0]
    if len(command) > 1:
        parameter = command[1]
        if operation == 'I':
            tree.insert(parameter)
        elif operation == 'P':
            if tree.exists(parameter):
                print(parameter + ' existe')
            else:
                print(parameter + ' nao existe')
    else:
        output = []
        if operation == 'INFIXA':
            output = tree.in_order()
        elif operation == 'PREFIXA':
            output = tree.pre_order()
        elif operation == 'POSFIXA':
            output = tree.pos_order()
        print(' '.join(output))

  except EOFError:
    break