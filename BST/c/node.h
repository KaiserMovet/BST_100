#ifndef NODE_H // warunek sprawdzający, czy nagłówek został już dołączony
#define NODE_H // jeśli nie, to definiujemy stałą NODE_H

#include <stdbool.h>

// deklaracje funkcji
struct Node;
typedef struct Node Node;
Node* new_node(int value);
bool node_add(Node *node, int value);
bool node_contain(Node *node, int value);
int node_length(Node *node);
int node_height(Node *node);
void node_remove(Node *node);

#endif // NODE_H