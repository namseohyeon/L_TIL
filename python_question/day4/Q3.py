class car():
    speed = 0
    def p(speed, name):
        print(name,"---> 현재의 속도(슈퍼 클래스): ", speed)

class sedan(car):
    # speed = 0
    def p(speed, name):
        print(name,"---> 현재의 속도(서브 클래스): ", speed)

class sonata(sedan):
    pass


car1 = car.p(200, "트럭")
car2 = sedan.p(150, "승용차")
car3 = sonata.p(150, "소나타")
