#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
codejam assist
 @hanasoo
"""

import optparse
import os
import sys

from decimal import *

class Solver:
	def __init__(self, case_num, src):
		self.case_num = case_num
		self.src = src

	def option1(self, current, total, probs):
		c_prob = reduce(lambda x, y: x * y, probs)
		expect = c_prob * (total - current + 1) + (1 - c_prob) * (total * 2 - current + 2)
		return expect

	def option2(self, current, total, probs):
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

	def option3(self, current, total, probs):
		expect = total + 2
		return expect

	def run(self):
		for i in range(self.case_num):
			current, total = [int(char) for char in self.src.pop(0).strip().split(' ')]
			probs = [Decimal(char) for char in self.src.pop(0).strip().split(' ')]
			ans = min([self.option1(current, total, probs),
				self.option2(current, total, probs), 
				self.option3(current, total, probs)])
			yield i, '%06f' % ans

def main ():
	# Option parser
	parser = optparse.OptionParser(usage='%prog [options] input_file')
	parser.add_option('-o', '--out_file',
		action = 'store', dest = 'out_file',
		help = 'Write output filename')
	parser.add_option('--base_dir',
		action = 'store', dest = 'base_dir',
		help = ('Path to base directory '))
	parser.set_defaults(base_dir = os.path.dirname(os.path.realpath(__file__)))
	options, args = parser.parse_args()

	if not len(args):
		raise Exception('need input-filename')

	in_file = args[0]
	out_file = options.out_file if options.out_file else in_file.replace('.in', '.out')
	print ('input file: %s' % in_file)
	print ('output file: %s\n' % out_file)

	# read file
	f = open(in_file, 'r')
	src = f.read().split('\n')
	f.close()

	case_num = int(src.pop(0))
	s = Solver(case_num, src)
	result = ''
	for case in s.run():
		num, ans = case
		ans = 'Case #{0}: {1}\n'.format(num + 1, ans)
		print ans
		result += ans

	# write file
	f = open(out_file, 'w')
	f.write(result)
	f.close()

if __name__ == '__main__':
	main()