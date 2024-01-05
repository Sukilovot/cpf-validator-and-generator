from sys import argv

# its 11 digits
valid_sum_of_cpf = [33, 44, 55, 66, 11, 12, 21, 22, 23, 23, 32, 33, 34, 43, 44, 45, 54, 55, 56, 65, 66, 67, 76, 77, 78, 87, 88]

def validate(cpf):
	original_cpf = cpf
	cpf = str(cpf).replace(".", "").replace("-", "")
	cpf_num = 0

	for i in range(0, 11):
		cpf_num += int(cpf[i])

	for num in valid_sum_of_cpf:
		if int(cpf_num) == num:
			return f"valid"
	return f"not valid"