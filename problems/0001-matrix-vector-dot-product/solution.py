def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	n_col_a = len(a)
	length_b = len(b)
	if n_col_a != length_b:
		return -1
	product = []
	for row in a:
		product_ele = 0
		for i, ele in enumerate(row):
			product_ele += ele * b[i]
		product.append(product_ele)
	return product
