var RopeCutting = /** @class */ (function () {
    function RopeCutting() {
    }
    RopeCutting.prototype.RopeCutting = function (arr) {
        arr.sort(function (a, b) { return a - b; }); // Sort the array in ascending order
        var j = 0;
        var n = arr.length;
        var total = n - 1;
        for (var i = 1; i < n; i++) {
            if (arr[i] !== arr[i - 1]) {
                arr[j] = n - i;
                j++;
            }
        }
        return arr.slice(0, j);
    };
    return RopeCutting;
}());
