public class Node {
    int value;
    Node left;
    Node right;

    public Node(int value){
        this.value = value;
        this.left = null;
        this.right = null;
    }

    public boolean add(int value) {
        if(value<this.value){
            if(this.left==null){
                this.left = new Node(value);
                return true;
            }
            return this.left.add(value);
        }

        if(value>this.value){
            if(this.right==null){
                this.right = new Node(value);
                return true;
            }
            return this.right.add(value);
        }
        return false;
    }

    public boolean contain(int value) {
        if(value<this.value){
            if(this.left==null){
                return false;
            }
            return this.left.contain(value);
        }

        if(value>this.value){
            if(this.right==null){
                return false;
            }
            return this.right.contain(value);
        }
        return true;
    }

    public int length(){
        int a = (this.left == null) ? 0 : this.left.length();
        int b = (this.right == null) ? 0 : this.right.length();
        return a + b + 1;

    }
    public int height(){
        int a = (this.left == null) ? 1 : this.left.height() + 1;
        int b = (this.right == null) ? 1 : this.right.height() + 1;
        return (a>b)? a : b;
    }
    
}
