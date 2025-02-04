var Solution = /** @class */ (function () {
    function Solution() {
    }
    // Function to check if Kth bit is set or not.
    Solution.prototype.checkKthBit = function (n, k) {
        var leftbit = 1 << k;
        return (n & leftbit) !== 0;
    };
    return Solution;
}());
var checkCode = new Solution();
console.log(checkCode.checkKthBit(4, 0));
console.log(checkCode.checkKthBit(4, 2));
console.log(checkCode.checkKthBit(500, 3));
