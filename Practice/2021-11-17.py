"""
OOP - Inheritance and Subclass
"""

class Unit:
    def __init__(self, rank, size, life):
        self.name = self.__class__.__name__
        self.rank = rank
        self.size = size
        self.life = life

    def show_status(self):
        print('이름: {}'.format(self.name))
        print('등급: {}'.format(self.rank))
        print('샤이즈: {}'.format(self.size))
        print('라이프: {}'.format(self.life))

class Goblin(Unit):
    """
    class Unit의 subclass
    """
    def __init__(self, rank, size, life, attack_type, damage):
        super(Goblin, self).__init__(rank, size, life)
        # 부모에서 정의되지 않은 새로운 속성을 정의
        self.attack_type = attack_type
        self.damage = damage
                 
    def show_status(self):
        # print('이름: {}'.format(self.name))
        # print('등급: {}'.format(self.rank))
        # print('사이즈: {}'.format(self.size))
        # print('라이프: {}'.format(self.life))
        # 계속 반복하는 대신 super로 부모에서 정의된 함수 사용
        # method override의 예
        super(Goblin, self).show_status()
        print('공격 타입: {}'.format(self.attack_type))
        print('데미지: {}'.format(self.damage))

    def attack(self):
        print('[{}]이 공격합니다! 상대방 데미지({})'.format(self.name, self.damage))

class SphereGoblin(Goblin):
    def __init__(self, rank, size, life, attack_type, damage, sphere_type):
        # method override
        super(SphereGoblin, self).__init__(rank, size, life, attack_type, damage)
        self.sphere_type = sphere_type

    def show_status(self):
        super(SphereGoblin, self).show_status()
        print('창 타입: {}'.format(self.sphere_type))

class Hero(Unit):
    def __init__(self, rank, size, life, goblins = None):
        super(Hero, self).__init__(rank, size, life)
        if goblins is None:
            self.goblins = []
        else:
            self.goblins = goblins

    def show_own_goblins(self):
        num_of_goblins = len([x for x in self.goblins if isinstance(x, Goblin)])
        num_of_sphere_goblin = len([x for x in self.goblins if isinstance(x, SphereGoblin)])
        print('현재 영웅이 소유한 고블린은 {}명, 창 고블린은 {}명 입니다.'.format(num_of_goblins, num_of_sphere_goblin))

    def make_goblin_attack(self):
        for goblin in self.goblins:
            goblin.attack()

    def add_goblins(self, new_goblins):
        for goblin in new_goblins:
            if goblin not in self.goblins:
                self.goblins.append(goblin)
            else:
                print('이미 추가된 고블린입니다.')
    def remove_goblins(self, old_goblins):
        for goblin in old_goblins:
            try:
                self.goblins.remove(goblin)
            except:
                print('{}을 소유하고 있지 않습니다'.format(goblin))

# 고블린 오브젝트 생성
g1 = Goblin('Soldier', 'Small', 100, '근접 공격', 15)
g2 = Goblin('Soldier', 'Small', 100, '근접 공격', 15)
sphere_g1 = SphereGoblin('Soldier', 'Small', 100, '레인지 공격', 10, '긴 창')

# 영웅 오브젝트 생성 후, 고블린 오브젝트 할당
hero_1 = Hero('Hero', 'Big', 300, [g1, g2, sphere_g1])

g3 = Goblin('Soldier', 'Small', 100, '근접 공격', 20)
sphere_g2 = SphereGoblin('Soldier', 'Small', 100, '레인지 공격', 5, '긴 창')

print('# 새로운 고블린 추가 전')
hero_1.show_own_goblins()
hero_1.make_goblin_attack()

# 새로운 고블린 추가
hero_1.add_goblins([g3, sphere_g2])

print('\n # 새로운 고블린 추가 후')
hero_1.show_own_goblins()
hero_1.make_goblin_attack()

# 추가한 고블린 삭제
hero_1.remove_goblins([g3, sphere_g2])

print('\n # 추가 한 고블린 삭제 후')
hero_1.show_own_goblins()
hero_1.make_goblin_attack()

# 영웅에게 소유되지 않은 고블린 생성
g4 = Goblin('Soldier', 'Small', 100, '근접 공격', 20)

# 이미 소유한 고블린 추가
print('\n # 에러 메세지 발생')
hero_1.add_goblins([g1])
hero_1.remove_goblins(g4)