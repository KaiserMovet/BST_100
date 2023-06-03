class Tree{
    Node root;

    public Tree(){
        this.root = null;
    }

    public boolean add(int value){
        if(this.root == null){
            this.root = new Node(value);
            return true;
        }
        return this.root.add(value);
    }

    public boolean contain(int value){        
        if(this.root == null){
            return false;
        }
        return this.root.contain(value);
    }

    public int length(){
        if(this.root == null){
            return 0;
        }
        return this.root.length();
    }
    public int height(){
        if(this.root == null){
            return 0;
        }
        return this.root.height();
    }
}