##1
# print("hello world")

##2
# for i in range(int(input())):
#     print("i =",i,"sum =",i+10)

##3
# for i in range(int(input())):
#     print("i =",i,"sum =",i+10)


##4
def count_vowels(s):

    count = 0

    for char in s:

        if char.lower() in ['a', 'e', 'i', 'o', 'u']:

            count += 1

    print(count)

count_vowels(input())

