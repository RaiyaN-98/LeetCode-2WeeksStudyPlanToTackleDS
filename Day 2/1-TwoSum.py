class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic: dic[nums[i]].append(i)
            else: dic[nums[i]] = [i]
                
        ans = []
        
        for i in range(len(nums)):
            x = target - nums[i]
            if x in dic: 
                if x != nums[i]:
                    ans.append(i)
                    ans.append(dic[x][0])
                    break
                elif len(dic[x]) > 1:
                    ans.append(i)
                    ans.append(dic[x][1])
                    break
        return ans
        
