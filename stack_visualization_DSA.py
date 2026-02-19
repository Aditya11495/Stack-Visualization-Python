import matplotlib.pyplot as plt
import time

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        print(f"Pushed: {value}")

    def pop(self):
        if not self.is_empty():
            removed = self.items.pop()
            print(f"Popped: {removed}")
            return removed
        else:
            print("Stack is Empty")

    def is_empty(self):
        return len(self.items) == 0

    def visualize(self):
        plt.clf()
        plt.bar(range(len(self.items)), self.items)
        plt.title("Stack Visualization (LIFO)")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.pause(0.8)

stack = Stack()

plt.ion()

for value in [10, 20, 30, 40]:
    stack.push(value)
    stack.visualize()
    time.sleep(0.5)

stack.pop()
stack.visualize()

plt.ioff()
plt.show()
