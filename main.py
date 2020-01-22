import math
from typing import List


class Solution():
    # Problem 48
    def rotate(self, matrix: List[List[int]]) -> None:
        last = len(matrix)-1
        for r in range(last):
            for c in range(r, last-r):
                matrix[r][c], matrix[last-c][r], matrix[last-r][last-c], matrix[c][last-r] = matrix[last-c][r], matrix[last-r][last-c], matrix[c][last-r], matrix[r][c]
        return matrix


    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = [None] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] <= len(nums):
                arr[nums[i] - 1] = True

        print(arr)
        for i in range(len(nums)):
            if arr[i] != True:
                return i + 1

        return len(nums) + 1

    def myPow(self, x: float, n: int) -> float:

        if x == 1 or x == 0:
            return x

        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        m = n / 2

        if abs(n) == 1:
            return x

        if int(m) + int(m) == n:
            return self.myPow(x * x, n / 2)
        else:
            return self.myPow(x * x, math.floor(n / 2)) * x

    def longestCommonPrefix(self, strs) -> str:

        index = 1
        if len(strs) == 0:
            return ''

        while 1:
            prefix = strs[0][:index]
            eject = False
            for str in strs:

                if str[:index] == '':
                    return ''
                if str[:index] != prefix:
                    eject = True
                    break

            if eject:
                break

            if index > len(strs[0]):
                break
            index = index + 1

        return strs[0][:index - 1]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        a = nums1
        b = nums2

        aI = 0
        bI = 0
        aJ = len(nums1) - 1
        bJ = len(nums2) - 1

        if aJ < 0:
            return (b[math.ceil((bI + bJ) / 2)] + b[math.floor((bI + bJ) / 2)]) / 2
        elif bJ < 0:
            return (a[math.ceil((aI + aJ) / 2)] + a[math.floor((aI + aJ) / 2)]) / 2

        if (aJ == aI and bJ == bI):
            return (a[aI] + b[bI]) / 2

        while 1:
            if a[aJ] >= b[bJ]:
                aJ = aJ - 1
            else:
                bJ = bJ - 1

            if a[aI] <= b[bI]:
                aI = aI + 1
            else:
                bI = bI + 1

            if (aJ == aI and bJ == bI):
                return (a[aI] + b[bI]) / 2

            if aJ - aI < 0 or bJ - bI < 0:
                break

        # print(aI,aJ, bI, bJ)

        if aJ - aI < 0:
            if (bI + bJ) % 2 == 0:
                return b[int((bI + bJ) / 2)]
            else:
                return (b[math.ceil((bI + bJ) / 2)] + b[math.floor((bI + bJ) / 2)]) / 2
        else:
            if (aI + aJ) % 2 == 0:
                return a[int((aI + aJ) / 2)]
            else:
                return (a[math.ceil((aI + aJ) / 2)] + a[math.floor((aI + aJ) / 2)]) / 2


if __name__ == '__main__':
    solution = Solution()

    print(solution.findMedianSortedArrays([1, 3, 6, 8, 15], [2, 5, 6, 9, 10]))
    print(solution.findMedianSortedArrays([], [2, 5, 6, 9]))
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))

    print(solution.longestCommonPrefix(['abb', 'abeegaae', 'aberrae']))
    print(solution.longestCommonPrefix(['', 'a', 'b']))
    print(solution.longestCommonPrefix(['a', 'aa']))

    print(solution.myPow(2, -3))
    print(solution.myPow(3, -4))
    print(solution.myPow(-2, 2))
    print(solution.myPow(2.5, 3))
    print(solution.myPow(5.3, 333))
    print(solution.myPow(1, 43453434335))

    print(solution.firstMissingPositive([1, 2, 3, 4, 5]))
    print(solution.firstMissingPositive([3, 4, -1, 1]))
    print(solution.firstMissingPositive([1, 2, 0]))
    print(solution.firstMissingPositive([-5, 1, 3, 2]))

    # print(solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    print(solution.rotate([
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]))
