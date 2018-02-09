#!-*-coding:utf8 -*-

import xmath

print '#import xmath'
print xmath.pi
print xmath.max(10, 5)
print xmath.sum(1,2,3,4,5)

print '#import xmath as math'
import xmath as math #將xmath取名為math
print math.e

print '#from xmath import min'
from xmath import min
print min(10, 5)