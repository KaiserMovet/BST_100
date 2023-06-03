import { TreeNode } from './node';

export class Tree {
    root: TreeNode | null;

    constructor() {
        this.root = null;
    }

    add(value: number) {
        if (this.root == null) {
            this.root = new TreeNode(value);
            return true;
        }
        return this.root.add(value);
    }
    contain(value: number) {
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

