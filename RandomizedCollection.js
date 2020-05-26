/**
 * Initialize your data structure here.
 */
const RandomizedCollection = function() {
  this.map = {};
  this.array = [];
};

// Problem 381

/**
 * Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
 * @param {number} val
 * @return {boolean}
 */
RandomizedCollection.prototype.insert = function(val) {
  if (!this.map[val]) {
    this.map[val] = [this.array.length];
    this.array.push([val, 0]);
    return true;
  } else {
    this.map[val].push(this.array.length);
    this.array.push([val, this.map[val].length - 1]);
    return false;
  }
};

/**
 * Removes a value from the collection. Returns true if the collection contained the specified element.
 * @param {number} val
 * @return {boolean}
 */
RandomizedCollection.prototype.remove = function(val) {
  if (!this.map[val]) return false;

  const ind = this.map[val].pop();
  const [removed, mapIndex] = this.array.pop();

  if (this.map[val].length == 0) delete this.map[val];

  if (ind == this.array.length) return true;

  this.array[ind] = [removed, mapIndex];
  this.map[removed][mapIndex] = ind;

  return true;
};

/**
 * Get a random element from the collection.
 * @return {number}
 */
RandomizedCollection.prototype.getRandom = function() {
  return this.array[Math.floor(Math.random() * this.array.length)][0];
};
