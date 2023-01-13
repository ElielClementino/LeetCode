// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
var nums = [8,1,2,2,3]

var smallerNumbersThanCurrent = function(nums) {
    var lowest_count = 0
    var lista_count = []
    
    for (let num=0; num < nums.length; num++){
        for (let next_num=0; next_num < nums.length; next_num++) {
            if (nums[num] > nums[next_num]) {
                lowest_count += 1
            }
        }
        lista_count.push(lowest_count)
        lowest_count = 0
    }
    return lista_count
    
};

console.log(smallerNumbersThanCurrent(nums))