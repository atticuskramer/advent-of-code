full_input = """1-0-0020
1=0---1=1=201
10=02-0=1
1-12-=111201-1212
110=-222=0201=
10--2=20
2=12=-02222021=02-
1-1-1=-1
2=2=2--00-2121=02-1
201-1-210-
1212-11=
2=---10
2=1-02200001211
1===1-2==2-1
10=--=-=00
22-0=
2==0-1022=02
11221=-==-1-20-0
100
10-=22===1=00=0
2=0
1=1=0101=20
2--0=02-11021-
1222011-2--2=
22
20==00=122
2=1-010
20-=222-=2-1002-2
2=
122==01==12202-=
120202
2112=2-0202-12-02
1-=
11=
1101-1==2--
1=0=00=2=0-=02
1021--
1=02-=201122-=12-1
1==0=200=02=2=-2=22
1=21=10211-2222
21-0
1==21=
12=-220002-1=-21=2
1100-=-
1201=02=-111=00-0=
10=-=0122100==1--2
21=-12
10=21-0-2-200022
2102=-2--=1-2=2-1
1=1211101
2002=02--===
1200-
11--20-=-
10-20-0
1=2=
20100-22-0
12==-1
22=0011
2-200222=1121
201-2-=2==00-
1=-=0=--0===2
21=----2==020
1=1-20-=1=-02-2--2=
21
1=202110111=000
2-22-002=
10=1-001
1-002-221000=02
2==---1-0
1012=0--=00--10
1-2=21-2
1=1
11-
1-10--122-12
20
1==
2010=-2-2==2=--
1=11=
10-=
1=-=2--2-110=100
100==--01==
1-1-20=--1-2-0212
20-1001002-
2=1-
1==-2-0-102=-
1-1
12-1-0=2=-22--=10
10=21-02--=-=22
110210-12210--1-=-
1==1--2=21
1-0200=2-2-
22==-00=-
1-=2=-20-202=20111
2=0=-1=
1=-212=1=2
10-220=02
100-
1==02=0021
10=-1222-
1-212==
12-012=
1-0-102-1=-=-01=1-=1
1-
11211
2-0
1=0=
1=0=111000--=12=1
1-1-011==0102-
2==02202=2-=2
11---01-=--=2-02
1==0120-01=0-=0
1=-=2=1-=0=0==212=
212211110=
1=20101-==1"""

test_input = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""

snafu_dict = {'=' : -2, '-' : -1, '0' : 0, '1' : 1, '2' : 2}
rev_snafu_dict = {value : key for key, value in snafu_dict.items()}

# Snafu's will always be represented as a list of single character strings

def snafu_to_decimal(snafu):
    total = 0
    for i, char in enumerate(reversed(snafu)):
        total += (5 ** i) * snafu_dict[char]
    return total
    
def decimal_to_base_n_str(num, n):
    if n <= 1:
        raise ValueError
    result_str = ''
    divisor = 1
    while num // (divisor * n) > 0:
        divisor *= n
    while divisor > 0:
        result_str += str(num // divisor)
        num = num % divisor
        divisor //= n
    return result_str

# Returns a NEW snafu list that is one greater than the input    
def snafu_increment(snafu):
    num = snafu_dict[snafu[-1]]
    num += 1
    if num > 2:
        if len(snafu) > 1:
            return snafu_increment(snafu[:-1]) + ['=']
        else:
            return ['1', '=']
    else:
        return snafu[:-1] + [rev_snafu_dict[num]]
    
def base_5_to_snafu(b5_str):
    snafu = ['0'] + list(b5_str)
    for i, num in enumerate(snafu):
        # These literals are probably bad practice. It would probably just be
        # best to rethink/enhance the snafu dictionaries instead
        if num == '3':
            snafu[i] = '='
            snafu[:i] = snafu_increment(snafu[:i])
        elif num =='4':
            snafu[i] = '-'
            snafu[:i] = snafu_increment(snafu[:i])
    if snafu[0] == '0':
        return snafu[1:]
    else:
        return snafu
            
    
def decimal_to_snafu(num):
    b5_num = decimal_to_base_n_str(num, 5)
    return base_5_to_snafu(b5_num)
        
    
def sum_snafus(snafus_str):
    total = 0
    for snafu in map(list, snafus_str.split('\n')):
        total += snafu_to_decimal(snafu)
    return total
    
def part_1(input_str):
    return ''.join(decimal_to_snafu(sum_snafus(input_str)))
    
# print(sum_snafus(test_input))
# print(decimal_to_base_n_str(100, 2))
# print(decimal_to_base_n_str(256, 2))
# print(decimal_to_base_n_str(14, 2))
# print(decimal_to_base_n_str(1, 2))
# print(decimal_to_base_n_str(4890, 5))
# print(decimal_to_snafu(4890))
# print(snafu_increment(['2','=','-','2','2','2']))

print(part_1(test_input))
print(part_1(full_input))