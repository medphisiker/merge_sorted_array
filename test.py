from main import Solution

def test():
    solution = Solution()
    
    # Example 1 even len
    nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6]
    
    # Example 2 second array len=0
    nums1, m, nums2, n = [1], 1, [], 0
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1]
    
    # Example 3 second array len=0
    nums1, m, nums2, n = [0], 0, [1], 1
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1]
    
    # Doubles
    nums1, m, nums2, n = [1,1,2,2,0,0], 4, [1,2], 2
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1,1,1,2,2,2]
    
    # odd len
    nums1, m, nums2, n = [1,2,3,0,0], 3, [1,2], 2
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1,1,2,2,3]
    
    # negative numbers
    nums1, m, nums2, n = [-109,-1,0,0,0], 3, [-100,109], 2
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [-109,-100,-1,0,109]
    
    # Test 6: Все элементы nums2 меньше nums1
    nums1, m, nums2, n = [5,6,7,0,0,0], 3, [1,2,3], 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,3,5,6,7]
    
    # Test 7: Все элементы nums1 меньше nums2
    nums1, m, nums2, n = [1,2,3,0,0,0], 3, [4,5,6], 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,3,4,5,6]
    
    # Test 8: Пустой nums1 (m=0, n=0)
    nums1, m, nums2, n = [], 0, [], 0
    solution.merge(nums1, m, nums2, n)
    assert nums1 == []
    
    # Test 9: Максимальные значения m и n (200)
    nums1 = [i for i in range(200)] + [0]*200
    nums2 = [i for i in range(200, 400)]
    solution.merge(nums1, 200, nums2, 200)
    assert nums1 == sorted([i for i in range(400)])
    
    # Test 10: Когда nums1 и nums2 содержат одни и те же элементы
    nums1, m, nums2, n = [2,4,6,0,0,0], 3, [2,4,6], 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [2,2,4,4,6,6]
    
    # Test 11: nums1 состоит только из нулей
    nums1, m, nums2, n = [0,0,0], 0, [2,4,6], 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [2,4,6]
    
    # Test 12: nums2 пустой, но m=0 (nums1 непустой)
    nums1, m, nums2, n = [0,0,0], 0, [], 0
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [0,0,0]
    
    
if __name__ == "__main__":
    test()