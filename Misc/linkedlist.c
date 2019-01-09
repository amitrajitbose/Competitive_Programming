//IMPLEMENTATION OF LINKED LIST AND ALL OF ITS FUNCTIONS
#include<stdio.h>
#include<stdlib.h>
#include<conio.h> //Not for LINUX
typedef struct nd{
    int data;
    struct nd *link;
}node;
node *start=NULL;
void display() // displaying the list
{
    node *p;
    if(start==NULL)
    {
        printf("List is empty!");
        exit(0);
    }
    p = start;
    while(p!=NULL)
    {
        printf("%d ",p->data);
        p = p->link;
    }
    printf("\n");
}
void addatend() // inserting an element at the end position
{
    node *p,*temp;
    int val;
    printf("Enter the value..");
    scanf("%d",&val);
    temp = (node*)malloc(sizeof(node)); // creation of a node
    temp->data = val;
    p = start;
    while(p->link!=NULL)
        p = p->link;
    p->link = temp;
    temp->link = NULL;
}
void addatbeg() // inserting an element at the begining
{
    node *temp;
    int val;
    printf("Enter the value..");
    scanf("%d",&val);
    temp = (node*)malloc(sizeof(node)); // creation of a node
    temp->data = val;
    temp->link = start;
    start = temp;
}
void addatpos() // inserting an element at a given position
{
    node *p,*temp;
    int i,val,pos;
    printf("Enter the value..");
    scanf("%d",&val);
    printf("Enter the position..");
    scanf("%d",&pos);
    temp = (node*)malloc(sizeof(node)); // creation of a node
    temp->data = val;
    p = start;
    for(i=1;i<pos-1 && p!=NULL; i++)
        p = p->link;
    if(p==NULL)
    printf("There are less than %d elements!\n",pos);
    else
    {
        temp->link = p->link;
        p->link = temp;
    }
}
void delatbeg() // deleting the 1st node
{
    node *p;
    if(start==NULL)
    {
        printf("List is empty!");
        exit(1);
    }
    p = start;
    start = start->link;
    free(p);
}
void delatend() // deleting the last node
{
    node *p,*q;
    if(start==NULL)
    {
        printf("List is empty!");
        exit(2);
    }
    p = start;
    while(p->link!=NULL)
    {
        q = p; // q holds the previous node
        p = p->link;
    }
    q->link = NULL;
    free(p);
}
void delatpos() // deleting node from a given position
{
    node *p,*q;
    int i,pos;
    printf("From which position?..");
    scanf("%d",&pos);
    if(start==NULL)
    {
        printf("List is empty!");
        exit(3);
    }
    p = start;
    for(i=1;i<pos && p!=NULL; i++)
    {
        q = p; // q holds the previous node
        p = p->link;
    }
    if(p==NULL)
        printf("There are less than %d elements!\n",pos);
    else
    {
        q->link = p->link;
        free(p);
    }
}
int main(){
    int a=1;
    node *start=NULL;
    while(a==1){
        int ch;
        printf("\nPress 0 To EXIT");
        printf("\nPress 1 To CREATE List");
        printf("\nPress 2 To ADD AT BEGINNING");
        printf("\nPress 3 To ADD AT END");
        printf("\nPress 4 To ADD AT ANY POSITION");
        printf("\nPress 5 To DELETE FROM BEGINNING");
        printf("\nPress 6 To DELETE FROM END");
        printf("\nPress 7 To DELETE FROM ANY POSITION");
        printf("\nPress 8 To DISPLAY LIST");
        printf("\nEnter Choice: ");
        scanf("%d",&ch);
        switch(ch)
        {
            case 0: a=0;break;
            case 1: addatbeg();break;
            case 2: addatbeg();break;
            case 3: addatend();break;
            case 4: addatpos();break;
            case 5: delatbeg();break;
            case 6: delatend();break;
            case 7: delatpos();break;
            case 8: display();break;
            default:printf("\nINVALID CHOICE");
        }
    }
    return 0;
}
