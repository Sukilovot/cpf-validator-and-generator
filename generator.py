from validator import validate
import random

def generate():
    while True:
        cpf = []
        cpf_txt = ""

        for i in range(0, 11):
            cpf.append(str(random.randint(0, 9)))

        for num in cpf:
            cpf_txt = cpf_txt + num

        if str(validate(cpf_txt)) == "valid":
            return cpf_txt

print(generate())
