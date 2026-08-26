class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return nums
        if len(nums)==len(set(nums)):
            return nums
        h={}
        for i in range(len(nums)):
            if nums[i] in h:
                h[nums[i]]=h[nums[i]]+1
            else:
                h[nums[i]]=1
        l=[]
        i,maxel,c=0,0,0
        """for i in range(len(nums)):
            if h[nums[i]]>c:
                c=h[nums[i]]
            if nums[i] not in l:
                l.append(nums[i])
                h[nums[i]]=0
            c=0"""

        while len(l)<k:
            if i<len(nums):
                if h[nums[i]]>c:
                    c=h[nums[i]]
                    maxel=nums[i]
            i+=1
            if i==len(nums)-1:
                l.append(maxel)
                h[maxel]=0
                c=0
                i=0
        return l