#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__maxstack = []

    def Push(self, a):
        if not self.__maxstack or a >= self.__maxstack[-1] :
            self.__stack.append(a)
            self.__maxstack.append(a)
        else:
            self.__stack.append(a)
            self.__maxstack.append(self.__maxstack[-1])

    def Pop(self):
        self.__stack.pop()
        self.__maxstack.pop()

    def Max(self):
        return self.__maxstack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
