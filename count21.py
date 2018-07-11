# -*- coding:utf-8 -*-

import random

class Count21:
    def __init__(self, seq, total):
        if(seq < 1): seq = 1
        if(total < 1): total = 1
        self.seq = seq # 一度に言える数の最大値(最小値は1)
        self.total = total # totalを言った方の負け
        self.opt_begin = 0 # CPU何手目から最善手で打つか
        self.strategies = range((total - 1) % (seq + 1), total, seq+1) # 勝つために言うべき数

    def level(self, level):
        if(level < 1): level = 1
        if(level > 5): level = 5
        self.opt_begin = self.total * (1 - (level-1)/4.0)

    def play(self):
        print("先手か後手かを選んでください．")
        turn = input("先手:0, 後手:1 => ")
        if(turn < 0 or turn > 1): turn = 0
        optimum = False # CPUが最善手を打つかどうか
        last = 0
        while(last < self.total):
            says_min = last + 1
            says_max = last + self.seq
            if(says_max > self.total): says_max = self.total

            if((not optimum) and last > self.opt_begin): optimum = True

            if(turn):
                if optimum and self._optimazation(last):
                    says = self._optimazation(last)[0]
                else:
                    says = random.randint(says_min, says_max)
                print "CPU:",
            else:
                says = input(str(says_min) + "~" + str(says_max) + "の数を入力してください: ")
                if(says < says_min): says = says_min
                if(says > says_max): says = says_max
                print "You:",

            print ", ".join(map(str, range(says_min, says+1)))
            last = says
            turn = not turn

        if(turn):
            print("You LOSE")
        else:
            print("You WIN")

    def _optimazation(self, last):
        return filter(lambda x: last < x and x < last + self.seq + 1, self.strategies)

def main():
    # 連続した数字を数字を交互に入力(3つまで)，21を言った方の負け
    count21 = Count21(3, 21)
    print("~~~21を言ったら負けゲーム~~~")
    print("CPUのレベルを5段階で設定します")
    level = input("Input 1(最弱) ~ 5(最強) : ")
    count21.level(level) # 難易度を設定
    count21.play()

if __name__ == "__main__":main()
