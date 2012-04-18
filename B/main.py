#!/usr/bin/env python
# -*- coding: utf-8 -*-

FILE_NAME = 'B-large'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

case_num = int(src.pop(0))
case_count = 0
result = ''

#returns "got better than p" and "was suprising"
def judge(score, p, can_be_sup):
	is_best = False
	is_sup = False
	tri = [score / 3, score / 3, score / 3]
	tri[0] += 1 if score % 3 > 0 else 0
	tri[1] += 1 if score % 3 > 1 else 0
	if max(tri) >= p:
		is_best = True
	elif can_be_sup:
		if score % 3 == 1:
			pass
			#Case 13 => [5 4 4], [5 5 3] no chance
		elif max(tri) != 0 and max(tri) + 1 >= p:
			#Case 15 => [5 5 5], [6 5 4]
			#Case 14 => [5 5 4], [6 4 4]
			is_best = is_sup = True
	print "%s %s" % (tri, '(*)' if is_sup else '')
	return is_best, is_sup

print('############ start #################')
for case_count in range(case_num):
	s = src.pop(0).strip().split(' ')
	num = int(s.pop(0))
	sup = int(s.pop(0))
	p = int(s.pop(0))
	scores = [int(score) for score in s]

	ans = 0
	for score in scores:
		#print score, p, sup
		#print judge(score, p, sup)
		is_best, is_sup = judge(score, p, sup)
		if is_best:
			ans += 1
		if is_sup:
			sup -= 1
	print s
	ans = 'Case #%d: %d\n' % (case_count + 1, ans)
	print ans
	result += ans
print('############ end ###################')



f = open(OUT_FILE, 'w')
f.write(result)
f.close()