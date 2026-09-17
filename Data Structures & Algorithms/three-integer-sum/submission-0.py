class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        list1 = []
        for i in range(len(nums)):
            
            j = i + 1
            k = len(nums)-1
            while j < k:
                #print(i,j,k)
                if nums[i] + nums[j] + nums[k] == 0 and ([nums[i] , nums[j] , nums[k]] not in list1):
                    list1.append([nums[i] , nums[j] , nums[k]])
                
                if nums[i] + nums[j] + nums[k] > 0:
                    k -=1
                else:
                    j += 1
        return list1
                






        