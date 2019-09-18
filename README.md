Algorithm
========

# leetcode & codility
leetcode & codility를 공부하며 기록하는 Repository
- 계획: 1일 1문제
- 목표: 중급은 꼭 다 풀기

## Codility
- [Codility summary](https://github.com/eagle705/algorithms/tree/master/Codility)

## Leetcode
- [Leetcode summary](https://github.com/eagle705/algorithms/tree/master/Leetcode)
-----------

## Coding Tips
- List.index도 좋지만 List.find가 더 편하다 index가 없을 경우에 -1 리턴하기 때문
- 속도가 우선이면 메모리를 좀 낭비해도 dict으로 코딩하자
- 제곱승은 pow(2, 31)도 되고 2**31도 된다
- None Error가 날 수 있는건 inline if 구문으로 다른변수로 바꾸자
- for loop의 경우 처음과 끝 index를 매우 신경 써라
- n^2이 아닌 방법으로 풀 수 있는 것들을 고민!
  - 양쪽에서 조여오는 경우나
  - BST 같이 mid를 쪼개서 탐색한다든지..!
- 작은 경우의수부터 생각하고 빠르게 브레인스토밍해야
- 어떤 문제들은 그냥 sort 한다음에 푸는게 시간복잡도가 좀 손해봐도 잘풀리는것들이 있음
- 간단한 if 예외처리가 속도를 빠르게함
- if ```elm``` in ```dict or list``` 식의 문법은 경우에 따라서 속도를 4배나 느려지게함
- 수학문제 풀때처럼 빠르게 생각! 틀에서 약간 벗어난 수학문제일때가 많지만
- in-place 문제의 경우 파이썬은 inline에서 여러 객체 대입이 가능하니까 이 특징을 사용하자
- https://www.youtube.com/watch?v=iGFnsuMeUQY
- https://www.youtube.com/user/damazzang/videos
- 코딩테스트 가이드: https://baactree.tistory.com/52
- http://blog.samstdio.com/coding-test/
- https://www.notion.so/580c3a42f21b49b497b7089f539a9f78
- 어려운 문제는 작은문제 여러개로 쪼개져 있다고 생각하면 된다.
- Time complexity가 높은 정답부터 낮은 정답으로 최적화하게끔 풀어나가는게 안전하다.
- 소수 찾기 알고리즘(```Sieve of Eratosthenes```): https://codility.com/media/train/9-Sieve.pdf
- 최대공약수 구하기(Euclidean algorithm): https://codility.com/media/train/10-Gcd.pdf
- 합성수 조합(Counting divisors) + 소수 테스트(Primality test): https://codility.com/media/train/8-PrimeNumbers.pdf
- 가끔 헷갈릴 수 있는데 Binary Search와 Binary Search Tree(BST)는 완전 다른 것임..
- 이진 탐색(Binary Search): https://codility.com/media/train/12-BinarySearch.pdf

## Python Tips
- [파이썬을 파이썬 답게 강의](https://programmers.co.kr/learn/courses/4008)
- sort(), reverse() -> 이런건 객체를 반환하지 않음, sort는 기본적으로 오름차순
- reversed 같은 식으로 하면 객체를 반환하지만 reversed 객체로 나오기때문에 list로 형변환 해줘야함
- / : 나누기(소수점도 나옴), %: 나머지(떨어지는 나머지), //: 몫(곱해지는 텀)
- [12. 얕은 복사(shallow copy)와 깊은 복사(deep copy)](https://wikidocs.net/16038)
- [29. 변수 scope](https://wikidocs.net/16055)
- [44. class 정리 - 정적메소드 @classmethod와 @staticmethod의 정리](https://wikidocs.net/16074)
- (Combination을 위한 itertools)[https://www.geeksforgeeks.org/itertools-combinations-module-python-print-possible-combinations/]
- 숫자 -> 이진법 바꾸기
  - format(32, "b"): '100000'
- 이진법 -> 숫자로 바꾸기
  - int('100000', 2): 32
- unpaired 경우는 if count % 2 == 0 로 2로 나누어 떨어지는지 아닌지로 체크!
- shift 문제의 경우, % 를 이용해서 나누기를 통해 length를 넘어가는 인덱스를 관리한다
- 나누기(/)나 나머지(%) 구하거나, 몫(//)을 구하는 경우 앞에 텀에 괄호 쳐주자
- for loop 두번 돌지말고 한번만 돌게끔.. 전체 합구해놓고 각 loop에서 처리해준다든지.. 이런식으로 가자 2*O(N)이 O(N^2) 보단 낫다
- 원소 확인할때는 list 에 append해서 if in으로 하지말고 set() .add로 해서 확인하는게 훨씨인 빠름
- [파이썬 내장함수 TimeComplexity 참고](https://wiki.python.org/moin/TimeComplexity), 보면 같은 x in s라도 list와 set은 복잡도가 다르고, 리스트의 경우 새로 생성하는거 자체가 O(n)임.. 굳이 생성안해도 되는거면 if로 비교하는게 훨씬 나음!
- list -> set 바꾸는것도 time complexity n 들어감
- 나누어 떨어지는 수 개수 세는 문제 같은 경우는 for loop 돌리지 말고 그냥 / 나 // 연산자로 몫 개수 세고 n mod k == 0인 경우 n 이 0인 경우도 고려해야하니 주의할 것!
- itertools의 경우 yield로 반환하기 때문에 list로 감싸는것과 안감싸는게 차이가 좀많이 남 ```for _ in itertools.combinations(range(length), 3):``` [문서 참고](https://docs.python.org/2/library/itertools.html#itertools.combinations)
- O(N**2)를 O(N)으로 풀려면 수학적인 센스가 있어야되는 문제들이 몇개 있음
- stack 문제를 풀때는 마지막에 스택에 값이 남아있는지와, 스택에 값이 없는데 pop 하려고하는때 이 두 가지에 대해서 예외처리 해줘야함
- pop은 왠만하면 바로 쓰지말고, [-1]로 인덱싱해서 쓰다가 조건이 딱 맞춰졌을때 pop으로 빼라 안 그러면 arr_length 때문에 while등에서 조건으로 쓸 경우 에러날 수 있음.. while문에서 쓰는 조건은 간단하게 하고, 차라리 True로 주고 안의 if 문으로 break 거는 처리를 하는게 더 편할 수 있음!
- O(N)을 여러번 하는게 loop 안에서 한번 더 리스트 탐색해서 O(N**2) 만드는 것보다 나음
- cumulative 하게 쌓을땐 list의 extend 기능을 활용해보자
- 재귀는 리턴 조건이 명확할때만 써야!
- max_slice 문제는 lower bound 0으로 셋팅하고 풀고 최대값이 0이하면 max()로 -값 리턴해주면됨. lower bound가 0 이라는건 새로 슬라이스 하겠다는 뜻임
- 소수 찾을때 time complexity 줄이는 방법중 하나는 sqrt(N)을 해서 divider가 sqrt(N)보다 클때도 합성수가 없으면 소수로 리턴하는거다. 이게 왜 성립되냐면 합성수라면 sqrt(N)전에 반드시 합성수가 존재한다. 위의 경우는 왠만하면 다 잘 되는데 숫자 2(소수) 인 경우엔 인덱스에 따라 작동 안할 수가 있다.
- 소수를 구분할때 속도를 위한 sqrt(N)으로 풀수도 있고 i*i < N 을 기준으로 풀수도 있다. 합성수 찾을때도 그 중간 값이 sqrt(N)이기 때문에 한번에 i 와 N // i 라는 합성수 2개를 찾으면 sqrt(N) 까지만 찾으면 된다. 그리고 합성수 찾을 때 if i == N // i 인 경우는 중복이니 조심 할 것!

## interview Tips
- [Reverse Interview](https://github.com/JaeYeopHan/Interview_Question_for_Beginner/blob/master/Reverse_Interview/README.md)



---------

## Reference Repo
- https://github.com/dudmy/study/tree/master/Codility
