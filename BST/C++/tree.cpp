#include "node.cpp"

class Tree{
    public: Node* root;

    public: Tree(): root(nullptr){}

    public: bool add(int value){
        if(this->root == nullptr){
            this->root = new Node(value);
            return true;
        }
        return this->root->add(value);
    }

    public: bool contain(int value){
        if(this->root == nullptr) return false;
        return this->root->contain(value);
    }

    public: int length(){
        if(this->root == nullptr) return 0;
        return this->root->length();
    }

    public: int height(){
        if(this->root == nullptr) return 0;
        return this->root->height();
    }
};