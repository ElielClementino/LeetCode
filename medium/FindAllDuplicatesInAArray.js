// https://leetcode.com/problems/find-all-duplicates-in-an-array/
nums = [4,3,2,7,8,2,3,1]
nums.sort()
repetidos = []
var findDuplicates = function(nums) {
    for (index=0; index <= nums.length; index++){
        if (index + 1 < nums.length){
            if (nums[index] == nums[index + 1]){
                repetidos.push(nums[index])
            }
        }
    }
    return repetidos
};
console.log(findDuplicates(nums))