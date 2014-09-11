#Think Python exercise 7.4

#evaluation loop

import math

def eval_loop():
	evaluated = False
	while True:
		user_input = raw_input("write what you'd like me to evaluate: ")
		if user_input == 'done':
			break
		evaluated = eval(user_input)
		print evaluated

	return evaluated

print (eval_loop())