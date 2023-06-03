const Node = require('./node.js');

class Tree {
    constructor() {
        this.root = null;
    }

    add(value) {
        if (this.root == null) {
            this.root = new Node(value);
            return true;
        }
        return this.root.add(value);
    }
    contain(value) {
        if (this.root == null) {
            return false;
        }
        return this.root.contain(value);
    }
    length() {
        return (this.root == null ? 0 : this.root.length())
    }
    height() {
        return (this.root == null ? 0 : this.root.height())
    }

}

module.exports = Tree;