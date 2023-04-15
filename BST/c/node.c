#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
typedef struct Node Node;

struct Node{
    int value;
    Node *left;
    Node *right;

};

Node* new_node(int value){
    struct Node* node = (Node*)malloc(sizeof(struct Node));
    node->value = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

bool node_add(Node *node, int value){
    if(value < node->value){
        if(node->left == NULL){
            node->left = new_node(value);
            return true;
        }
        return node_add(node->left,value);
    }

    if(value > node->value){
        if(node->right == NULL){
            node->right = new_node(value);
            return true;
        }
        return node_add(node->right,value);
    }

    return false;
    }

bool node_contain(Node *node, int value){
    if(value < node->value){
        if(node->left == NULL) return false;
        return node_contain(node->left,value);
    }

    if(value > node->value){
        if(node->right == NULL) return false;
        return node_contain(node->right,value);
    }

    return true;
}

int node_length(Node *node){
    int left_len = 0;
    if(node->left != NULL){
        left_len = node_length(node->left);
    }

    int right_len = 0;
    if(node->right != NULL){
        right_len = node_length(node->right);
    }
    return left_len + right_len + 1;
}

int node_height(Node *node){
    int left_height = 0;
    if(node->left != NULL){
        left_height = node_height(node->left);
    }

    int right_height = 0;
    if(node->right != NULL){
        right_height = node_height(node->right);
    }
    if(left_height>right_height) return left_height + 1;
    return right_height + 1;
}

void node_remove(Node *node){
    if(node->left != NULL){
        node_remove(node->left);
    }
    if(node->right != NULL){
        node_remove(node->right);
    }
    free(node);
    
}