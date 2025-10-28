
stream = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1]
stream = stream[::-1]


ans = []
print(stream)

for i in stream:
    if i == 1:
        ans.append(1)

print(ans)



windows = []
i = 0
power = 0



while i < len(ans):
    size = 2 ** power
    if i + size <= len(ans):
        window = ans[i:i + size]
        windows.append(window)
        i += size
        power += 1
    else:
        
        window = ans[i:]
        windows.append(window)
        break

print(windows)

