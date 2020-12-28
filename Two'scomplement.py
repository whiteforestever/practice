s = "1101"
right_end = len(s)
i = len(s) - 1
while i >= 0:
    if (s[i]=='1'):
        right_end = i
        break
    i-= 1
for i in range(right_end):
    if (i == 0):
        continue
    if (s[i] == '0'):
        s = s[0:i] + '1' + s[i+1:len(s)]
    else:
        s = s[0:i] + '0' + s[i+1:len(s)]
print(s)
