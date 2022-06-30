

def word():
    for i in range(2,10):
        print("#  %d단  # " %i, end="")
    print()

def gugudan():
    for i in range(1,10):
        for j in range (2,10):
        # word()
            print("%dx %d= %2d  " %(j,i,i*j), end="")
        # print()
        print()


word()
gugudan()

