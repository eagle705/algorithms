# CommonPrimeDivisors

Check whether two numbers have the same prime divisors.

## Task description

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

- N = 15 and M = 75, the prime divisors are the same: {3, 5};
- N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
- N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
Write a function:

```python
def solution(A, B)
```

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

- Z is an integer within the range [1..6,000];
- each element of arrays A, B is an integer within the range [1..2,147,483,647].

## Solution

### First

* Programming language: Python
* Task score:
* Analysis
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    # A = [15, 10, 9, 12, 125]
    # B = [75, 30, 2, 42*3, 250]

    # A = [1,5125,12,2]
    # B = [1,2,24,2]
    
    # A = [6059, 551, 551]
    # B = [442307, 303601, 303601*551]
    
    
    # compute gcd
    def gcd(a, b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)
        
    res_count = 0    
    for i in range(len(A)):
        gcd_val = gcd(A[i], B[i])

        # check prime
        if A[i] > B[i]:
            check_val = A[i] // gcd_val
        else:
            check_val = B[i] // gcd_val
        
        # Sieve of Eratosthenes
        def get_prime_list(gcd_val):
            sieve = [True] * (gcd_val + 1) # 0번 인덱스 때문
            sieve[0] = False
            sieve[1] = False
            j = 2
            while(j * j < gcd_val): # 중간 넘어가면 dividers는 사라지기 때문
                if sieve[j]:
                    k = j*j
                    while(k < gcd_val):
                        sieve[k] = False
                        k += j
                j+=1
            prime_list = [num for k, num in enumerate(range(gcd_val+1)) if sieve[k] is True and gcd_val % num == 0]
            
            if len(prime_list) > 1:
                return prime_list[:-1]
            else:
                return prime_list
        
        gcd_val_prime_list = get_prime_list(gcd_val)
        check_val_prime_list = get_prime_list(check_val)
        
        pass_flag = True
        for _check_val in check_val_prime_list:
            if _check_val not in gcd_val_prime_list:
                pass_flag = False
                break


        # print("A[i]: {}, B[i]: {}".format(A[i], B[i]))   
        # print("gcd_val: ", gcd_val)
        # print("check_val:" , check_val)
        # print("gcd_val_prime_list: ", gcd_val_prime_list)
        # print("check_val_prime_list: ", check_val_prime_list)
        # print("pass_flag: ", pass_flag)
        # print("")
            
        if pass_flag is True:
            res_count += 1
    # print("res_count: ",res_count)
            
    return res_count
```


## Comment
아직까진 제대로 풀지 못했다 ㅠㅠ 뒤에 가면 집중력이 떨어지는 듯
