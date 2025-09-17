#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
l = list(map(int, input("enter numbers: ").split()))
print(l)
k=[]
h=[]
for i in range(0,len(l)):
    for j in range(len(l)):
        k=[]
        if l[i]+l[j]==9:
            k.append(j)
            k.append(i)
            h=k
print(h)
            
            