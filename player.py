
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
        if monster.hp < 0:
            monster.hp = 0     
        print(f"{monster.name}에게 {damage}의 데미지를 입혔습니다! (남은 HP: {monster.hp})\n")

    def info(self):
        print(f"이름 : {self.name}")
        print(f"HP : {self.hp}")
        print(f"공격력 : {self.attack_power}")
        print(f"방어력 : {self.defense}")
        #수정 완료 
    
