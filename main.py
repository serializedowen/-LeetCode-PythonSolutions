import math
from typing import List
import collections
import math


class Solution:

    # Problem 313
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:


        pass


    # Problem 347    TODO
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums.sort()
        ret = []
        min = len(nums)
        count = 0
        minVal =
        for i in range(0, len(nums)):
            if i == len(nums) - 1:
                if count >= min or len(ret) < k:
                    if minVal != '':
                        ret.remove(minVal)
                    ret.append(nums[i])
                break


            count += 1

            if nums[i] != nums[i + 1]:

                if len(ret) < k:
                    ret.append(nums[i])
                    if count < min:
                        min = count
                        minVal = nums[i]

                elif count >= min:
                    ret.remove(minVal)
                    ret.append(nums[i])
                    minVal = nums[i]
                    min = count

                count = 0

        return ret







    # Problem 309
    def maxProfit(self, prices: List[int]) -> int:
        if not len(prices): return 0
        # the max prof of at I while holding/not holding stock
        dp = [[0, 0] for i in range(0, len(prices))]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 2][1] - prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])

        return dp[len(prices) - 1][1]


    # Problem 343
    def integerBreak(self, n: int) -> int:
        res = 1
        if (n == 2): return 1
        if (n == 3): return 2
        while (n > 4):
            res *= 3
            n -= 3
        res *= n
        return res


    # Problem 547
    def findCircleNum(self, M: List[List[int]]) -> int:
        def friends(i: int, remain: List[int], M: List[List[int]]):
            if i not in remain: return
            remain.remove(i)
            for u in range(0, len(M)):
                if M[i][u] == 1:
                    friends(u, remain, M)

        remain = [i for i in range(0, len(M))]
        circles = 0

        while len(remain):
            friends(remain[0], remain, M)
            circles += 1

        return circles

    # Problem 509  all
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        n, m = 0, 1

        for i in range(2, N + 1):
            n, m = m, n + m

        return m

    # Problem 539
    def findMinDifference(self, timePoints: List[str]) -> int:

        timePoints.sort()

        h0, m0 = timePoints[0].split(':')

        dict = {}

        def diff(a, b):

            if a in dict:
                aMin = dict[a]
            else:
                aT = a.split(":")
                aMin = int(aT[0]) * 60 + int(aT[1])
                dict[a] = aMin

            if b in dict:
                bMin = dict[b]
            else:
                bT = b.split(":")
                bMin = int(bT[0]) * 60 + int(bT[1])
                dict[b] = bMin

            val = abs(aMin - bMin)

            if val >= 12 * 60:
                return 24 * 60 - val
            else:
                return val

        overflow = diff(str(int(h0) + 24) + ':' + m0, timePoints[-1])

        for i in range(1, len(timePoints)):
            overflow = min(diff(timePoints[i], timePoints[i - 1]), overflow)

        return overflow


# Problem 552
def checkRecord(self, n: int) -> int:
    fib = [[0, 0], [3, 2], [8, 4], [19, 7]]
    fib.extend([[0, 0] for i in range(0, n - 3)])

    for i in range(4, n + 1):
        fib[i][1] = 2 * fib[i - 1][1] - fib[i - 4][1]
        fib[i][0] = (3 * fib[i - 1][0]) - fib[i - 4][0] * 2 - fib[i - 2][1] * (i - 1)

    print(fib)

    return fib[n][0]


# Problem 551
def checkRecord2(self, s: str) -> bool:
    cA = 0

    for i, c in enumerate(s):
        if c == 'A':
            cA += 1

        if c == 'L' and i >= 2:
            if c == s[i - 1] and c == s[i - 2]:
                return False

    return cA < 2


# Problem 645
def findErrorNums(self, nums: List[int]) -> List[int]:
    actual = sum(nums)
    expected = int(len(nums) * (len(nums) + 1) / 2)
    dup = actual - sum(set(nums))
    return [dup, dup + expected - actual]


