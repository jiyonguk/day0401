import random

def makeNums():
    balls = [i for i in range(1,46)]

    random.shuffle(balls)


    return balls[0:6]

def input_display():
    moeny = int(input('금액을 입력하세요'))
    if moeny % 1000 != 0:
        print('try again')
        return input_display()
    else:
        return moeny / 1000

def main():
    count = input_display()
    for x in range(int(count)):
        nums = makeNums()
        print(sorted(nums))
    print('---------------------------')



if __name__ == "__main__":

    main()
