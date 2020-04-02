
class Menu:

    def __init__(self, n, p):
        self.name = n
        self.price = p

class Kiosk:

    def __init__(self, mlist):
        self.menu_list = mlist
        self.order_list = []

    def start_service(self):
        print("WELCOME.....")
        num = 1
        print("----------------------")
        for menu in self.menu_list:
            print(num, menu.name, menu.price)
            num += 1
        print("----------------------")
        choice = int(input('메뉴번호를 선택하세요, 0을 누르면 완료\n'))

        if choice == 0:
            return
        self.order_list.append(self.menu_list[choice -1])
        self.start_service()

    def print_bill(self):
        total = 0
        print('-------------')
        for order_menu in self.order_list:
            print(order_menu.name, order_menu.price)
            total += order_menu.price
        print('------------')
        print('TOTAL:', total)
        print('---------------')

class MainKiosk:

    def __init__(self, dic):
        self.kiosks = dic

    def service(self):
        print(self.kiosks)
        idx = int(input('0 ro 1'))
        kiosk = self.kiosks[idx]
        
kiosk1 = Kiosk([
            Menu('김밥',2000),
            Menu('라면',4000),
            Menu('쫄면',1000),
            Menu('떡라면',3000)
        ])
kiosk2 = Kiosk([
            Menu('봉골레',12000),
            Menu('까르보나라',10000),
            Menu('알리올리오',11000),
            Menu('크림치즈',13000)
        ])
mainKiosk = MainKiosk([kiosk1, kiosk2])

mainKiosk.service()



kiosk.start_service()
kiosk.print_bill()