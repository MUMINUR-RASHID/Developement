s=input()
sub_string=[]
n=len(s)

temp_string=""

for i in range(n):
    temp_string= temp_string + s[i]

    if temp_string.count('L')==temp_string.count('R'):
        sub_string.append(temp_string)
        temp_string=""

print(len(sub_string))
for str in sub_string:
    print(str)