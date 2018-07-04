# -*- coding:utf-8 -*-

class FizzBuzz:
    def __init__(self, rules={}):
        self.rules = rules # {num:string, ...}
        # self.rules = sorted(rules.items()) # {num:string, ...}
    
    def fizzbuzz(self, x):
        # if x % self.num == 0:
        #     return self.rules[x]
        # else:
        #     return ""
        result = [ i[1] for i in sorted(self.rules.items()) if x % i[0] == 0]

    def add_rule(self, num, string):
        self.rules[num] = string # numの倍数の時stringを返す
        # self.rules = sorted(self.rules.items())

    def show(self, count): # count: 上限値
        # fizzbuzz = [str(i) for i in range(1, count + 1)]
        fizzbuzz = list(map(str, [ i for i in range(1, count + 1)]))

        print "\n".join(fizzbuzz)


def main():
    # "3の倍数ならFizz、5の倍数ならBuzz、両方とも当てはまるならFizzBuzzを返す

    # fizz = FizzBuzz(3, "Fizz")
    # buzz = FizzBuzz(5, "Buzz")
    #
    # for i in range(1, 31):
    #     result_string = ""
    #     result_string += fizz.is_fizzbuzz(i)
    #     result_string += buzz.is_fizzbuzz(i)
    #     
    #     if result_string == "":
    #         print i
    #     else:
    #         print result_string

    fizzbuzz = FizzBuzz({3:"Fizz", 5:"Buzz"});
    print fizzbuzz.rules
    fizzbuzz.show(31)
    print fizzbuzz.fizzbuzz(6)


if __name__ == "__main__":main()
