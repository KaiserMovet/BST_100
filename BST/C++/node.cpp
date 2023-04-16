#include <algorithm>

class Node{
    public: int value;
    private: Node* left;
    private: Node* right;

    public: Node(int value) : value(value), left(nullptr), right(nullptr){}

    public: bool add(int value){
        if(value < this->value){
            if(this->left == nullptr){
                this->left = new Node(value);
                return true;
            }
            return this->left->add(value);
        }

        if(value > this->value){
            if(this->right == nullptr){
                this->right = new Node(value);
                return true;
            }
            return this->right->add(value);
        }

        return false;
    }

    public: bool contain(int value){
        if(value < this->value){
            if(this->left == nullptr) return false;
            return this->left->contain(value);
        }

        if(value > this->value){
            if(this->right == nullptr) return false;
            return this->right->contain(value);
        }

        return true;
    }

    public: int length(){
        int left_len = 0;
        if(this->left != nullptr){
            left_len = this->left->length();
        }

        int right_len = 0;
        if(this->right != nullptr){
            right_len = this->right->length();
        }
        return left_len + right_len + 1;
    }

    public: int height(){
        int left_height = 0;
        if(this->left != nullptr){
            left_height = this->left->height();
        }

        int right_height = 0;
        if(this->right != nullptr){
            right_height = this->right->height();
        }

        return 1 + std::max(left_height, right_height);
    }


};