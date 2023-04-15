#ifndef TREE_H // warunek sprawdzający, czy nagłówek został już dołączony
#define TREE_H // jeśli nie, to definiujemy stałą TREE_H

#include "node.h"

// deklaracje funkcji
struct Tree;
typedef struct Tree Tree;
Tree* new_tree();
bool tree_add(Tree* tree, int value);
bool tree_contain(Tree* tree, int value);
int tree_length(Tree* tree);
int tree_height(Tree* tree);
void tree_remove(Tree* tree);

#endif // TREE_H