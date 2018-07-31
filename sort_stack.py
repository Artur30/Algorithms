def sort_stack(stack):
    temp_stack = []
    while stack:
        x = stack.pop()
        while temp_stack and temp_stack[-1] > x:
            stack.append(temp_stack.pop())
        temp_stack.append(x)
    return temp_stack


if __name__ == '__main__':
    stack = [3, 2, 1, 5, 4, 7, 0]
    stack = sort_stack(stack)
    print(stack)
