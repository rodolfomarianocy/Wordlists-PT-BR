import argparse, random

def main(output_list, cpf_numbers):
    cpf_lists = []
    if args.mode == "seq":
        cpfs = generate_cpfs_seq(cpf_numbers)
    elif args.mode == "rnd":
        cpfs = generate_cpfs_random(cpf_numbers)
    if (args.format == 1):
        for cpf in cpfs:
            cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
            cpf_lists.append(cpf)
    else:
        for cpf in cpfs:
            cpf_lists.append(cpf)
    print("[X] Wordlist being generated")
    create_wordlist(cpf_lists, args.output_list)
    print("[X] Wordlist generated successfully with " + str(cpf_numbers) + " CPFs")

def generate_cpfs_seq(cpf_numbers):
    cpfs = []
    for i in range(1, cpf_numbers+1):
        cpf_base = f'{i:09d}00'
        full_cpf = calc_check_digit(cpf_base)
        cpfs.append(full_cpf)
    return cpfs

def generate_cpfs_random(cpf_numbers):   
    cpfs = set()  
    while len(cpfs) < cpf_numbers:
        cpf = [random.randrange(10) for _ in range(9)]
        for _ in range(2):
            value = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
            cpf.append(11 - value if value > 1 else 0)
        cpfs.add("".join(map(str, cpf)))  
    return list(cpfs)

def calc_check_digit(cpf_base):
    def calc_digit(digits):
        sum = 0
        qtd_digits = len(digits)
        for i in range(qtd_digits):
            sum += int(digits[i]) * ((qtd_digits + 1) - i)
        result = 11 - sum % 11
        return result if result <= 9 else 0

    cpf_base = cpf_base[:-2]
    first_digit = calc_digit(cpf_base)
    cpf_base += str(first_digit)
    second_digit = calc_digit(cpf_base)
    cpf_base += str(second_digit)
    return cpf_base

def create_wordlist(cpf_lists, output_List):
    with open(output_list, "a") as my_file:
        for index, cpf in enumerate(cpf_lists):
            print(cpf)
            if index == len(cpf_lists) - 1:
                my_file.write(cpf)
            else:
                my_file.write(cpf + '\n')

def banner():
    print("""
 _____ _____ _____ _____                     _           
|     |  _  |   __|   __|___ ___ ___ ___ ___| |_ ___ ___ 
|   --|   __|   __|  |  | -_|   | -_|  _| .'|  _| . |  _|
|_____|__|  |__|  |_____|___|_|_|___|_| |__,|_| |___|_|  
""")
    
parser = argparse.ArgumentParser(description=banner())
parser.add_argument('-n', '--numbers', type=int, dest="cpf_numbers", help='Enter how many CPFs you want to generate', default=10)
parser.add_argument('-f', '--format', type=int, dest="format", help='0 = XXXXXXXXXXX, 1 = XXX.XXX.XXX-XX', default=0)
parser.add_argument('-o', '--output', type=str, dest="output_list", help='output.txt', default="cpfs.txt")
parser.add_argument('-m', '--mode', type=str, dest="mode", help='rnd = random, seq = sequential', default="rnd")

args = parser.parse_args()
output_list = args.output_list
cpf_numbers = args.cpf_numbers
main(output_list, cpf_numbers)