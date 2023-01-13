// https://leetcode.com/problems/search-insert-position/
nums = [1,3,5,6]
target = 7
var searchInsert = function(nums, target) {
    if (nums.includes(target)) {
        return nums.indexOf(target)
    }
    nums.push(target)
    nums.sort((a,b) => a-b)
    return nums.indexOf(target)
}

position = searchInsert(nums, target)
console.log(position)