# Problem 492
def constructRectangle(self, area: int) -> List[int]:
    ret = [area, 1]
    for i in range(math.floor(math.sqrt(area)), 0, -1):
        if area % i == 0:
            return [int(area / i), i]

    return ret


# dp(i) represents result of "i" bits number: "1000...". It means the count of all valid numbers smaller than this "100...", including those starting with "0". We can divide this into two sub-problems: Results with first bit being "1", can be represented by dp(i-2) Results with first bit being "0", can be represented by dp(i-1) "first" here means the "i"th bit from left to right So we have: dp(i)=dp(i-1)+dp(i-2) This is a fibonacci number.
# However, this only gives us result of 2^n number. How to find result smaller than any "num"? If the "num" starts with "11", then dp(n) is its result. If "num" starts with "10", then dp(n-1)+next is its result, where "next" is the result of next sub num starting with "1".

# Problem 600  DP
def findIntegers(self, num: int) -> int:
    num = bin(num + 1)[2:]
    n = len(num)
    fibo = [1, 2]
    for _ in range(n - 1):
        fibo.append(fibo[-1] + fibo[-2])

    res = 0
    for i in range(n):
        v = num[i:i + 2]
        if v == '11':
            res += fibo[n - i]
            break
        elif v == '10':
            res += fibo[n - i - 1]
        elif v == '1':
            res += 1
    return res

    # if num < 3:
    #     return num + 1
    #
    # ret = [True for x in range (0, num + 1)]
    # occur = 0
    # curPower = 2
    #
    #
    # for x in range (0, num+ 1):
    #     if curPower * 2 <= x:
    #         curPower *= 2
    #
    #     ret[x] = (x == curPower or x == curPower * 2) or (ret[curPower] and ret[x - curPower] and (x - curPower) < (curPower / 2))
    #
    #     if ret[x]:
    #         occur += 1
    # return occur


# Problem 474  DP
def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for s in strs:
        zeros = s.count('0')
        ones = len(s) - zeros

        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                if i >= zeros and j >= ones:
                    dp[i][j] = max(dp[i - zeros][j - ones] + 1, dp[i][j])

    print(dp)
    return dp[-1][-1]


# Problem 448
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    output = []
    for x in nums:
        y = abs(x)
        nums[y - 1] = 0 - abs(nums[y - 1])

    r = []
    for i, x in enumerate(nums):
        if x > 0:
            r.append(i + 1)
    return r


