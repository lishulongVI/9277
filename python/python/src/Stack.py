class Stack(object):
    def __init__(self):
        self.item = []
    
    def push(self,value):
        self.item.append(value)
    
    def pop(self):
        return self.item.pop()

    def size(self):
        return len(self.item)
    
    def peek(self):
        if len(self.item) > 0:
            return self.item[len(self.item)-1]
        raise Exception('no peek value')


if __name__ == '__main__':
    que = Stack()
    que.push(1)
    que.push(2)
    print(que.peek())
    print(que.pop())
    print(que.size())

    print(  len('bank_balance_negative_much_bigger_than_applyed_amount'))
    
    
