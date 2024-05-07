n=int(input())
value=input()

arr=list(map(int,value.split()))

ans=0
bol=0

while True:
    cnt=0
    for val in arr:
        if val%2==1:
            bol=1
            break

        elif val==0:
            cnt+=1

    if bol==1 or cnt==n:
        break

    for i in range(n):
        arr[i]/=2

    ans+=1

print(ans)