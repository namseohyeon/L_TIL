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
+ null: 값이 주어졌는데 값에 아무것도 없음
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
+ const ob = { # 안에 속성 작성
    name: "seohyeon",
    point: 10
}  
console.log(ob.point) #10 출력
+ ob.point = 20 # Objects안 속성 변경
+ ob.lastName = "nam" # Objects안 속성 추가