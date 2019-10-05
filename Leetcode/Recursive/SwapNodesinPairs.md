# Swap Nodes in Pairs
## Task description
To showcase the above guidelines, we give another example on how to solve a problem recursively. 

Given a linked list, swap every two adjacent nodes and return its head.

e.g.  for a list 1-> 2 -> 3 -> 4, one should return the head of list as 2 -> 1 -> 4 -> 3.

We define the function to implement as swap(head), where the input parameter head refers to the head of a linked list. The function should return the head of the new linked list that has any adjacent nodes swapped.

Following the guidelines we lay out above, we can implement the function as follows:

First, we swap the first two nodes in the list, i.e. head and head.next;
Then, we call the function self as swap(head.next.next) to swap the rest of the list following the first two nodes.
Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a new linked list.
As an exercise, you can try to implement the solution using the steps we provided above. Click on "Swap Nodes in Pairs" to try to implement the solution yourself. 


## Examples

```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

## Solution

### Frist


- 55 / 55 test cases passed.
- Status: Accepted
- Runtime: 40 ms
- Memory Usage: 14 MB
- Link: https://leetcode.com/submissions/detail/266174092/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or  head.next is None:
            return head
        else:
            head.val, head.next.val, = head.next.val, head.val

            head.next.next = self.swapPairs(head.next.next)
            return head
```

## Comment
- 동시할당문으로 편하기 풀긴했는데, 이거 키포인트는.. next에 대한 포인터를 바꾸는게 아니라 그냥 val 만 바꿔주는거임.. 포인트 바꿔버리면 너무 헷갈려짐
- return 조건은 홀수일때 짝수일때 다르니 조심해야함
