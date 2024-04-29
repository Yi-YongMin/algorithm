import sys
N,M=map(int,sys.stdin.readline().split())
basket=[0]
for i in range(1,N+1):
    basket.append(i)
for i in range(M):
    s,l=map(int,sys.stdin.readline().split())
    temp=basket[s]
    basket[s]=basket[l]
    basket[l]=temp
print(*basket[1:])
