a=input('Enter the parity bit data : ')
name=a.split()
b=0
c=0
x=[]
y=[]
for i in a:
    if i=='1':
        b=b+1
    else:
        c=0
if b%2==0:
    for i in name:
        name1=i + '1'
else:
    for i in name:
        name1 = i + '0'
print('\nParity bit data is {}'.format(name1))
for i in name1:
    x.append(i)
#print(x)
while c < len(a):
    if x[c]=='0':
        if x[c+1]=='1':
            if x[c+2]=='0':
                x.insert(c+3,'1')
                y.append(c+3)
    c=c+1
x[y[0]]='0'
x[y[1]]='0'
x[y[2]+1]='0'
x.append('0101')
#print(x)
name2=''.join(x)
print('\nTransmitting data : {}'.format(name2))







