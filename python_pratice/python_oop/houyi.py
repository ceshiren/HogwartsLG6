# -*- coding: utf-8 -*-
# @Author : feier
# @File : houyi.py
from python_pratice.python_oop.game_oop import Game
# 快速导包：Alt + enter
'''
后裔，后裔继承了 Game 的 hp 和 power。并多了护甲属性。
重新定义另外一个 defense 属性：
final_hp = hp + defense - enemy_power
enemy_final_hp = enemy_hp - power
两个 hp 进行对比，血量先为零的人输掉比赛
'''

class HouYi(Game):

    def __init__(self, my_hp, enemy_hp):
        self.defense = 100
        # 继承父类的构造方法
        super().__init__(my_hp, enemy_hp)

    def fight(self):
        # 改造一下 my_hp 的计算方式
        while True:
            # 我的剩余血量
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            # 敌人的剩余血量
            self.enemy_hp -= self.my_power
            print(f"我的血量：{self.my_hp} VS 敌人血量：{self.enemy_hp}")
            # self.rest(3)
            # 胜负判断
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break
        super().__private_method()


if __name__ == '__main__':
    houyi = HouYi(1000, 1100)
    # 子类对象可以直接调用父类的属性和方法
    print(houyi.my_power)
    houyi.fight()
    # houyi.rest(3)
    # 演示命令行上传
