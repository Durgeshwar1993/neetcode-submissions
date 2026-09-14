class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_prod = {}
        right_prod = {}

        prod = 1
        for i in range(len(nums)):
            prod = prod*nums[i]
            left_prod[i] = prod
        prod = 1
        for j in range(len(nums)-1,0,-1):
            prod = prod*nums[j]
            right_prod[j] = prod
        
        res = []
        for i in range(len(nums)):
            res.append(left_prod.get(i-1,1)*right_prod.get(i+1,1))
        #print(left_prod,right_prod)
        return res