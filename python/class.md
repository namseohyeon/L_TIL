## 클래스(class)
+ class & object(객체, 인스턴스)
+ 집의 설계도(class), 형태가 있는 집(object)
+ 가지고 있는 값들은 다르지만, 가져야할 특성은 공통적으로 가지고 있다.    
  
ex) class 클래스 이름:  
    -명사(속성)를 초기화 하는 공간  
    -동사를 정의하는 공간


### OOP(객체 지향 프로그래밍)
+ 객체를 중심으로 코드를 짜는 형식

### 클래스의 정의/클래스 호출
ex) class C:  #class 이름 맨 앞 대문자 필요  
        def __init__(self,h,w):  #내부적으로 저장되어 있는 함수  
            print("안녕")  
            self.h = h  
            self.w = w  
        def A(self): #맨 앞 인자는 <b>!self!</b> 필요      
            print("A")
            self.h = self.h + 1   

        def B():  
            print("B")  

word1 = C(h=100,w=50)  #할당 주소 저장됨   
word2 = C(h=150,w=20)  

#100, 50  
#150,20  

word.A() #A, 151가 출력됨  
=> C.A(word)가 전달된다고 생각 그래서 self가 인자가 됨  


+ 생성자
+ 안녕출력됨 __init__이 없으면 빈칸, 현재는 안녕을 뒤집어 씌움
+ 클래스 생성 시 호출됨
+ 

### 클래스의 상속
ex) class D(C): #인수에 상속 받고 싶은 클래스를 넣는다.
    name = "seohyeon"
    def F():  
        print("D")  
    #적지 않아도 C함수의 생성자, 함수들을 사용할 수 있다.  
    def __init__(self,h,w):  #내부적으로 저장되어 있는 함수  
        super.__init__(self,h,w) #부모 생성자이용  
        print("잘가")  
        self.r = r #추가적으로 선언  
        # 이런식으로 상속받은 함수를 추가, 수정 가능    
=>만약 상속받지 않으면 object라는 클래스를 상속받고 있다.

### 클래스 관점에서의 파이썬 기본 자료형
+ API: 프로그래밍 언어, 라이브러리, 애플리케이션 등이 제공하는 기능들을 제어할 수 있게 만든 인터페이스 
ex)  
a = [1,2,3]  
b = list([1,2,3])
c = {} ...   
a.append(4)
a.pop()  

### 객체를 인스턴스 변수로 가지고 있기
+ 매개변수에 어떤 객체든 여러개를 넣을 수 있다  
ex)def A(list, listA=[20,30,40], x = x):  #list를 변수로 넣은 경우   
    self.list = list  

A = A([100,200,300])

### 객체 method의 cascading 
ex2)    
team = Team(  
    coach = coach,  
    player_list = [  
        SoccerPlayer(70), #변수를 따로 만드는 과정을 생략해서 바로 변수를 리스트에 할당도 가능  
        SoccerPlayer(20),  
    ]
)   

team.player_list[0].walk() #옆 처럼 사용가능
