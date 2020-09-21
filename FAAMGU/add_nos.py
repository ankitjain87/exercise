# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self, node):
        while node.next != None:
            print(node.val)
            node = node.next
        print(node.val)

class LinkedList:
    head = None

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = None
        carry = 0
        while l1 and l2:
            n = l1.val + l2.val + carry
            carry = 0

            l1 = l1.next
            l2 = l2.next

            if n > 9:
                n, carry = n%10, 1

            if not output:
                output = ListNode(n)
                self.head = output
            else:
                output.next = ListNode(n)
                output = output.next

        while l1 != None:
            n = l1.val + carry
            carry = 0
            if n > 9:
                n, carry = n%10, 1

            output.next = ListNode(n)
            output = output.next
            l1 = l1.next


        while l2 != None:
            n = l2.val + carry
            carry = 0
            if n > 9:
                n, carry = n%10, 1

            output.next = ListNode(n)
            output = output.next
            l2 = l2.next

        if carry == 1:
            output.next = ListNode(carry)

        return self.head


#  [2, 4, 3], [5, 6, 4]

l1 = ListNode(1)
l1.next = ListNode(8)
# l1.next.next = ListNode(3)

# l1.print_list(l1)

l2 = ListNode(0)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

out = LinkedList().addTwoNumbers(l1, l2)
print("-=-=-==Output======")
out.print_list(out)