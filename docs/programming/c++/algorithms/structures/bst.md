---
description: BST
---

# Drzewa przeszukiwań binarnych

## Opis problemu

{% content-ref url="../../../../algorithms/structures/drzewa-przeszukiwan-binarnych.md" %}
[drzewa-przeszukiwan-binarnych.md](../../../../algorithms/structures/drzewa-przeszukiwan-binarnych.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```cpp
#include <iostream>

using namespace std;

class BST {
    struct node {
        int value;
        node *left;
        node *right;
    };

    node *root;
public:
    BST() {
        root = nullptr;
    }

    node* get_root() {
        return root;
    }

    void insert(int value) {
        node *new_node = new node();
        new_node->value = value;
        new_node->left = nullptr;
        new_node->right = nullptr;

        if(root == nullptr) {
            root = new_node;
            return;
        }

        node *current, *parent;
        current = root;
        while(current != nullptr) {
            parent = current;
            if(value < current->value) {
                current = current->left;
            } else {
                current = current->right;
            }
        }

        if(value < parent->value) {
            parent->left = new_node;
        } else {
            parent->right = new_node;
        }
    }

    void inorder(node *current) {
        if(current == nullptr) {
            return;
        }

        inorder(current->left);
        cout << current->value << " ";
        inorder(current->right);
    }

    void preorder(node *current) {
        if(current == nullptr) {
            return;
        }

        cout << current->value << " ";
        preorder(current->left);
        preorder(current->right);
    }

    void postorder(node *current) {
        if(current == nullptr) {
            return;
        }

        postorder(current->left);
        postorder(current->right);
        cout << current->value << " ";
    }

    void clear(node *current) {
        if(current == nullptr) {
            return;
        }

        clear(current->left);
        clear(current->right);
        delete current;
    }

    ~BST() {
        clear(root);
    }
};

int main() {
    int array[7] = {20, 10, 30, 5, 15, 25, 35};
    BST bst = BST();

    for(auto el : array) {
        bst.insert(el);
    }

    cout << "Inorder: ";
    bst.inorder(bst.get_root());
    cout << endl;

    cout << "Preorder: ";
    bst.preorder(bst.get_root());
    cout << endl;

    cout << "Postorder: ";
    bst.postorder(bst.get_root());
    cout << endl;
    
    return 0;
}
```
{% endcode %}

### Opis implementacji

![Przykładowe drzewo wykorzystane w implementacji](<../../../../.gitbook/assets/image (10).png>)

{% embed url="http://graphonline.ru/en/?graph=iTYRccYJVswEnVGe" %}
