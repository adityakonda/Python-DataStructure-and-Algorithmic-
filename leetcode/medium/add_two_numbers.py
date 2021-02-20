# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __int__(self, val, next):
        self.val = val,
        self.next = next

class LinkedList:

    def __int__(self):
        self.head = None

    def insert_end(self, val):
        if self.head is None:
            self.head = ListNode(val, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next


        itr.next = ListNode()



        # (2,None)
        # (2, obj4), (4, None)
        # (2, obj4), (4, obj3), (3, None)


        pass

    def insert_value(self, list):
        for element in list:
            self.insert_end(element)



class Solution:



    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
