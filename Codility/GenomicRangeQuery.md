# GenomicRangeQuery

Find the minimal nucleotide from a range of sequence DNA.

## Task description

A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

* The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
* The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
* The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:

```java
class Solution { public int[] solution(String S, int[] P, int[] Q); }
```

that, given a non-empty zero-indexed string S consisting of N characters and two non-empty zero-indexed arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

The sequence should be returned as:

* a Results structure (in C), or
* a vector of integers (in C++), or
* a Results record (in Pascal), or
* an array of integers (in any other programming language).

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.

Assume that:

* N is an integer within the range [1..100,000];
* M is an integer within the range [1..50,000];
* each element of arrays P, Q is an integer within the range [0..N − 1];
* P[K] ≤ Q[K], where 0 ≤ K < M;
* string S consists only of upper-case English letters A, C, G, T.

Complexity:

* expected worst-case time complexity is O(N+M);
* expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

## Solution

### First

* Programming language: Python
* Task score:
* Analysis
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    letter_to_score = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4}

    len_arr = len(P)

    if len(set(S)) == 1:
        return [letter_to_score[S[0]]] * len_arr

    # score_S = [letter_to_score[char] for char in S]

    list_of_save_min_by_pos = []
    list_of_res = []
    for i in range(len_arr):
        start_idx = P[i]
        end_idx = Q[i]
        min_score = 9999

        for saved_start_idx, saved_end_idx in list_of_save_min_by_pos:
            if  start_idx <= saved_start_idx and saved_end_idx <= end_idx:
                min_score = 1
                break
        if min_score == 1:
            list_of_res.append(min_score)
        else:

            if end_idx == len_arr-1:
                for s_elm in S[start_idx:]:
                    min_score = letter_to_score[s_elm] if letter_to_score[s_elm] < min_score else min_score
                    if min_score == 1:
                        break


            else:
                for s_elm in S[start_idx:end_idx+1]:
                    min_score = letter_to_score[s_elm] if letter_to_score[s_elm] < min_score else min_score
                    if min_score == 1:
                        break

            list_of_res.append(min_score)
            if min_score == 1:
                list_of_save_min_by_pos.append((start_idx, end_idx))
    return list_of_res

```

### Second

* Programming language: Python
* Task score: 100%, 0% -> 62%
* Analysis : O(N * M)
* Link: https://app.codility.com/demo/results/training7Y7J2C-ZYN/
* Code

```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    str_to_imf = {
        "A":1,
        "C":2,
        "G":3,
        "T":4
        }
    
    if len(set(S)) == 1:
        return [ str_to_imf[S[0]] ] * len(P)
    
    # 최저 최고 prefix sum으로 풀수 없으니 고민해보다가..
    # prefix sum 으로 컴포넌트 개수 세보자!로 결정
    prefix_sum = []
    ACGT_to_sum = {
            "A":0,
            "C":0,
            "G":0,
            "T":0
            }
            
    # 깊은 복사 해줘야함
    import copy
    for i, s_elm in enumerate(S): # O(N)
        if i == 0:
             ACGT_to_sum[s_elm] += 1
             prefix_sum.append(ACGT_to_sum)
        else:
            _ACGT_to_sum = copy.deepcopy(prefix_sum[-1]) 
            _ACGT_to_sum[s_elm] += 1
            prefix_sum.append(_ACGT_to_sum)
    
        
    
    M = len(P)
    res_list = []
    acgt_list = ['A', 'C', 'G', 'T']
    # acgt_list = list(set(S))
    # acgt_list.sort()
    # print("acgt_list: " , acgt_list)
    for i in range(M): # O(M)
        # 매번 인덱싱하는건 좀 위험함.. 속도가 느려질수있음
        # if Q[i] == len(S):
        #     sub_str = S[P[i]:]
        # else:
        #     sub_str = S[P[i]:Q[i]+1]
        
        if Q[i] == P[i]:
            res_list.append(str_to_imf[S[Q[i]]])
            continue
        for s_elm in acgt_list:
            if P[i] == 0:
                count = prefix_sum[Q[i]][s_elm]
            else:
                count = prefix_sum[Q[i]][s_elm] - prefix_sum[P[i]-1][s_elm] 

            if count > 0:
                res_list.append(str_to_imf[s_elm])
                break
            
    return res_list
```

### Third
* Programming language: Python
* Task score: 100%
* Analysis : O(N + M)
* Link: https://app.codility.com/demo/results/training9SS4B3-FDC/
* Code

```python
def solution(S, P, Q):
    # write your code in Python 3.6
    str_to_imf = {
        "A":1,
        "C":2,
        "G":3,
        "T":4
        }
    
    # if len(set(S)) == 1:
    #     return [ str_to_imf[S[0]] ] * len(P)
    
    # 최저 최고 prefix sum으로 풀수 없으니 고민해보다가..
    # prefix sum 으로 컴포넌트 개수 세보자!로 결정
    prefix_sum = []
    ACGT_counter = [0,0,0,0]
    ACGT = ['A','C','G','T']
    M = len(P)
    N = len(S)
    
    for i, s_elm in enumerate(S): # O(N)
        if s_elm == 'A':
            ACGT_counter[0] += 1
        elif s_elm == 'C':
            ACGT_counter[1] += 1
        elif s_elm == 'G':
            ACGT_counter[2] += 1
        else: # 'T'
            ACGT_counter[3] += 1
        prefix_sum.append(ACGT_counter[:])

    res_list = []
    
    for i in range(M): # O(M)
        if Q[i] == P[i]:
            res_list.append(str_to_imf[S[Q[i]]])
            continue
        for idx in range(4):
            if P[i] == 0:
                count = prefix_sum[Q[i]][idx]
            else:
                count = prefix_sum[Q[i]][idx] - prefix_sum[P[i]-1][idx] 
            if count > 0:
                res_list.append(str_to_imf[ACGT[idx]])
                break
            
    return res_list
```


## Comment
- 첫번째 풀때보다 코드는 나아진것 같은데 Performance 점수는 더 떨어졌다. O(N * M)이라는데 이유를 모르겠음
- 각 ACGT에 대한 prefix sum을 쓰는걸로 아이디어를 적용함. 나쁘지 않은 방법인거 같은데 미세한 차이로 performance test fail 나서 고민중..
- prefix_sum 할때 꼭 front index 값을 포함하려면 A[back] - A[front-1] 이런 식으로 front index 전 값에서 빼야하는거 유의하고 if front-1 == 0 else ...  케이스 나눠줘야하는거 기억!
- 세번째 풀이는 그냥 dict으로 개수 체크 했던걸 리스트로 바꿔준것 뿐이다 deep copy도 안하고 그냥 [:]로 처리하고, 로직상은 같은데 아무래도 list를 index로 바로 접근하는게 dict을 key로 접근하는것보다 좀 더 빠른게 아닌가.. 아님 deep copy에서 병목이 생기는게 아닌가 싶다.
