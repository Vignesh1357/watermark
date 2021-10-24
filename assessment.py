a= 4

output=[]

for idx,i in enumerate(range(a)):
    if i==a:
        output.append('*'*i)
    else:
        output.append('*'*(i+idx-1))

maxi=len(output[-1])

for j in output:
    print(j.center(maxi))