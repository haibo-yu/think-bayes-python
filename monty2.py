#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
__author__ = 'Haibo Yu' 

''' 
solve the Monty Hall problem by Suite class
''' 

from thinkbayes import Suite

class Monty(Suite):
    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1

def main():
    suite = Monty('ABC')
    suite.Update('B')
    suite.Print()
    
if __name__ == '__main__':
    main()