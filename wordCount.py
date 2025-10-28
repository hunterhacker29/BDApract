

text = "hello world hello  world  welcome to  python  programming  world"


# arr= " ".join(text.split())

print(text)
# print(arr)

ar=[]

for i in text.split():
   
    
    ar.append(i)


# print(ar)

hash = {}


for i in ar:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1
        
        
        
        
print("Word Count is : ")
print(hash)

