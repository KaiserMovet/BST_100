
class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    add(value) {
        if (value < this.value) {
            if (this.left == null) {
                this.left = new Node(value);
                return true;
            }
            return this.left.add(value);
        }
        if (value > this.value) {
            if (this.right == null) {
                this.right = new Node(value);
                return true;
            }
            return this.right.add(value);
        }
        return false;
    }


    contain(value) {
        if (value < this.value) {
            if (this.left == null) {
                return false;
            }
            return this.left.contain(value);
        }
        if (value > this.value) {
            if (this.right == null) {
                return false;
            }
            return this.right.contain(value);
        }
        return false;
    }

    length() {
        let a = (this.left == null ? 0 : this.left.length());
        let b = (this.right == null ? 0 : this.right.length());
        return a + b + 1;
    }

    height() {
        let a = (this.left == null ? 1 : this.left.height() + 1);
        let b = (this.right == null ? 1 : this.right.height() + 1);
        return (a > b ? a : b)
    }

}

module.exports = Node;