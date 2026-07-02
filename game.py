from player import Player
from monster import blue_mushroom
from battle import BattleManager


class Game:
    def __init__(self, player, monster, battle_manager):
        # Game 클래스는 player, monster, battle_manager를 가집니다.
        # 파라미터가 제공되면 주입받아 사용하고, 없을 경우 monster.py 등의 기본 객체명을 준수하여 매핑합니다.
        self.player = player
        self.monster = monster
        self.battle_manager = battle_manager

    def show_menu(self):
        # 메뉴는 다음과 같이 정확히 출력합니다.
        print("1. 공격하기")
        print("2. 플레이어 정보 보기")
        print("3. 몬스터 정보 보기")
        print("4. 종료")

    def start(self):
        # start() 메서드에서 while 반복문으로 메뉴를 실행합니다.
        while True:
            self.show_menu()
            try:
                choice = input("선택: ").strip()
            except (KeyboardInterrupt, EOFError):
                break

            if choice == "1":
                # 사용자가 1을 입력하면 플레이어가 몬스터를 공격합니다.
                self.battle_manager.player_attack(self.player, self.monster)
                
                # 몬스터 HP가 0(이하)이면 게임을 종료합니다.
                if self.monster.hp <= 0:
                    break
            elif choice == "2":
                self.player.info()
            elif choice == "3":
                self.monster.info()
            elif choice == "4":
                break
