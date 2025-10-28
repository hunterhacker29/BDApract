## static 
# def Trailing (n):
#     if n==1 or n ==0 or n==5:
#         return 0
    
#     if n==10 :
#         return 1
    
#     if n ==4 :
#         return 2
    
     

# x = [1,5,10,5,15,1]

# hashs = []



# for i in x :
#     h= i % 11
#     hashs.append(h)
    
# print(x)
# print(hashs)

# ans = []

# for i in hashs:
#     ans.append(Trailing(i))
    

# print(ans)

# maxx = max(ans)
# print(maxx)


# anss = 2**maxx

# print("Distinct Element Count is ",anss)






## dynamic



def Trailing (n):
    
    
    count = 0 
    num = str(n)
   
    for i in range(len(num)-1,-1,-1):
        if num[i] =='1':
            break
        else:
            count +=1
    return count


x = [1,5,10,5,15,1]

hashs = []

binhash=[]


for i in x :
    h= i % 11
    hashs.append(h)
    
    
for i in hashs :
    binhash.append(bin(i)[2:])
    

print(x)
print(hashs)

print(binhash)

ansss = []

for i in binhash:
    ansss.append(Trailing(i))
    
print(ansss)
count = 2** max(ansss)


print("Distinct Element Count is ",count)

