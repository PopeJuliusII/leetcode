def solution_1(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    p = len(nums1) - 1
    while n:
        if m and nums1[m - 1] > nums2[n - 1]:
            nums1[p] = nums1[m - 1]
            m -= 1
        else:
            nums1[p] = nums2[n - 1]
            n -= 1
        p -= 1
