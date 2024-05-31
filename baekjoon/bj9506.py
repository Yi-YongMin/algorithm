def isPerfect(x):
    arr = [1]
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            arr.append(i)
    return arr


while True:
    N = int(input())
    if N == -1:
        break
    arr = isPerfect(N)
    if sum(arr) == N:
        print(str(N), "= 1", end=" ")
        for i in range(1, len(arr)):
            print(f"+ {arr[i]}", end=" ")
        print()
    else:
        print(f"{N} is NOT perfect.")
