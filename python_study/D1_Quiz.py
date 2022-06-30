#1
# print("\"naver\"","\"kakao\"","\"samsung\"")
# print("naver;","kakao;","samsung;")
# print("naver","kakao","samsung", sep=";" )

#2
# print("first",end="");print("second")

#3
# a="132"
# print(type(a))

#4
# num=100
# print(str(num))

#5
# license_plate = "24가 2210"
# print(license_plate[4:8]) #포함:미포함
# print(license_plate[-4:])
# print(license_plate.split()[1])

#6
# string = "홀짝홀짝홀짝"
# print(string[::2])

#7
# string = "PYTHON"
# print(string[::-1])

#8
# phone_number = "010-1111-2222"
# new_phone_number=phone_number.split("-")
# New_phone_number=" ".join(new_phone_number)
# print(New_phone_number)

#phone_number = phone_number.replace("-", " ")
#print(phone_number)

#9
#오류가 생긴다

#10
# str="hello,everyone"
# new_str=str.split(",")
# print(new_str)

#11
# data = " LG전자 "
# Ndata=data.strip()
# print(Ndata)

#12
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# movie_rank.append("배트맨")
# movie_rank.insert(1,"슈퍼맨")
# movie_rank.remove("배트맨") #del movie_rank[3]
# print(movie_rank)

#13
# nums = [1,2,3,4,5,6,7]
# print(max(nums))

#14
# print(nums[::-1])

#15
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest1 = " ".join(interest)
# print(interest1)

#16
# t = ('a', 'b', 'c')
# tlist = list(t)
# tlist[0] = "A"
# t = tuple(tlist)
# print(t)

#17
# inventory = {"메로나":300,"비비빅":400,"죠스바":250}
# print(inventory["메로나"])

# print(list(inventory.keys()))

# print(list(inventory.values()))

# del inventory["죠스바"] # inventory.pop("죠스바")

# print(inventory)

#18
# mylist = ["SK하이닉스", "삼성전자", "LG전자"]
# print(len(mylist[0]))
# print(len(mylist[1]))
# print(len(mylist[2]))

#19
# mylist=["가", "나", "다", "라"]
# for i in mylist[::-1]:
#     print(i)

# length=len(mylist);
# for i in range(length):
#     print(mylist[length-1-i]);

# for i in range(len(mylist)-1, -1, -1):
#     print(mylist[i])


#20
# mylist= ["A", "b", "c", "D"]
# for i in mylist:
#     if(i.isupper()):
#         print(i)

#21
# mylist= ['dog', 'cat', 'parrot']
#  #한글자만 대문자로 변환
# for i in range(0,3):
#     print(mylist[i].capitalize())

#22
# for i in range(2002,2051,4):
#     print(i)

#23
# def print_arithmetic_operation(x,y):
#     print(x+y)
#     print(x-y)
#     print(x*y)
#     print(x/y)
# x= int(input("수를 입력해주세요"))
# y= int(input("수를 입력해주세요"))
# print_arithmetic_operation(x,y)

# a,b = map(int,input().split())
# def print_arithmetic_operation(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
    
# print_arithmetic_operation(a,b)

#24

# def print_max(a,b,c):
#     if(a>=b):
#         max = a
#         if(a>c):
#             if(b>c):
#                 mid = b
#                 min =c
#             else:
#                 mid = c
#                 min = b
#         else:
#             max =c
#             mid =a
#             min = b
#     elif(b>=c):
#         max = b
#         if(b>a):
#             if(a>c):
#                 mid = a
#                 min =c
#             else:
#                 mid = c
#                 min = a
#         else:
#             max =a
#             mid =b
#             min = c
#     elif(c>=a):
#         max = c
#         if(c>b):
#             if(b>a):
#                 mid = b
#                 min =a
#             else:
#                 mid = a
#                 min = b
#         else:
#             max =b
#             mid =c
#             min = a
#     print("max: ",max)
#     print("mid: ",mid)
#     print("min: ",min)

# x= int(input("수를 입력해주세요"))
# y= int(input("수를 입력해주세요"))
# z= int(input("수를 입력해주세요"))
# print_max(x,y,z)

# def print_max(num1, num2, num3):
#     max = 0
#     if num1 > max:
#         max = num1
#     if num2 > max:
#         max = num2
#     if num3 > max:
#         max = num3
#     return max

# def print_max():
#     num = list(map(int, input().split()))
#     max=0
#     for _ in num:
#         if max < _:
#             max=_

#     print(max)

# print_max()

#25 
# def print_score(list):
#     return sum(list)/len(list) #리스트나 튜플 처럼 인덱스 순환 접근이 가능한 자료형

# print(print_score([100,80,90]))

#26
# class Stock:
#     # pass 

#27
# class Stock:
#     def __init__(self, name, code):
#         self.name=name
#         self.code=code
        
# 삼성=Stock("삼성전자","005930")
# print(삼성.name); #삼성전자

#28
# class Stock:
#     def __init__(self, name, code):
#         self.name=name;
#         self.code=code;
#     def set_name(self,name):
#         self.name=name;

# a=Stock(None,None);
# a.set_name("삼성전자")
# print(a.name); #삼성전자

#29
# class Animal():
#     def __init__(self, name, species):
#         self.name=name
#         self.species=species
#     def greet(self):
#         print(f'Hi! My name is {self.name} and I am a {self.species}')

# class Cat():
#     def __init__(self,name):
#         Animal.__init__(self,name,"cat");
#     def greet(self):
#         print("Meow");

# class Dog():
#     def __init__(self,name):
#         Animal.__init__(self,name,"dog")
#     def greet(self):
#         print("Dog")

# c=Cat("kitty")
# c.greet()

# d=Dog("doggy")