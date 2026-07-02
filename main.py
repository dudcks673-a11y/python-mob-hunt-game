from player import Player
from monster import blue_mushroom
from battle import BattleManager
from game import Game


def main():
    # 1. 플레이어, 몬스터, 배틀 매니저 객체 생성
    player = Player(name="용사🗡️", hp=100, attack_power=15, defense=5)
    monster = blue_mushroom
    battle_manager = BattleManager()
    
    # 2. Game 객체 생성 및 주입
    game = Game(player, monster, battle_manager)
    
    # 3. 게임 시작
    game.start()


if __name__ == "__main__":
    main()
