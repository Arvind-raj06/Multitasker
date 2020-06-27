print("Welcome!!!")
from datetime import datetime
a=0
c=0
''' Type in your first name with @123'''
while(True):
    x=input("Enter the password \t")
    if "@123" in x and x.isalnum():
        print("==============")
        print("Welcome "x[:x.index('@')])
        print("==============")
        d=input("Looking for something new \t")
        if(d=='yes'):
            a=input("What's that? \t")
        else:
            print("Then go learn something new")
            input("Thank you for using this")
            break
        input("Ok good luck on your search \n") 
        break
    elif(x=='0000'):
        print("Welcome Guest")
        g=input("Your sweet name please:  ")
        file=open("Guest.txt","a")
        file.write(g)
        file.write("\n")
        file.close()
        print("Hi!")
        print(g)
        d=input("Looking for something new \t")
        if(d=='yes'):
                print("\nHere's the menu: \n")
                print("calc")
                print("sci calc")
                print("percent")
                print("surplus")
                print("compute")
                print("tract")
                a=input("\nWhat's that you want to do? \t")
        else:
            input("Thank you for using this")
            break
        input("Ok good luck on your search \n") 
        break
    else:
        
        g=input("\t WTF Who the hell are you? \t")
        print("\n")
        print("\t how did you get the access? \n")
        input("\t Get out of this login \n")
        intru=open("Intruder.txt")
        now = datetime.now()
        intru.write(now)
        intru.write("\n")
        intru.write(g)
        intru.close
        a=a+1
o=x
def welcome():
    if(a=='calc'):
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("Which arithmetic operation are you going to perform")
        c=input("Enter only the number \t")
        if(c=='1'):
            x=float(input("Enter the I number\t"))
            y=float(input("Enter the II number\t"))
            z=x+y
            print(z)
        elif(c=='2'):
            x=float(input("Enter the I number\t"))
            y=float(input("Enter the II number\t"))
            z=x-y
            print(z)
        elif(c=='3'):
            x=float(input("Enter the I number\t"))
            y=float(input("Enter the II number\t"))
            z=x*y
            print(z)
        elif(c=='4'):
            x=float(input("Enter the I number\t"))
            y=float(input("Enter the II number\t"))
            z=x/y
            print(z)
    elif(a=='exam'):
        input("All the best")
    elif(a=='surplus'):
        print("1. Prime numbers")
        print("2. Even numbers")
        print("3. Odd numbers")
        print("4. Factorial")
        j=input("Please enter only the number: \t")
        if(j=='1'):
            print("IN PROGRESS \n")
        elif(j=='2'):
            x=int(input("Enter the number for terms in it: \t"))
            i=0
            for i in range(x):
                if(i%2==0):
                    print(i)
        elif(j=='3'):
            x=int(input("Enter the number for terms in it: \t"))
            i=0
            for i in range(x):
                if(i%2==0):
                    i=i+1
                    print(i)
        elif(j=='4'):
            x=float(input("Enter a number: \t"))
            if(x=='1'):
                print(1)
            else:
                i=1
                y=1
                while i<=x:
                    y=y*i
                    i=i+1
                print(y)
    elif(a=='compute'):
        print("1. Tables")
        print("2. percent")
        print("3. permutation")
        f=input("Enter only the number \t")
        if(f=='1'):
            x=int(input("Enter the number: \t"))
            from itertools import count
            for i in count(1):
                print(i*x)
                if i>=10:
                    break
        elif(f=='2'):
            x=float(input("Enter the score \t"))
            y=float(input("Enter the total \t"))
            z=(x/y)*100
            print(z + '%')
        elif(f=='3'):
            x=int(input("Enter the number of elements(n): \t"))
            input("Permutation size is fixed (r): ")
            from itertools import permutations, product
            print(list(permutations(range(x))))
            print(len(list(permutations(range(x)))))
    elif(a=='sci calc'):
        print("1. Square")
        print("2. powering")
        print("3. Square root")
        print("4. Percentage")
        f=input("Enter only the number \t")
        if(f=='1'):
            x=float(input("Enter a number"))
            z=x*x
            print(z)
        elif(f=='2'):
            x=float(input("Enter a number \t"))
            y=float(input("Enter the power \t"))
            v=x
            w=2
            while w<=y:
               v=v*x
               w=w+1
            print(v)
        elif(f=='3'):
            import math
            x=float(input("Enter the number"))
            print(float(math.sqrt(x)))
        elif(f=='4'):
            x=float(input("Enter a number \t"))
            z=x/100
            c='%'
            print(z,c)
    elif(a=='text'):
        print("Welcome text is here")
        file=open("welcome.txt")
        cont=file.read()
        print(cont)
    elif(a=='DOB'):
        #dictionary
        ages={"Thangaraj":'21/3/1971',"Shanmuga Priya":'29/6/1982',"Arvind raj":'6/1/2001',"Bhadri raj":'14/6/2006'}
        x=input("Enter the name of the person \t")
        print(ages[x])
    elif(a=='percent'):
        print("Hello")
        def count(text,char):
            count=0
            for c in text:
                if c==char:
                    count+=1
            return count
        file_name=input("Enter a filename:  ")
        with open(file_name) as f:
            text=f.read()
        for char in "abcdefghijklmnoprstuvwxyz":
            perc=100*count(text,char)/len(text)
            print("{0}-{1}%".format(char,round(perc,2)))
    elif(a=='tract'):
        import re
        file=open("welcome.txt")
        cont=file.read()
        x=input("Enter the word that you want to search:\t")
        print(re.findall(x,cont))
        print(len(re.findall(x,cont)))
welcome()
if(o=='0000'):
    d=input("How's that  ")
    file=open("Guest.txt","a")
    file.write(d)
    file.write("\n")
    file.close()
    if(d=='nice'):
        input("Thank you")
    elif(d=='good'):
        input("Thank you!")
    elif(d=='very good'):
        input("Thank you!!!")
    elif(d=='excellent'):
        input("Thank you very much!!")
    elif(d=='great'):
        input("Thank you very much")
    elif(d=='well done'):
        input("Thank you!!")
    r=input("Have you enjoyed it??")
    file=open("Guest.txt","a")
    file.write(r)
    file.close
e='\0'
e=input("\n Do you want to exit or continue: \t")
while(e=='continue'):
    welcome()
