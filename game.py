import os
import sys

# monster.py 임포트 시 발생하는 테스트 출력을 방지하기 위해 stdout을 잠시 devnull로 돌려줍니다.
try:
    sys.stdout = open(os.devnull, 'w')
    from monster import Mushroom
finally:
    sys.stdout.close()
    sys.stdout = sys.__stdout__


class Player:
    def __init__(self, name="용사🗡️", hp=100, attack_power=15, defense=5):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power
        self.defense = defense

    def info(self):
        print("\n--- 플레이어 정보 ---")
        print(f"이름 : {self.name}")
        print(f"HP : {self.hp}/{self.max_hp}")
        print(f"공격력 : {self.attack_power}")
        print(f"방어력 : {self.defense}")
        print("---------------------")


class BattleManager:
    def attack(self, attacker, defender):
        # 공격력 - 방어력 계산 (최소 1 데미지 보장)
        damage = max(1, attacker.attack_power - defender.defense)
        defender.hp -= damage
        if defender.hp < 0:
            defender.hp = 0

        print(f"\n⚔️  {attacker.name}이(가) {defender.name}을(를) 공격했습니다!")
        print(f"💥 {damage}의 데미지를 입혔습니다.")
        print(f"📊 {defender.name}의 남은 HP: {defender.hp}")


class Game:
    def __init__(self):
        # player, monster, battle_manager를 설정합니다.
        self.player = Player(name="용사🗡️", hp=100, attack_power=15, defense=5)
        # monster.py의 Mushroom을 임포트해서 몬스터를 초기화합니다.
        self.monster = Mushroom(name="주황버섯🍄", hp=40, attack_power=8, defense=2)
        self.battle_manager = BattleManager()

    def show_menu(self):
        print("\n1. 공격하기")
        print("2. 플레이어 정보 보기")
        print("3. 몬스터 정보 보기")
        print("4. 종료")

    def start(self):
        print("🎮 몹 잡기 게임을 시작합니다!")
        while True:
            self.show_menu()
            try:
                choice = input("선택: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n게임을 종료합니다.")
                break

            if choice == "1":
                self.battle_manager.attack(self.player, self.monster)
                if self.monster.hp <= 0:
                    print(f"\n🎉 {self.monster.name}을(를) 처치했습니다! 게임을 종료합니다.")
                    break
            elif choice == "2":
                self.player.info()
            elif choice == "3":
                print("\n--- 몬스터 정보 ---")
                self.monster.info()
                print("-------------------")
            elif choice == "4":
                print("게임을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 1~4 사이의 번호를 선택해주세요.")


if __name__ == "__main__":
    game = Game()
    game.start()