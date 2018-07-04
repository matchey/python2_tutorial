# -*- coding:utf-8 -*-
import sys

class FizzBuzz:
    """
    　 num:指定の数
    result:指定の数の倍数なら、この文字列を吐き出す

    使い方:

    第一引数がnumに格納され、第二引数がresultに格納される。
    >>> test = FizzBuzz(3,"Fizz")

    また、is_fizzbuzzメソッドを使うことにより、引数xがnumで割りきれる場合に、resultの文字列を返してくれる。
    
    >>> test.is_fizzbuzz(1)
    ''
    >>> test.is_fizzbuzz(2)
    ''
    >>> test.is_fizzbuzz(3)
    'fizz'
    """
    def __init__(self,num,string):
        self.num = num
        self.result = string
    
    def is_fizzbuzz(self,x):
        " 引数xがnumの倍数なら、resultの文字列を返す "
        if x % self.num == 0:
            return self.result
        else:
            return ""



def main():
    "3の倍数ならFizz、5の倍数ならBuzz、両方とも当てはまるならFizzBuzzを返す"
    argv = sys.argv
    #もし引数が無ければ、Usageを表示して終了
    if len(argv) < 2:
        print "usage:python fizzbuzz.py [number]"
        exit()

    fizz = FizzBuzz(3,"fizz")
    buzz = FizzBuzz(5,"buzz")

    for i in range(1,int(argv[1]) + 1):
        result_string = ""
        result_string += fizz.is_fizzbuzz(i)
        result_string += buzz.is_fizzbuzz(i)
        
        if result_string == "":
            print i
        else:
            print result_string


if __name__ == "__main__":main()
