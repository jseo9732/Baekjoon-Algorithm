T = int(input())

for t in range(T):
    H, W, N, = map(int, input().split())
    if N % H == 0:
        floor = H
        num = N // H
    else:
        floor = N % H
        num = N // H + 1

    print(f'{floor  *100 + num}')
