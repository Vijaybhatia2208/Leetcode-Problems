function singleNumber(nums) {
    var ans = 0;
    for (var i = 0; i < nums.length; i++) {
        var x = 0;
        for (var j = 0; j < nums.length; j++) {
            if (i != j && nums[i] == nums[j]) {
                x = 1;
            }
        }
        if (x === 0) {
            ans = nums[i];
        }
    }
    return ans;
}
;
