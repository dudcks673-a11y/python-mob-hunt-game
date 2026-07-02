class Player:
    def __init__(self, name, hp, attack_power, defense):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, monster):
        print(f"{self.name}의 공격!")
        
        # 데미지 계산: 플레이어 공격력 - 몬스터 방어력
        damage = self.attack_power - monster.defense
        
        # 데미지가 1보다 작으면 최소 1로 처리
        if damage < 1:
            damage = 1
            
        # 몬스터 체력 감소
        monster.hp -= damage
        
        print(f"{monster.name}에게 {damage}의 데미지를 입혔습니다! (남은 HP: {monster.hp})\n")

    def info(self):
        print(f"이름 : {self.name}")
        print(f"HP : {self.hp}")
        print(f"공격력 : {self.attack_power}")
        print(f"방어력 : {self.defense}")
    
class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, hp=70, attack_power=18, defense=3)
        self.job = "도적"

    def info(self):
        print(f"[{self.job}]")
        super().info()

 # pyrefly: ignore [parse-error]
 class Warrior(Player):
    def __init__(self, name):
        # 전사 세팅: 높은 체력과 방어력, 낮은 공격력
        super().__init__(name, hp=120, attack_power=8, defense=10)
        self.job = "전사"

    def info(self):
        print(f"[{self.job}]")
        super().info()