# 88. Merge Sorted Array

This is a task from LeetCode ([link](https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)).

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to 0 and should be ignored. `nums2` has a length of `n`.

## Examples

### Example 1
**Input**: `nums1 = [1,2,3,0,0,0]`, `m = 3`, `nums2 = [2,5,6]`, `n = 3`  
**Output**: `[1,2,2,3,5,6]`  
**Explanation**: The arrays we are merging are `[1,2,3]` and `[2,5,6]`. The result of the merge is `[1,2,2,3,5,6]` with the underlined elements coming from `nums1`.

### Example 2
**Input**: `nums1 = [1]`, `m = 1`, `nums2 = []`, `n = 0`  
**Output**: `[1]`  
**Explanation**: The arrays we are merging are `[1]` and `[]`. The result of the merge is `[1]`.

### Example 3
**Input**: `nums1 = [0]`, `m = 0`, `nums2 = [1]`, `n = 1`  
**Output**: `[1]`  
**Explanation**: The arrays we are merging are `[]` and `[1]`. The result of the merge is `[1]`. Note that because `m = 0`, there are no elements in `nums1`. The 0 is only there to ensure the merge result can fit in `nums1`.

## Constraints
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Follow up
Can you come up with an algorithm that runs in O(m + n) time?
## Solution Approach

### Algorithm: Three Pointers (Backward)

The implemented solution uses the optimal three-pointers technique working from the end of the arrays:

1. **Three Pointers**:
   - `pointer_1`: points to the last valid element in `nums1` (at index `m-1`)
   - `pointer_2`: points to the last element in `nums2` (at index `n-1`) 
   - `insert_pos`: points to the last position in `nums1` (at index `m+n-1`)

2. **Key Insight**: By processing arrays from the end, we avoid overwriting unprocessed elements in `nums1`. This eliminates the need for temporary arrays or complex shifting operations.

3. **Process**:
   - Compare elements at `pointer_1` and `pointer_2`
   - Place the larger element at `insert_pos`
   - Move the corresponding pointer and `insert_pos` backward
   - Continue until one array is fully processed
   - Copy remaining elements from the other array

### Why This Approach is Optimal

**Time Complexity**: O(m + n)
- Each element from both arrays is processed exactly once
- No nested loops or repeated operations

**Space Complexity**: O(1)
- Only uses three integer variables as pointers
- Modifies `nums1` in-place without additional storage

### Key Advantages

1. **In-place modification**: Uses existing space in `nums1` without requiring extra memory
2. **No element shifting**: By working backward, we never overwrite unprocessed data
3. **Handles edge cases naturally**: Empty arrays, single elements, and boundary conditions are handled by the pointer logic
4. **Stable sorting**: When equal elements are encountered, the element from `nums2` is placed first, maintaining relative order

### Alternative Approaches

While this solution is optimal, other approaches exist:

1. **Naive approach**: Copy `nums2` to the end of `nums1` and sort - O((m+n)log(m+n)) time
2. **Forward three pointers**: Requires shifting elements - O(mn) time in worst case
3. **Temporary array**: Copy merged result to temporary array then back to `nums1` - O(m+n) time but O(m+n) space

The backward three-pointers approach is the most efficient solution, meeting the follow-up requirement of O(m+n) time complexity while using only O(1) extra space.