# Problem 482
def licenseKeyFormatting(self, S: str, K: int) -> str:
    S = S.replace("-", "").upper()

    words = []

    start = len(S) % K
    end = 0

    if S[:start]:
        words.append(S[:start])

    while end < K * (len(S) // K):
        end = start + K
        if S[start:end]:
            words.append(S[start:end])
        start = end

    return '-'.join(words)

    # Problem 433


def minMutation(self, start: str, end: str, bank: List[str]) -> int:
    list = []
    list.append((start, 0))

    def adjacent(a, b):
        count = 0
        for (i, c) in enumerate(a):
            if b[i] != c:
                count = count + 1

            if count > 1:
                return False

        return count == 1

    while len(list):
        a, level = list.pop()

        removed = []
        for (i, s) in enumerate(bank):
            if adjacent(s, a):
                if s == end:
                    return level + 1
                list.append((s, level + 1))
                removed.append(s)
            if a == end:
                return level

            if i == len(bank) - 1:
                for i in removed:
                    bank.remove(i)

                removed = []

    return -1


# Problem 416
def canPartition(self, nums: List[int]) -> bool:
    goal = sum(nums) / 2
    if goal != math.floor(goal): return False
    nums.sort(reverse=True)

    def help(curr, remains):
        for i in range(0, len(remains)):
            if curr + remains[i] > goal: return False
            if curr + remains[i] == goal: return True
            if help(curr + remains[i], remains[:i] + remains[i + 1:]):
                return True

    return help(0, nums)


# Problem 424
def characterReplacement(self, s: str, k: int) -> int:
    if len(s) == 0:
        return 0

    counts = {}
    curMax, start = s[0], 0
    for i, c in enumerate(s):
        counts[c] = counts.get(c, 0) + 1
        if counts[c] > counts[curMax] or (counts[c] == counts[curMax] and curMax == s[start]):
            curMax = c
        flips = i - start + 1 - counts[curMax]
        if flips > k:
            counts[s[start]] -= 1
            start += 1
    return len(s) - start


# Problem 48
def rotate(self, matrix: List[List[int]]) -> None:
    last = len(matrix) - 1
    for r in range(last):
        for c in range(r, last - r):
            matrix[r][c], matrix[last - c][r], matrix[last - r][last - c], matrix[c][last - r] = matrix[last - c][
                                                                                                     r], \
                                                                                                 matrix[last - r][
                                                                                                     last - c], \
                                                                                                 matrix[c][
                                                                                                     last - r], \
                                                                                                 matrix[r][c]
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

    # print(solution.findMedianSortedArrays([1, 3, 6, 8, 15], [2, 5, 6, 9, 10]))
    # print(solution.findMedianSortedArrays([], [2, 5, 6, 9]))
    # print(solution.findMedianSortedArrays([1, 2], [3, 4]))
    #
    # print(solution.longestCommonPrefix(['abb', 'abeegaae', 'aberrae']))
    # print(solution.longestCommonPrefix(['', 'a', 'b']))
    # print(solution.longestCommonPrefix(['a', 'aa']))
    #
    # print(solution.myPow(2, -3))
    # print(solution.myPow(3, -4))
    # print(solution.myPow(-2, 2))
    # print(solution.myPow(2.5, 3))
    # print(solution.myPow(5.3, 333))
    # print(solution.myPow(1, 43453434335))
    #
    # print(solution.firstMissingPositive([1, 2, 3, 4, 5]))
    # print(solution.firstMissingPositive([3, 4, -1, 1]))
    # print(solution.firstMissingPositive([1, 2, 0]))
    # print(solution.firstMissingPositive([-5, 1, 3, 2]))
    #
    # print(solution.characterReplacement('AVVGYYABBB', 1))

    # print(solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    # print(solution.rotate([
    #     [5, 1, 9, 11],
    #     [2, 4, 8, 10],
    #     [13, 3, 6, 7],
    #     [15, 14, 12, 16]
    # ]))

    # print(solution.canPartition([1, 5, 11, 5]))

    # print(solution.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]))

    # print(solution.minMutation("AAAAAAAA",
    #                            "CCCCCCCC",
    #                            ["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC", "AACACCCC", "ACCACCCC",
    #                             "ACCCCCCC", "CCCCCCCA",
    #                             "CCCCCCCC"]))
    #
    #
    # print(solution.licenseKeyFormatting("5F3Z-2e-9-w", 4))
    # print(solution.licenseKeyFormatting("2-5g-3-J", 2))
    # print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

    # print(solution.findMaxForm(['1'], 4, 2))
    #
    # print(solution.findIntegers(5))

    # print(solution.constructRectangle(78594))
    #
    # print(solution.findErrorNums([5,2,3,4,5,6,7]))
    # print(solution.findErrorNums([1,2,3,4,5,6,3]))
    # print(solution.findErrorNums([1,2,2,4]))
    # print(solution.findErrorNums([1,1]))
    # print(solution.findErrorNums([2, 2]))

    # print(solution.checkRecord("PPALLL"))
    # print(solution.checkRecord(4))

    # print(solution.findMinDifference(["23:59","00:00", '12:22', '12:23', '11:22']))
    # print(solution.findMinDifference(["23:59", "00:00", '00:00']))

    # print(solution.fib(4))
    #
    # print(solution.findCircleNum([[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
    # print(solution.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    # print(solution.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))


    # print((solution.integerBreak(8)))
    # print(solution.maxProfit([1,2,3,0,2]))

    print(solution.topKFrequent([1,1,1,2,2,3], 2))