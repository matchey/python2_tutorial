# -*- coding:utf-8 -*-

class FizzBuzz:
    def __init__(self, rules={}):
        self.rules = rules # {num:string, ...}
    
    def add_rule(self, num, string):
        self.rules[num] = string # numの倍数の時stringを返す

    def show(self, count): # count: 上限値
        fizzbuzz = list(map(self._fizzbuzz, [ i for i in range(1, count + 1)]))
        print "\n".join(fizzbuzz)

    def _fizzbuzz(self, x):
        result = [ i[1] for i in sorted(self.rules.items()) if x % i[0] == 0]
        return "".join(result) if result else str(x)

def main():
    # 3の倍数ならFizz、5の倍数ならBuzz、両方とも当てはまるならFizzBuzzを返す
    fizzbuzz = FizzBuzz({3:"Fizz", 5:"Buzz"})
    # fizzbuzz.add_rule(2, "Pooh") # 2の倍数のときにPooh
    fizzbuzz.show(31)

if __name__ == "__main__":main()
