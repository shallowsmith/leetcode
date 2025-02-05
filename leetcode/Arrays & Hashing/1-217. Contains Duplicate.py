'''
Understand: 
What is the required time and space complexity? 
Time Complexity: O(n) 
Space Complexity: O(n)

Can the input be an empty array?

Match:
Use hashmap to check for pre-existing key

Plan:
Initialize a hashmap

For every element in the array check if the given element already exists in the hashmap,
If not: Add the key-value pair as element-1 to the hash map.
If so: Return true because a value appears twice in the array

Return false at the end because this means there were no duplicates in the array


nums = [1, 2, 3, 1]
1 -> {"1": "1"}
2 -> {"1": "1", "2": "1"}
3 -> {"1": "1", "2": "1", "3": "1"}
1 -> {"1": "1", "2": "1", "3": "1"} -> 1 exists -> return True
'''

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        countMap = {}
        for num in nums: 
            if num not in countMap:
                countMap[num] = 1
            else:
                return True
        
        return False


'''
Review and Eval:
I think the solution could be more optimized with the data structures used. 
'''
