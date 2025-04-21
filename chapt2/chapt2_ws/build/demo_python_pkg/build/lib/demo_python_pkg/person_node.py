import rclpy
from rclpy.node import Node
class PersonNode:
    def __init__(self, name:str, age:int) -> Node:
        self.age = age
        self.name = name
    
    def eat(self, food_name:str):
        print(f'I am{self.name}')

def main():
    node = PersonNode('xiao', 1)
    node.eat('apple')