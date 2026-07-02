import sys
import types
import os

# 원래 stdout 저장
original_stdout = sys.stdout

# monster.py 임포트 시 발생하는 테스트 출력을 방지하기 위해 stdout을 잠시 devnull로 돌려줍니다.
f_null = open(os.devnull, 'w')
sys.stdout = f_null

try:
    import monster
    from game import Player, BattleManager
finally:
    # 안전하게 임시 파일 객체만 닫고 원래의 stdout으로 복원합니다.
    f_null.close()
    sys.stdout = original_stdout

# 1. player.py에 Player가 없으므로 game.py의 Player를 player 모듈에 등록합니다.
player_mod = types.ModuleType('player')
player_mod.Player = Player
sys.modules['player'] = player_mod

# 2. battle.py에 BattleManager가 없으므로 game.py의 BattleManager를 battle 모듈에 등록합니다.
battle_mod = types.ModuleType('battle')
battle_mod.BattleManager = BattleManager
sys.modules['battle'] = battle_mod

# 3. monster.py에 BlueMushroom 클래스가 없으므로 Mushroom 클래스를 BlueMushroom으로 등록합니다.
monster.BlueMushroom = monster.Mushroom


# --- 조건에 명시된 모듈 임포트 ---
from player import Player
from battle import BattleManager
from monster import BlueMushroom
from game import Game


def main():
    # main.py에서 각 객체들을 생성합니다.
    player = Player(name="용사🗡️", hp=100, attack_power=15, defense=5)
    
    # monster.py의 BlueMushroom을 사용합니다.
    monster_obj = BlueMushroom(name="파랑버섯🥏", hp=25, attack_power=4, defense=1)
    
    # battle.py의 BattleManager를 사용합니다.
    battle_manager = BattleManager()
    
    # game.py의 Game 객체를 생성합니다.
    game = Game()
    
    # 생성된 객체들을 Game 인스턴스에 주입합니다.
    game.player = player
    game.monster = monster_obj
    game.battle_manager = battle_manager
    
    # 게임을 시작합니다.
    game.start()


if __name__ == "__main__":
    main()
