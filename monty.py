#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
__author__ = 'Haibo Yu' 

''' 
solve the Monty Hall problem by class
''' 

from thinkbayes import Pmf

class Monty(Pmf):
    def __init__(self, hypos):
        """Initialize self.
        hypos:sequence of hypotheses
        """
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()
        
    def Update(self, data):
        """Update each hypothesis based on the data.
        data:any representation of the data
        """
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()
        
    def Likelihood(self, data, hypo):
        """Compute the likelihood of the data under the hypothesis.
        hypo:string name of the door where the prize is
        data:string name of the door Monty opened
        """
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1
        
def main():
    hypos = 'ABC'
    pmf = Monty(hypos)
    
    data = 'B'
    pmf.Update(data)
    
    for hypo, prob in sorted(pmf.Items()):
        print hypo, prob
        
if __name__ == '__main__':
    main()