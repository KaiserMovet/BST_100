#include <stdlib.h>
#include "node.h"
typedef struct Tree Tree;

struct Tree{
    Node *root;
};

Tree* new_tree(){
    struct Tree* tree = (Tree*)malloc(sizeof(struct Tree));
    tree->root = NULL;
    return tree;
}

bool tree_add(Tree* tree, int value){
    if(tree->root == NULL){
        tree->root = new_node(value);
        return true;
    }
    return node_add(tree->root,value);
}

bool tree_contain(Tree* tree, int value){
    if(tree->root == NULL) return false;
    return node_contain(tree->root, value);
}

int tree_length(Tree* tree){
    if(tree->root == NULL) return 0;
    return node_length(tree->root);
}

int tree_height(Tree* tree){
    if(tree->root == NULL) return 0;
    return node_height(tree->root);
}

void tree_remove(Tree* tree){
    if(tree->root != NULL){
        node_remove(tree->root);
        free(tree);
    }
}
