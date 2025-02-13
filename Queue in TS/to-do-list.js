var bold = "\x1b[1m";
var underline = "\x1b[4m";
var color = "\x1b[36m%s\x1b[0m";
var TaskList = /** @class */ (function () {
    function TaskList(capacity) {
        if (capacity === void 0) { capacity = 5; }
        this.capacity = capacity;
        this.storage = [];
    }
    TaskList.prototype.addTask = function (item) {
        if (this.size() < this.capacity) {
            this.storage.push(item);
        }
        else {
            console.error("List has reached it;s limit ", item, " not added");
        }
    };
    TaskList.prototype.completedTask = function () {
        this.storage.shift();
        return;
    };
    TaskList.prototype.getCurrentTask = function () {
        return this.storage[0];
    };
    TaskList.prototype.size = function () {
        return this.storage.length;
    };
    return TaskList;
}());
var heartList = new TaskList();
heartList.addTask("DSA 5 video");
heartList.addTask("Commit 1 on project");
heartList.addTask("Creating Gist");
console.log(color, bold, underline, heartList.getCurrentTask());
heartList.completedTask();
// let size: number = heartList.size();
// for (let index: number = 0; index < size; index++) {
//   console.log(heartList.getCurrentTask());
//   heartList.completedTask();
// }
