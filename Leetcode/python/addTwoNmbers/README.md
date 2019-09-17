- 포인트
    - 다음 node의 pointer를 넘겨주고, 재귀적으로 호출
    - None 값 체크해서, 바로 포인터 접근하지말고 변수로 바꿔서 사용
        - None 값 있는 노드느 새로 잘 만들어주고
    - None 체크등은 if문 inline에서 끝내는게 보기 편한듯
    - 경우의 수에 대한 분기 잘 짤라주고
        - 지금처럼 코드 짰을땐 일반화하기 힘들거같으니 일반화하는 방법 고민해봐야함

```
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

- my code

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_val = 0 if l1 is None else l1.val
        l2_val = 0 if l2 is None else l2.val
        val = l1_val + l2_val
        if val >= 10: # if one of l1, l2 is None, Never come here
            val = val - 10
            result_node = ListNode(val)
            if l1.next is None and l2.next is None:
                result_node.next = ListNode(1)
            elif l1.next is None:
                result_node.next = self.addTwoNumbers(ListNode(1), l2.next)
            elif l2.next is None:
                result_node.next = self.addTwoNumbers(l1.next, ListNode(1))
            else:
                l1.next.val = l1.next.val + 1
                result_node.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            result_node = ListNode(val)

            if l1.next is None and l2.next is None:
                return result_node
            elif l1.next is None:
                result_node.next = l2.next
            elif l2.next is None:
                result_node.next = l1.next
            else:
                result_node.next = self.addTwoNumbers(l1.next, l2.next)

        return result_node
```

- result
```
Success
Runtime: 72 ms, faster than 92.18% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.6 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
```
