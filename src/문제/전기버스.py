#
# A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
#
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
#
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
#
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
#

total = int(input())

chargeCount = 0

for i in range(0,total):
    K,N,M = map(int,input().split())
    pikaStop = list(map(int,input().split()))
    stop = []
    remain = N + 1
    fuel = K
    for k in range(0,N+1):
        stop.append(0)
    for a in range(0,len(pikaStop)):
        stop[pikaStop[a]] = 1
    print(stop)
    for j in range(0,N+1):
        remain -= 1
        if remain == fuel:
            break
        if (stop[j] == 0):
            fuel = K
            chargeCount += 1
        else:
            fuel -= 1
            print(fuel)
            if fuel < 0:
                chargeCount = 0
                break


    print(f"#{i+1} {chargeCount}")






