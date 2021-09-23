#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	return [max(li) for li in numbers]

def join_integers(numbers):
	pass
	return int("".join([str(n) for n in numbers]))

def generate_prime_numbers(limit):
	pre = []
	nbr = range(2,limit+1)
	while len(nbr) > 0:
		pre.append(nbr[0])
		p = nbr[0]
		nbr2 = []
		for nb in nbr:
			if (nb%p) != 0:
				nbr2.append(nb)
		nbr = nbr2
	return pre

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	li = []
	for stri in strings:
		for i in range(1,num_combinations):
			if(excluded_multiples is None):
				li.append(stri+str(i))
			elif i%excluded_multiples != 0:
				li.append(stri+str(i))
	
	return li

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
