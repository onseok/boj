#https://coarmok.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%ACpython-%EB%B0%B1%EC%A4%80-11723%EB%B2%88-%EB%B9%84%ED%8A%B8%EB%A7%88%EC%8A%A4%ED%82%B9?category=910483
import sys
input = sys.stdin.readline

m = int(input())
bit = 0
for _ in range(m):
    command = input().split()

    if command[0] == "all":
        bit = (1 << 20) - 1

    elif command[0] == "empty":
        bit = 0

    else:
        op = command[0]
        num = int(command[1]) - 1

        if op == "add":
            bit |= (1 << num)

        elif op == "remove":
            bit &= ~(1 << num)

        elif op == "check":
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)

        elif op == "toggle":
            bit = bit ^ (1 << num)
