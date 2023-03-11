# cook your dish here
for _ in range(int(input())):
    s=input()
    s1=s[1:len(s)]+s[0]
    s2=s[-1]+s[0:len(s)-1]
    if(s1==s2 or s==s1 or s2==s):
        print("YES")
    else:
        print("NO")