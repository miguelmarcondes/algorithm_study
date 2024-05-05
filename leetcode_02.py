## For the description of the problem, check this link: https://leetcode.com/problems/add-two-numbers/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_number = self.return_aligned_number(l1)
        second_number = self.return_aligned_number(l2)
        result = first_number + second_number
        result_node = None
        for digit in str(result):
            new_node = ListNode(int(digit))
            new_node.next = result_node
            result_node = new_node
            
        return result_node
        
    def return_aligned_number(self, l: Optional[ListNode]) -> int:
        current = l
        number_str = ""
        while current:
            number_str = str(current.val) + number_str
            current = current.next
        return int(number_str)
