const bold = "\x1b[1m";
const underline = "\x1b[4m";
const color = "\x1b[36m%s\x1b[0m"

interface ITaskList<T> {
  addTask(item: T): void,   // adds an item to the queue (enqueue)
  completedTask():T | undefined,  // retrieves an item from the queue (dequeue)
  size() : number;  // returns the size of the queue
  getCurrentTask() : T | undefined;  // Current Task 
}

class TaskList<T> implements ITaskList<T> {
  private storage : T[] = [];
  constructor(private capacity: number= 5) {}
  
  addTask(item: T): void {
    if (this.size() < this.capacity) {
      this.storage.push(item);
    } else {
      console.error("List has reached it;s limit ", item , " not added");
      
    }
  }

  completedTask(): T | undefined {
    this.storage.shift(); 
    return;   
  }

  getCurrentTask(): T | undefined {
    return this.storage[0]
  }

  size(): number {
    return this.storage.length;
  }
}


let heartList = new TaskList();
heartList.addTask("DSA 5 video");
heartList.addTask("Commit 1 on project");
heartList.addTask("Creating Gist");

console.log(color,bold, underline, heartList.getCurrentTask());

heartList.completedTask();

// let size: number = heartList.size();
// for (let index: number = 0; index < size; index++) {
//   console.log(heartList.getCurrentTask());
//   heartList.completedTask();
// }