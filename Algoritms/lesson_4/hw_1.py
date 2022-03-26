#Задание №1 Реализовать структуру данных стэк, который за О(1) выдает минимум в стэке.

class MinStack:
    stack = []

    def push(self, value: int):
        self.value = value
        self.stack.append(self.value)

    def pop(self):
        self.stack.pop()

    def top(self) -> int:
        return max(self.stack)

    def getMin(self) -> int:
        return min(self.stack)

minstack = MinStack()

minstack.push(1)
minstack.push(0)
minstack.push(-1)
minstack.push(-4)
minstack.top()
minstack.getMin()
minstack.pop()
minstack.getMin()

