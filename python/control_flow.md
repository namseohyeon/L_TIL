## 제어문

### if
+ 조건에 따라 동작
+ 구조
+ true면 아래 구문이 실행된다
ex) if(a>b):  
        구문1  
    else:  
        구문2  #생략가능  

+ boolean condition 예시  
a = "삼성전자2" in title #bool값 출력됨         

### 반복문
ex1)    
for 임시변수 in 리스트같은 형식의 자료형:
    if(bool형 조건):        
        구문1
        구문2
    else:  
        continue #다음 반복을 시작 현재 수 +1 반복문 시작  
      
ex2)  
for i in range(시작값, 끝값+1, 수가 변하는 크기):
    if(bool형 조건):  
        구문 
        <b>break</b> #반복문을 멈추고 나감 

### list comprehension
list = []  
for i in range(1,10):  
    list.append(i)

=>  [list for i in range(1,11) if i % 2 == 0] #list = [2,4,6,8,10]  

### while
+ for문 비슷
+ 구조
ex) while(비교연산):  
    구문1  
    a= a+1 #사용되는 변수의 값을 변경하는 로직 필요   
     
