#!/usr/bin/env python
# -*- coding: utf-8 -*-

'cookie probability'

__author__ = 'Herbert Yu'

from thinkbayes import Pmf
"""---------------------------------------------------------------------------
使用曲奇饼问题来测试Pmf类
假设有2碗曲奇饼，碗1包含30个香草曲奇和10个巧克力曲奇，碗2有上述两种饼干各20个。
现在设想你在不看的情况下随机地挑一个碗拿一块饼，得到了一块香草曲奇饼，那么：
从碗1取到香草曲奇饼的概率是多少？
-----------------------------------------------------------------------------"""
pmf = Pmf()

pmf.Set('Bowl1', 0.5)
pmf.Set('Bowl2', 0.5)    #先验概率0.5（先验分布）

pmf.Mult('Bowl1', 0.75)
pmf.Mult('Bowl2', 0.5)   #碗1拿到曲奇的概率3/4，碗2为1/2，Mult将先验概率乘以已知的似然度。
    
pmf.Normalize()          #归一化。由于上述假设包含了全部情况，可以重新归一化。

print "The probability from Bowl1 is %f" %pmf.Prob('Bowl1')
print "The probability from Bowl2 is %f" %pmf.Prob('Bowl2')