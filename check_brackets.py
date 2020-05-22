# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(i)
            
        elif next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack and are_matching(text[opening_brackets_stack[-1]], next):
                opening_brackets_stack.pop()
            else:
                return i+1
    return opening_brackets_stack[-1]+1 if opening_brackets_stack else "Success"
            


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
