T = int(input())
outputDict = {}

for i in range(T):
    N,M = map(int,input().split())
    space = list(map(int, input().split()))
    outputList = []
    compDict = {}


    for j in range(len(space)):
        if j not in compDict:
            compDict[j] = 0
        compDict[j] += space[j]
        for k in range(2,M+1):
            if j+k-1 < len(space):
                compDict[j] += space[j+k-1]
            else:
                break
    for p in range(0,len(space)-M):
        outputList.append(compDict[p])
    print(compDict)
    print("맥스",max(outputList))
    print("민",min(outputList))
    print("아웃풋리스트", outputList)
    outputDict[i] = max(outputList) - min(outputList)
    print(f"#{i+1} {outputDict[i]}")






