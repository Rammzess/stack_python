class Stack: 
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[len(self.elements)-1]

    def size(self):
        return len(self.elements)


def brackets_checker():
    my_stack = Stack()
    for symbol in brackets_str:
        if symbol in parentheses_list_open:
            my_stack.push(symbol)
        elif symbol in parentheses_list_close:
            index = parentheses_list_close.index(symbol)
            if (my_stack.size() > 0) and (
                    parentheses_list_open[index] == my_stack.peek()):
                my_stack.pop()
            else:
                return "Несбалансировано"
    if my_stack.isEmpty():
        return "Сбалансировано"
    else:
        return "Несбалансировано"


if __name__ == '__main__':
    brackets_str = input('Введите набор скобок: ')
    parentheses = '[{(})]'
    parentheses_list_open = ["[", "{", "("]
    parentheses_list_close = ["]", "}", ")"]
    for element in brackets_str:
        if element not in parentheses:
            print("Вы ввели неверный символ!")
            raise StopIteration
    print(brackets_checker())
