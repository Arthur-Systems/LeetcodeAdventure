# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, sum: int, index: int, result: list[int]):
        print(sum)
        while index >= len(result):
            result.append(0)
        result[index] += sum
        while result[index] > 9:
            carry = result[index]//10
            result[index] %= 10
            if index + 1 >= len(result):
                result.append(0)
            result[index + 1] += carry
            index += 1
        return result

    def Helper(self, l1: list[int], l2: list[int]):
        result = []
        while len(l1) != len(l2):
            if len(l1) > len(l2):
                l2.append(0)
            else:
                l1.append(0)
        print(l1, l2)
        for i in range(len(l1)):
            result = self.addTwoNumbers(l1[i] + l2[i], i, result)
        return result


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    print(Solution().Helper(l1, l2))
