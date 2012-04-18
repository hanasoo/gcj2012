#!/usr/bin/env python
# -*- coding: utf-8 -*-

FILE_NAME = 'A-small-attempt1'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

case_num = int(src.pop(0))
case_count = 0
result = ''

dic = {
	' ': ' ',
	'y': 'a',
	'q': 'z',
	'e': 'o',
}

sample_in = [
	'ejp mysljylc kd kxveddknmc re jsicpdrysi',
	'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
	'de kr kd eoya kw aej tysr re ujdr lkgc jv']
sample_out = [
	'our language is impossible to understand',
	'there are twenty six factorial possibilities',
	'so it is okay if you want to just give up'
	]

for i in range(3):
	for j in range(len(sample_in[i])):
		if sample_in[i][j] not in dic:
			dic[sample_in[i][j]] = sample_out[i][j]

def read(line):
	ans = ''
	for let in line:
		if let in dic:
			ans += dic[let]
		else:
			print "no idea with %s !!!!!" % let
			ans += '*'
	return ans

#print sorted(dic.keys())
#print sorted(dic.values())
dic['z'] = 'q'

result = ''
print('############ start #################')
for case_count in range(case_num):
	s = src.pop(0).strip()
	#print s
	ans = 'Case #%d: %s\n' % (case_count + 1, read(s))
	#print ans
	result += ans
print('############ end ###################')


f = open(OUT_FILE, 'w')
f.write(result)
f.close()