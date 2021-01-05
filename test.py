#!/bin/python -B 

from tokenizer import tokenize

if __name__ == '__main__':
	code = """
		my_float = 12.5
		my_number = 12
		my_number_negative = -12
		my_name = "kuesji"

		my_array = []
		my_dict = {}
		my_function(){}
		my_class {}
		my_class_extended : my_class {}

		a = 12
		b = 24

		op_sum = a+b
		op_diff = a-b
		op_mul = a*b
		op_div = a/b
		op_mod = a%b

		op_and = a & b
		op_or = a | b
		op_xor = a ^ b
		op_not = !a

		op_multiple = (a+b) * (a-b) % (a % 2)

		cmp_greater = a > b
		cmp_lesser = a < b
		cmp_equal = a == b
		cmp_not_equal = a != b

		special_dot = dict.put("blabla","blabla")

		/* yeah this is a commet line */
		/* btw i can write
			multiline comment too
			( maybe after btw i should continued with 'i use arch'. )
		*/
	"""

	tokens = tokenize(code)
	for token in tokens:
		print(token)
