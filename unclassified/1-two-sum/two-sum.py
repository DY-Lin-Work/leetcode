class Solution:
    def sort(nums: List[int], target: int):
        sortedNums = [[], [], []]
        idxList = [[], [], []]

        for idx in range(len(nums)):
            if nums[idx] < target/2:
                sortedNums[0].append(nums[idx])
                idxList[0].append(idx)
            elif nums[idx] == target/2:
                sortedNums[1].append(nums[idx])
                idxList[1].append(idx)
            elif nums[idx] > target/2:
                sortedNums[2].append(nums[idx])
                idxList[2].append(idx)
        return sortedNums, idxList


    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sortedNums, idxList = Solution.sort(nums, target) 
        # Sorts nums into 3 groups: <target/2 =target/2 >target/2

        if len(sortedNums[1]) == 2:
            return idxList[1]
        else:
            for idx_x in range(len(sortedNums[0])):
                diff = target - sortedNums[0][idx_x]
                for idx_y in range(len(sortedNums[2])):
                    if diff == sortedNums[2][idx_y]:
                        return [idxList[0][idx_x], idxList[2][idx_y]]