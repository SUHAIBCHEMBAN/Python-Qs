
# Q No 1 Find_max

def Find_max(num_list):
    max_number = max(num_list)
    return max_number

num_list = [4,2,3,6,7,8]
result = Find_max(num_list)
print(f"\nMax-Value = {result}")
  
# Q No 2 string_revers

def revers_string(words):
    return words[::-1]

words = "Hello World"
result = revers_string(words)
print(f"\nString After Reversing: {result}")


# Q No 3 Sort_acceding

def Sort_acceding(sortlist):
    return sorted(sortlist)

sortlist = [4,3,6,2,5,7,8,1]
result = Sort_acceding(sortlist)
print(f'\nAfter Sorting = {result}')

# Q No 4 Sum_even

def Sum_even(sumnum):
    sum = 0
    for i in range(1,sumnum + 1):
        if i % 2 == 0:
            sum = sum + i
    return sum

# sumnum = int(input("Enter a Number"))        
sumnum = 5
result = Sum_even(sumnum)
print(f"\nSum = {result}")


# Q No 5 check prime

def check_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

# num = int(input("Enter a Number"))
num = 5    
result = check_prime(num)
print(f"\nPrim {result}")

# Q No 6 second largest

def second_large(list_second):
    second = sorted(list_second)
    return second[-2]

list_second = [9,4,3,2,6,5]
result = second_large(list_second)
print(f"\nSecond largest Number in List = {result}")

# Q No 7 remove_duplicate

def remove_duplicate(dup_list):
    remove = set(dup_list)
    return list(remove)

dup_list = [11,2,1,11,5,4,2]
result = remove_duplicate(dup_list)
print(f"\nAfter removing = {result}")

# Q No 8 calculate sum

def calculate_sum(sumlist):
    return sum(sumlist)

sumlist = [1,2,3,4,5]    
result = calculate_sum(sumlist)
print(f"\nSum = {result}")

# Q No 9 genarate prime

def generate_prime(limit):
    prime = []
    for limit in range(2,limit):
        count = 1
        for i in range(2,limit):
            if limit % i == 0:
               count = 0
               break
        if count == 1:
            prime.append(limit)
    return prime
    
limit = 10
result = generate_prime(limit)
print(f"\nPrimelist :{result}")


# Q No 10  min & max

list_max_min = [4,3,6,8,2,5]
print(f"\nMax Value = {max(list_max_min)}")
print(f"Min Value = {min(list_max_min)}")

#  Q No 11  factorial

def factorial(num):
    fact = 1
    for i in range(1,num + 1):
        fact *= i
    return  fact

num = 5
result = factorial(num)    
print(f"\nFactorial = {result}")

# Q No 12 palidroma

def palidroma(words):
    size = len(words)
    for i in range(size // 2):
        if words[i] != words[size - 1 - i]:
            return False
    return True

words = 'malayalam'    
result = palidroma(words)
print(f"\nWord is {result}")


# Q No 13 Armstrong


def armstrong(num):
    str_num = str(num)
    size = len(str_num )
    sum =0

    for i in str_num:
        sum += int(i) ** size
        if num == sum:
            return True
    return False    

num = 153
result = armstrong(num)    
print(f"\nAmstrong {result}")


# Q No 14 fibonacci

def fibonacci_series(limit):
        a, b = 0, 1
        while a + b <= limit:
                c = a + b
                a, b = b, c
fibonacci_series(50)
print("\n0 1 1 2 3 5 8 13 21 34")


# Q No 15 prime_sum

def sum_prime(limit):
    sum = 0
    for i in range(2,limit + 1):
        is_prime = True
        for j in range(2,i):
            if i % j == 0:
                is_prime = False

        if is_prime:
            sum = sum + i         
    return sum            

                    
limit = 5
result = sum_prime(limit)
print(f"\nSum of prime numbers {result}")

# Q No 16 multiple_sum

def find_multiple(num):
    if num < 3:
        return 0
    sum = 0
    for i in range(3,num):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    return sum

num = 15
result = find_multiple(num)        
print(f"\nSum of Multiple of 3 and 5 = {result}")

# Q No 17 find_odd

def fin_ofodd(odnum):
    sum = 0
    for i in range(odnum):
        if i % 2 == 0:
            sum += i
    return sum

odnum = 10
result = fin_ofodd(odnum)
print(f"\nTotal Sum = {result}")


# Q No 18 union_lst

def union_list(lts1,lts2):
    set1 = set(lts1)
    set2 = set(lts2)
    union_set = set1.union(set2)
    union_list = list(union_set)
    return union_list  

lts1 = [1,2,3,4]
lts2 = [3,4,5,6]
final = union_list(lts1,lts2)
print(f"\nFianl Result of Union List : {final}")


# Q No 19  limit_sum

def sum_of_limit(lmt):
    num_str = str(lmt)
    sum = 0
    for i in num_str:
        sum += int(i)
    return sum

lmt = 151
result = sum_of_limit(lmt)    
print(f"\nResult is : {result}")

# Q No 20 vowel

def check_vowel(word):
    vwl = 'aeiouAEIOU'
    count = 0
    for i in word:
        if i in vwl:
            count += 1
    return count    

word = 'i am a boy'
result = check_vowel(word)
print(f"\nCount of Vowels : {result}")




















