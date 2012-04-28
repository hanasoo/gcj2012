#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *

FILE_NAME = 'sample'
FILE_NAME = 'A-small-attempt0'
FILE_NAME = 'A-large'

IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

case_num = int(src.pop(0))
case_count = 0
result = ''

def option1(current, total, probs):
	c_prob = reduce(lambda x, y: x * y, probs)
	expect = c_prob * (total - current + 1) + (1 - c_prob) * (total * 2 - current + 2)
	return expect

def option2(current, total, probs):
	print '### try go back all'
	expect = current + total + 1
	c_prob = probs.pop(0)
	for i in range(current - 1, 0, -1):
		print '### try go back %d, %f' % (i, c_prob)
		c_ex = i * 2 + total - current + 1
		e = c_prob * c_ex + (1-c_prob) * (c_ex + total + 1)
		c_prob *= probs.pop(0)
		expect = min(expect, e)
	return expect

def option3(current, total, probs):
	expect = total + 2
	return expect

print('############ start #################')
for case_count in range(case_num):
	current, total = [int(char) for char in src.pop(0).strip().split(' ')]
	probs = [Decimal(char) for char in src.pop(0).strip().split(' ')]
	print 'start %s %s %s' % (current, total, probs)
	ans = min([option1(current, total, probs), option2(current, total, probs), option3(current, total, probs)])
	ans = 'Case #%d: %06f\n' % (case_count + 1, ans)
	print ans
	result += ans
print('############ end ###################')


f = open(OUT_FILE, 'w')
f.write(result)
f.close()