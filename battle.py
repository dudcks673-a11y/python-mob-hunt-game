class BattleManager:
    """
    플레이어와 몬스터의 전투를 관리하는 클래스
    """

    def is_monster_dead(self, monster):
        """
        몬스터의 HP가 0 이하인지 확인하여 사망 여부를 반환합니다.
        """
        return monster.hp <= 0

    def player_attack(self, player, monster):
        """
        플레이어가 몬스터를 공격하고 결과를 출력합니다.
        """
        # 플레이어 공격
        player.attack(monster)

        # 몬스터 생존 여부 확인
        if self.is_monster_dead(monster):
            print(f"{monster.name}을(를) 처치했습니다!")
        else:
            print(f"{monster.name}의 남은 HP: {monster.hp}")