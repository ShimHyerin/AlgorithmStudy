import sys
input = sys.stdin.readline

n = int(input())

def push(stack, x):
    stack.append(x)
    return stack

def pop(stack):
    if stack: print(stack.pop())
    else: print(-1)
    return stack

def size(stack):
    print(len(stack))

def empty(stack):
    if stack: print(0)
    else: print(1)

def top(stack):
    if stack: print(stack[-1])
    else: print(-1)

stack = []
for i in range(n):
    prompt_ = input().split()
    prompt = prompt_[0]

    if prompt == 'push':
        push(stack, prompt_[1])
    elif prompt == 'pop':
        pop(stack)
    elif prompt == 'size':
        size(stack)
    elif prompt == 'empty':
        empty(stack)
    else:
        top(stack)