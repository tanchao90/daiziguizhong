# -*- coding:utf-8 -*-

import itertools
import time

# 说明
# 用是个元素的list代表五角星
# list中每个元素代表其中一个点，下图是list下标和五角星点的对应关系
# -----0-----
# 1--2---3--4
# --5-----6--
# -----7-----
# -8-------9-


def add_pentagram(pentagram_dict, permutation):
	"""在所有的全排列中，每个五角星都会重复五次
	通过旋转五角星，确定同构五角星，排除结果中的重复值
	"""
	# 旋转顺序
	rotate_outside = [0, 1, 8, 9, 4, 0]
	rotate_inside = [3, 2, 5, 7, 6, 3]

	for x in xrange(0, len(rotate_outside)-1):
		new_permutation = list(permutation)
		for index in range(1, len(rotate_outside)):
			new_permutation[rotate_outside[index-1]] = permutation[rotate_outside[index]]
			new_permutation[rotate_inside[index-1]] = permutation[rotate_inside[index]]
		str_pentagram = ''.join(str(num) for num in new_permutation)
		if str_pentagram in pentagram_dict:
			return False
		permutation = new_permutation

	pentagram_dict[str_pentagram] = permutation
	return True

def is_valid(permutation):
	lines = [
		[0, 2, 5, 8],
		[0, 3, 6, 9],
		[1, 2, 3, 4],
		[1, 5, 7, 9],
		[4, 6, 7, 8]
	]
	pre_sum = 0
	for index in lines[0]:
		pre_sum += permutation[index]
	for line in lines[1:]:
		cur_sum = 0
		for index in line:
			cur_sum += permutation[index]
		if cur_sum != pre_sum:
			return False
	return True

def pentagram(seq):
	print '*'*20
	print 'seq:', seq
	count = 0
	pentagram_dict = {}
	start_time = time.time()
	for each_permutation in itertools.permutations(seq, len(seq)):
		count += 1
		if is_valid(each_permutation):
			add_pentagram(pentagram_dict, each_permutation)

	print 'valid result:'
	for key, value in pentagram_dict.iteritems():
		print key, ':', value

	print 'count:', count # 10!=3628800
	print 'valid_count:', len(pentagram_dict)
	print 'cost time:', time.time() - start_time
	print ''

if __name__ == "__main__" :
	pentagram([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	pentagram([1,2,3,4,5,6,7,7,7,8])
	pentagram([1,2,3,4,5,6,8,9,10,12])