fi = open('./input.txt', 'r')
numOfCom = int(fi.readline().split()[0])
com = []

for line in fi:
    com.append(line.split())

stack = [None] * numOfCom
poped = [None] * numOfCom

j = 0
k = 0

for i in range(0, numOfCom):
    if com[i][0] == "+":
        stack[j] = int(com[i][1])
        j += 1
    else:
        poped[k] = stack[j-1]
        stack[j-1] = None
        j -= 1
        k += 1

print stack
print poped

fo = open('./output.txt', 'w')

for element in poped:
    if element:
        fo.write(str(element)+"\n")
