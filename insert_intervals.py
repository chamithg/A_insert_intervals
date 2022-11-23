class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        for index,(a,b) in enumerate(intervals):
            if newInterval[0]>b and newInterval[1]< intervals[index+1][0]:
                intervals.insert(index +1 ,newInterval)
                return intervals
            elif 
        

obj = Solution()
intervals = [[1,3],[6,9]]
newInterval = [4,5]
print(obj.insert(intervals,newInterval))