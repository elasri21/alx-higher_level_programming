#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: head of the list
 * Return: 1 on success.0 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *front_l;
int length = 0, j = 0;
front_l = *head;
while (front_l != NULL)
{
length++;
front_l = front_l->next;
}
if (length > 0)
{
int ns[length], i = 0, h = length - 1;
front_l = *head;
while (front_l != NULL)
{
ns[j] = front_l->n;
j++;
front_l = front_l->next;
}
while (i < h)
{
if (ns[i] != ns[h])
return (0);
else
{
i++;
h--;
continue;
}
}
}
return (1);
}
