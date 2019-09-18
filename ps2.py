print('---------------------------')
print('Welcome to the Game')
print('---------------------------')
list1=['0','0','0','0','0','0','0','0','0']
list2=[0,0,0,0,0,0,0,0,0]
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0
a9=0
x=0
while 1:
    print('\n1. Play Tic-Tac-Toe Game\n2. Exit')
    a=int(input('\nEnter your choice : '))
    if a==1:
        b=str(input('\nEnter player 1 name : '))
        c=str(input('\nEnter player 2 name : '))
        d=str(input('\nWhat you want to become even player or odd player : '))
        print('\nPlayer {} is odd player and Player {} is even player'.format(b,c))
        print('\n-------Game Started-------\n')
        string=''.join(list1)
        print(string[0:3])
        print(string[3:6])
        print(string[6:9])
        while x<=8:
            pos1=input('Enter position player {} : '.format(b))
            num1=input('Enter number player {} : '.format(b))
            if num1 >='1' and num1 <='9':
                if pos1=='1':
                    list1[0]=num1
                    list2[0]=int(num1)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1=list2[0]
                    a2=list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1+a2+a3)==15 or (a4+a5+a6)==15 or (a7+a8+a9)==15 or (a1+a4+a7)==15 or (a2+a5+a8)==15 or (a3+a6+a9)==15 or (a1+a5+a9)==15 or (a3+a5+a7)==15:
                        print('Player {} Wins'.format(b))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos1=='2':
                    list1[1] = num1
                    list2[1] = int(num1)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(b))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (
                            a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (
                            a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos1=='3':
                    list1[2] = num1
                    list2[2] = int(num1)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(b))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (
                            a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (
                            a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos1=='4':
                    list1[3] = num1
                    list2[3] = int(num1)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(b))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (
                            a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (
                            a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos1=='5':
                    list1[4] = num1
                    list2[4] = int(num1)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(b))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (
                            a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (
                            a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos1=='6':
                    list1[5] = num1
                    list2[5] = int(num1)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(b))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos1=='7':
                    list1[6] = num1
                    list2[6] = int(num1)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(b))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos1=='8':
                    list1[7] = num1
                    list2[7] = int(num1)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(b))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos1=='9':
                    list1[8] = num1
                    list2[8] = int(num1)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(b))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                else:
                    print('\n--------Game Error--------\n')
                    print('You entered wrong position')
                    print('\nEnter Again\n')
                    continue

            pos2 = input('Enter position player {} : '.format(c))
            num2 = input('Enter number player {} : '.format(c))
            if num2 >= '1' and num2 <= '9':
                if pos2 == '1':
                    list1[0] = num2
                    list2[0] = int(num2)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (
                            a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(c))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos2 == '2':
                    list1[1] = num2
                    list2[1] = int(num2)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (
                            a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(c))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos2 == '3':
                    list1[1] = num2
                    list2[1] = int(num2)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (
                            a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(c))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos2 == '4':
                    list1[1] = num2
                    list2[1] = int(num2)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (
                            a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(c))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos2 == '5':
                    list1[1] = num2
                    list2[1] = int(num2)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (
                            a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(c))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos2 == '6':
                    list1[1] = num2
                    list2[1] = int(num2)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (
                            a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(c))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos2 == '7':
                    list1[1] = num2
                    list2[1] = int(num2)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (
                            a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(c))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos2 == '8':
                    list1[1] = num2
                    list2[1] = int(num2)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (
                            a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(c))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                elif pos2 == '9':
                    list1[1] = num2
                    list2[1] = int(num2)
                    string = ''.join(list1)
                    print(string[0:3])
                    print(string[3:6])
                    print(string[6:9])
                    a1 = list2[0]
                    a2 = list2[1]
                    a3 = list2[2]
                    a4 = list2[3]
                    a5 = list2[4]
                    a6 = list2[5]
                    a7 = list2[6]
                    a8 = list2[7]
                    a9 = list2[8]
                    if (a1 + a2 + a3) == 15 or (a4 + a5 + a6) == 15 or (a7 + a8 + a9) == 15 or (a1 + a4 + a7) == 15 or (
                            a2 + a5 + a8) == 15 or (a3 + a6 + a9) == 15 or (a1 + a5 + a9) == 15 or (a3 + a5 + a7) == 15:
                        print('Player {} Wins'.format(c))
                        break
                    if (a1 + a2 + a3) >= 15 and (a4 + a5 + a6) >= 15 and (a7 + a8 + a9) >= 15 and (a1 + a4 + a7) >= 15 and (a2 + a5 + a8) >= 15 and (a3 + a6 + a9) >= 15 and (a1 + a5 + a9) >= 15 and (a3 + a5 + a7) >= 15:
                        print('\n------Game Draw-------\n')
                        print('\n------Better Luck Next Time------\n')
                        break
                else:
                    print('\n--------Game Error--------\n')
                    print('You entered wrong position')
                    print('\nEnter Again\n')
                    continue

            x=x+1
    else:
        print('--------------------------')
        print('Thank You for Playing Game')
        print('--------------------------')
        exit()


