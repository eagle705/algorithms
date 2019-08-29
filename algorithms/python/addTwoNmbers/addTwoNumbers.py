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
