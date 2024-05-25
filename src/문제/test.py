total = int(input("테스트 케이스 수를 입력하세요: "))

for i in range(total):
    K, N, M = map(int, input().split())
    pikaStop = list(map(int, input().split()))

    stop = [0] * (N + 1)
    for station in pikaStop:
        stop[station] = 1

    position = 0
    fuel = K
    chargeCount = 0

    while position < N:
        if position + K >= N:
            break

        max_reachable = position + K
        next_position = -1

        for j in range(position + 1, max_reachable + 1):
            if stop[j] == 1:
                next_position = j

        if next_position == -1:
            chargeCount = 0
            break

        position = next_position
        chargeCount += 1

    print(f"#{i+1} {chargeCount}")
