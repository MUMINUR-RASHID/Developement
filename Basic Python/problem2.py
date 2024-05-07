n = int(input())
value = input()
arr1 = list(map(int, value.split()))

arr1.sort()

ans = 0
val = 0
cnt=0
for i in range(n):
    if val==arr1[i]:
        cnt+=1
    else:
        if val>cnt:
            ans += cnt
        else:
            ans+=(cnt-val)
        
        val=arr1[i]
        cnt=1
if val>cnt:
    ans += cnt
else:
    ans+=(cnt-val)
    
print(ans)
