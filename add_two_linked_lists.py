# Definition for singly-linked list.
import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def stringify(self):
        if self.next == None:
            return str(self.val)
        else:
            return str(self.val) + '->' + self.next.stringify()

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = linked_list_to_num(l1)
        num2 = linked_list_to_num(l2)
        sum = num1 + num2

        return num_to_linked_list(sum)

def num_to_linked_list(num):
    remainder = num % 10
    next_digit = num // 10 # using Py3 integer division

    node = ListNode(remainder)

    if next_digit > 0:
        node.next = num_to_linked_list(next_digit)
    return node

def linked_list_to_num(listy):
    if listy.next:
        return listy.val + (10 * linked_list_to_num(listy.next))

    return listy.val

a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3

b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

a_to_num = linked_list_to_num(a1)
b_to_num = linked_list_to_num(b1)

print("linked_list_to_num test a", a1.stringify(), a_to_num, a_to_num == 342)
print("linked_list_to_num test b", b1.stringify(), b_to_num, b_to_num == 465)

num_to_c = num_to_linked_list(123).stringify()
num_to_d = num_to_linked_list(835).stringify()
num_to_e = num_to_linked_list(102).stringify()
num_to_f = num_to_linked_list(1000000000000000000000000000001).stringify()
f_to_num = linked_list_to_num(num_to_linked_list(1000000000000000000000000000001))

print("num_to_linked_list test c", num_to_c, num_to_c == '3->2->1')
print("num_to_linked_list test d", num_to_d, num_to_d == '5->3->8')
print("num_to_linked_list test e", num_to_e, num_to_e == '2->0->1')
print("num_to_linked_list test f", num_to_f, num_to_f == '1->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->0->1',
    f_to_num)

test_l1 = num_to_linked_list(1000000000000000000000000000001)
test_l2 = num_to_linked_list(465)

sol = Solution()
out = sol.addTwoNumbers(test_l1, test_l2).stringify()
print(out)