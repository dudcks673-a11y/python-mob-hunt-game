class Mob:
    def __init__(self, name, hp, attack_power, defense):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense

    def attack(self):
        print(f"{self.name}의 스킬 발동.")
        print("공격했습니다.")

    def info(self):
        print(f"이름 : {self.name}")
        print(f"HP : {self.hp}")
        print(f"공격력 : {self.attack_power}")
        print(f"방어력 : {self.defense}")

class Mushroom(Mob):
    def run(self):
        print(f"{self.name}: 달리기")

    def jump(self):
        print(f"{self.name}: 점프")

class Slime(Mob):
    def __init__(self, name, hp, attack_power, defense, count=1):
        super().__init__(name, hp, attack_power, defense)
        self.count = count

    def split(self):
        self.count *= 2
        print(f"{self.name}이(가) 분열했습니다! 현재 개체 수 : {self.count}")

blue_mushroom = Mushroom("파랑버섯🥏:", 25, 4, 1)
red_mushroom = Mushroom("빨간버섯🍄:", 50, 8, 2)

blue_slime = Slime("파랑슬라임🌀:", 20, 3, 1)
red_slime = Slime("빨간슬라임🐙:", 40, 6, 2)

