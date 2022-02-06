ctr = 0
lastIndex = 0
bOfLastWord = 0
x = 0
string = '   this    is a test   '

while x < len(string):
    if string[x] == ' ':
        if string[x+1] != ' ':
            x + 1 = bOfLastWord

while x < len(string):
    if string[x] != ' ':
        lastIndex = x 
    x = x + 1
x = 0
while x < lastIndex:
    if string[x] == ' ' and string[x] != string[x - 1] and x != 0 :
        ctr = ctr + 1    
    x = x + 1
print(ctr + 1)

print(string[bOfLastWord:lastIndex])