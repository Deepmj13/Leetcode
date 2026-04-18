'''

3190. Find Minimum Operations to Make All Elements Divisible by Three
Easy


You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

Return the minimum number of operations to make all elements of nums divisible by 3.

 

Example 1:

Input: nums = [1,2,3,4]

Output: 3

Explanation:

All array elements can be made divisible by 3 using 3 operations:

Subtract 1 from 1.
Add 1 to 2.
Subtract 1 from 4.
Example 2:

Input: nums = [3,6,9]

Output: 0

 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50


if the number is already divisable by three then no need for operation, if number is not divisable by the 3 then need operation like add 1 or subtract 1,

we will check if the it divisable by 3 , 'if no % 3 == 0', but since we have to perfom operation so we will find the number that is not divisable by 3 so if 'no % 3 != 0'.
and then we wil create a nested condition.

'''
def result(nums):
    ops = 0
    for i in nums:
        if i % 3 != 0 :
            ops+=1
            # if i+1 % 3 == 0 or i-1 % 3 == 0:
            #     ops+=1
    print(ops)

result([1,2,3,4])