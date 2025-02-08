function singleNumber(nums) {
    var ans = [];
    for (var i = 0; i < nums.length; i++) {
        var test = true;
        for (var j = 0; j < nums.length; j++) {
            if ((j !== i) && (nums[i] === nums[j]))
                test = false;
        }
        test && ans.push(nums[i]);
    }
    return ans;
}
;
