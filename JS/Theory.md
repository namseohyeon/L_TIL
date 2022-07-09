## why js
+ 상호작용이 가능한 웹을 위한 만들어짐
+ 프로트엔드에서 유일한 프로그래밍 언어
+ 백엔드에서는 사용할 수 있는 언어 많음
+ 게임 만들때 js,css,html만 알면 됨 
+ three.js는 자바스크립트로 3D구현 라이브러리 -> 데이터 시각화 가능
+ 프레임워크로 사용 가능 -> 앱, 웹 만들 수 있음
+ 백엔드도 JS로 가능
+ 실시간 기능 할 때 좋음
+ 머신러닝도 가능(ml5.js 사용시 러닝메신 모델 생성 웹 사이트 구축하여 모델 훈련 가능)
+ 브라우저에서 열어야 js 파일 실행 아님
+ html을 브라우저에서 열고, html 파일에서 import된 js를 가져옴
+ consloe에서 js 사용가능

### Basic Data Types
+ int: 숫자 및 연산자 사용가능 => 숫자 계산 가능
+ string: 문자 사용 시 "",'' 필요 +이용하여 문자들 붙이기 가능
+ booleans: true, false 사용
+ null: 값이 주어졌는데 값에 아무것도 없음 #파이썬은 none
+ undefined: 값이 정의 되지 않음

### Variables
+ 값을 저장 및 유지 
+ 변수이름 규칙(띄어쓰기x, 카멜식 사용)
+ 상수: const a = 5 / 값을 유지, 바뀌지 않음
+ 변수: let b = "hi" / 값 수정 가능
+ 과거에는 var 사용 /  값 수정 가능, 하지만 같은 변수를 또 선언해도 , 에러가 나오지 않고 각기 다른 값이 출력됨(사용x)


### Arrays
+ 자료구조
+ 데이터로 이루어져 있는 리스트
+ 리스트 안에 다른 타입을 넣어도 됨
+ const sum = ['hi',1, true]
+ sum[0] #hi 출력
+ sum.push("push") #값 추가 #파이썬은 append

### Objects
<pre>
+ const ob = { # 안에 속성 작성
    name: "seohyeon",
    point: 10
}  
</pre>
console.log(ob.point) #10 출력
+ ob.point = 20 # Objects안 속성 변경
+ ob.lastName = "nam" # Objects안 속성 추가


### function
<pre>
+ function A(name, age){ console.log(name, age); }  
    A("seohyeon",10);
+ 객체 안에 넣을 수 있음  
const player = {
    name="nico",  
    say: function(name){
        console.log("hi" + name);  
    },  
};  
</pre>
player.say("didi");  
+ return #반환

### conditonals
+ if(condition1){} else if(condition2){} else{}
+ typeof age #타입 알아내기
+ parseInt("1") #"1"을 1로 만듬, 숫자 문자열을 숫자형으로 변형
+ parseInt("abc") #NaN 출력 * Not a Number
+ isNaN() 함수는 NaN인지 아닌지 판별 false면 number, true면 NaN임
+ &&(and), ||(or), ===(같다)

###  Searching For Elements
+ querySelector(".hello h1:first-child") #hello 클래스의 h1태그 찾기, 여러개 존재 시 첫번째 element만 가져옴 -> 모두 가져오고 싶으면 querySelectorAll()사용 #Array를 반환 
+ querySelector는 css selector를 사용하여 css로 검색 가능
+ querySelector("#hello") == Element.getElementsById("hello")
+ document.querySelector("#userForm #username") == document.getElementById("username"); #querySelector가 더 구체적이고, 제한적이다. id = "userForm"인 태그 속  id = "username"인 태그를 가져옴
+ Element.getElementsByClassName() #className태그의 텍스트 가져옴
+ Element.getElementsById() #Id의 텍스트 가져옴
+ Element.getElementsByTagName #div,h1같은 태그들의 텍스트를 불러옴


### event
ex)
<pre>
const title = document.querySelector(".hello h1:first-child")  

function handleTitleClick(){    
        title.style.color = "blue";  
}      

title.addEventListener("click",handleTitleClick); == title.onClick = handleTitleClick;  #클릭하면 함수 전달
title.addEventListener("mouseenter",handleTitleClick);
#마우스가 오면 함수 전달    
title.addEventListener("mouseleave",handleTitleClick);   #마우스가 떠나면 함수 전달 
</pre>
+ window.addEventListener("resize", 함수명) #윈도우 크기가 달라지면 함수 전달
+ window.addEventListener("copy", 함수명) #글을 카피하면 함수 전달
+ window.addEventListener("contextmenu", 함수명) #사용자가 요소를 마우스오른쪽 단추로 클릭해 메뉴를 열 때 발생

### CSS in Javascript
+ 조건문을 추가하여 이벤트 사용 가능  
+ css와 js파일 바로 연결하여 사용가능
+ classList: class들의 목록으로 작업 허용, 기존의 클래스네임이 조건문에 의해 없어질 수 있어 그때 사용
+ h1.classList.contain(A) #A라는 className이 리스트에 있는지 확인
+ h1.classList.remove(A) #A라는 className 삭제
+ h1.classList.add(A) #A라는 className 추가
+ h1.classList.toggle("A") #A라는 클래스가 있는 지 확인 후 제거 + 없다면 추가 #위 3개의 코드 합친 것과 같음
+ 창크기 조절하기 : inner 경우 창틀을 뺀 내용과 스크롤를 포함한 전체 윈도우 크기/ outer의 경우 창틀과 스크롤 모두 포함한 전체 크기

## 정리
+ JS에서 HTML에 액세스하기 위해 사용하는 객체는 document
+ document.querySelector(".home h1:first-child") # class="home"인 태그의 h1태그들 중 첫번째 요소(first-child)
+ className과 classList의 차이점: 
    + className는 모든 클래스를 교체하여 기존의 class가 없어짐
    + classList는 클래스 자체를 건드리지 않음. 클래스를 추가하고 삭제하는 방향으로 하여 기존 클래스를 유지
        + classList: 클래스들의 리스트, 1번 클래스 뒤 2번 클래스를 추가해서 속성을 덮어씌울 수 있고 제거해서 다시 1번 클래스로 돌아갈 수 있음
        + classList 메소드
            + Element.classList.add( "String" ) #클래스 값을 추가. 추가하려는 클래스가 엘리먼트의 class 속성에 이미 존재 시 무시
            + Element.classList.remove( "String" ) #지정한 클래스 제거
            + Element.classList.contains( "String") #지정한 클래스 값이 엘리먼트의 class 속성에 존재하는지 불리언 타입으로 확인
            + Element.classList.replace( "oldClass", "newClass" ) #존재하는 클래스를 새로운 클래스로 교체
 