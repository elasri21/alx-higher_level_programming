#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head:list head
 * @number:number to insert
 * Return: new node on success. NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *currnode = *head, *newnode;
newnode = malloc(sizeof(listint_t));
if (newnode == NULL)
return (NULL);
newnode->n = number;
if (currnode == NULL || currnode->n >= number)
{
newnode->next = currnode;
*head = newnode;
return (newnode);
}
while (currnode && currnode->next && currnode->next->n < number)
currnode = currnode->next;
newnode->next = currnode->next;
currnode->next = newnode;
return (newnode);
}
