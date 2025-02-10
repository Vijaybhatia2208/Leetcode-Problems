var Solutions = /** @class */ (function () {
    function Solutions() {
    }
    Solutions.prototype.AllPossibleStrings = function (s) {
        var bitSize = 1 << s.length;
        var answer = [];
        for (var index = 1; index < bitSize; index++) {
            var val = "";
            for (var j = 0; j < s.length; j++) {
                if (index & (1 << j))
                    val += s[j];
            }
            answer.push(val);
        }
        return answer.sort();
    };
    return Solutions;
}());
