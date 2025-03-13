#!/usr/bin/env python

def to_fifty(max_value):
    numbers = list(range(0, max_value + 1, 5))
    print(numbers)

def main():
    max_value = int(input("Enter a maximum value: "))
    to_fifty(max_value)

if __name__ == "__main__":
    main()
