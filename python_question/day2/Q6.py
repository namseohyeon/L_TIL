animal_dict = {'닭':'병아리', '개':'강아지', '곰':'능소니','고등어':'고아기', '명태':'노가리', '말':'망아지', '호랑이':'개호주'}

while(True):
    #딕셔너리.keys() 앞에 list를 넣지 않으면 dict_keys([,,,,,]) 이런 형식으로 출력됨 -> 그래서 list를 앞에 적어준다. 
    animal=input(str(list(animal_dict.keys()))+"중 새끼 이름을 알 수 싶은 동물은? ")
    if animal in animal_dict:
        print("<%s>의 새끼는 <%s> 입니다" %(animal,animal_dict.get(animal)))
    else:
        print("그런 동물은 없습니다.")