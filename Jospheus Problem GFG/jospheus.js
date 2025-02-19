var Josephus = /** @class */ (function () {
    function Josephus() {
    }
    Josephus.prototype.josephus = function (n, k) {
        var arr = [];
        for (var index = 0; index < n; index++)
            arr.push(index + 1);
        return this.solve(arr, k, 0);
    };
    Josephus.prototype.solve = function (arr, k, pos) {
        if (arr.length === 1) {
            return arr[0];
        }
        pos = (pos + k - 1) % arr.length;
        arr.splice(pos, 1);
        return this.solve(arr, k, pos);
    };
    return Josephus;
}());
