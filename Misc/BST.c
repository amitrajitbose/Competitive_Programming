/*C Program to Implement all BST operations*/

#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
 
typedef struct nd
{
    int data;
    struct nd *left, *right;
}node;

node *root=NULL;

//Function to search a value/node in a BST
node* searchElement(node *root, int value)
{
    if(root==NULL){
        printf("\nNO MATCH FOUND");
    	return root;
    }
    else if(root->data>value){
    	searchElement(root->left,value);
    }
    else if(root->data<value){
    	searchElement(root->right,value);
    }
    else if(root->data==value){
        printf("\nMATCH FOUND");
    }
}

//Function to insert a new node/value
node* insert(node *root, int value)
{
	if(root==NULL){
		//Allocate memory
		node *temp=(node *)malloc(sizeof(node));
		temp->data=value;
		temp->left=temp->right=NULL;
		return temp; //this line proved to be damn important
	}
	else{
		if(value<root->data){
			root->left=insert(root->left,value);
		}
		else{
			root->right=insert(root->right,value);
		}
	}
	return root;
}

//Function to display inorder
void displayInorder(node *root){
	if (root != NULL)
    {
        displayInorder(root->left);
        printf("%d ", root->data);
        displayInorder(root->right);
    }
}

//Defining the minValueNode() function
//Returns the minimum value from a sub-tree

node* minValueNode(node* nod)
{
    node* current = nod;
 
    // loop down to find the leftmost leaf
    while (current->left != NULL)
        current = current->left;
 
    return current;
}

//Defining the maxValueNode() function
//Returns the maximum value from a sub-tree

node* maxValueNode(node* nod)
{
    node* current = nod;
 
    // loop down to find the leftmost leaf
    while (current->right != NULL)
        current = current->right;
 
    return current;
}

//Function to find height of a sub-tree
int height(node *root){
    if(!(root))
        return 0;
    if(!root->left && !root->right)
        return 0;
    int l,r;
    l=height(root->left);
    r=height(root->right);
    return (1+((l>r)?l:r));
}


//Function to delete a node
node *delete(node *root, int val){
	if(root==NULL)
		return root;
	else{
		if(val<root->data){
			root->left=delete(root->left,val);
		}
		else if(val>root->data){
			root->right=delete(root->right,val);
		}
		else{
			//thus traversal process has completed
			//i.e. val=root->data

			//for one or zero child
			if(root->left==NULL){
				node *temp=root->right;
				free(root);
				return (temp);
			}
			else if(root->right==NULL){
				node *temp=root->left;
				free(root);
				return (temp);
			}
			//now for two child node
			//we do not need any else block since all blocks have 'return'
			//here, we will need the inorder successor(i.e. smallest val of right sub tree)

			node *temp=minValueNode(root->right);
			root->data=temp->data;
			root->right=delete(root->right,temp->data);
		}
		return root;
	}
}
//Function to count number of nodes, recursive
int count(node *root)
{
    if(root==NULL)
        return 0;
    else
        return(count(root->left) + count(root->right) + 1);
}

//Function to find total number of external nodes
int totalExternalNodes(node *tree)
{
    if(tree==NULL)
        return 0;
    else if((tree->left==NULL) && (tree->right==NULL))
        return 1;
    else
        return (totalExternalNodes(tree->left) + totalExternalNodes(tree->right));
}

//Function to find total number of internal nodes
int totalInternalNodes(node *tree)
{
    if((tree==NULL) || ((tree->left==NULL) && (tree->right==NULL)))
        return 0;
    else
        return (totalInternalNodes(tree->left)+ totalInternalNodes(tree->right) + 1);
}

//Function to delete the entire tree and free memory
node *deleteBST(node *root){
    if(root){
        deleteBST(root->left);
        deleteBST(root->right);
        free(root);
    }
}

//Function to mirror a BST
node *mirror(node *root){
    node *temp;
    if(root!=NULL){
        mirror(root->left);
        mirror(root->right);
        temp=root->left;
        root->left=root->right;
        root->right=temp;
    }
    return root;
}


int main(){

    root = insert(root, 50);
    root = insert(root, 30);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 70);
    root = insert(root, 60);
    root = insert(root, 80);

    displayInorder(root);
    printf("\n");
    
    
    root = delete(root,70);

    displayInorder(root);
    printf("\n");
    
    searchElement(root,60);
    
    printf("\nSmallest Node: %d",minValueNode(root)->data);
    printf("\nLargest Node: %d",maxValueNode(root)->data);
    
    printf("\nTOTAL NODE COUNT: %d",count(root));
    printf("\nINTERNAL NODE COUNT: %d",totalInternalNodes(root));
    printf("\nEXTERNAL NODE COUNT: %d",totalExternalNodes(root));
    
    printf("\nHeight: %d",height(root));
    
    root = mirror(root);
    printf("\nMirrored BST Infix Order: ");
    displayInorder(root);
    
    deleteBST(root); //Last Function Always
    printf("\nBST DELETED");
    
    getch();
    return 0;
}
