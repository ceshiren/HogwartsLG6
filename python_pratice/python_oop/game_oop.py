# -*- coding: utf-8 -*-
# @Author : feier
# @File : game_oop.py
'''
一个回合制游戏，每个角色都有 hp 和 power，hp 代表血量，power 代表攻击力，hp 的初始值为 1000，power 的初始值为 200。
定义一个 fight 方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个 hp 进行对比，血量剩余多的人获胜
'''
from python_pratice.python_oop.log_decorator import log_decorator


class Game:
    # def __init__(self):
    #     # 初始化属性
    #     self.my_hp = 1000
    #     self.my_power = 200
    #     self.enemy_hp = 1000
    #     self.enemy_power = 199

    def __init__(self, my_hp, enemy_hp):
        # 初始化属性
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 199
        # 定义私有属性
        self.__secret = "secret"

    # 对打方法
    @log_decorator
    def fight(self):
        while True:
            # 我的剩余血量
            self.my_hp = self.my_hp - self.enemy_power
            # 敌人的剩余血量
            self.enemy_hp -= self.my_power
            print(f"我的血量：{self.my_hp} VS 敌人血量：{self.enemy_hp}")
            # 胜负判断
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break

    # 定义休息方法
    def rest(self, time_num):
        self.__private_method()
        print(f"太累了，休息 {time_num} 分钟")

    # 定义私有方法
    def __private_method(self):
        print(self.__secret)
        print("这是一个私有方法")


if __name__ == '__main__':
    game = Game(1000, 1100)
    # game.rest(3)
    game.fight()
    # 私有变量和私有方法不能通过对象直接去调用
    # print(game.__secret)
    # game.__private_method()
