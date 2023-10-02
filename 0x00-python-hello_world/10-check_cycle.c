#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check for sycles in a linked list
 * @list: list to be checked
 * Return: integer
 */

int check_cycle(listint_t *list)
{
listint_t *rabbit = list;
listint_t *turtle = list;
if (!list)
return (0);
while (turtle && rabbit && rabbit->next)
{
turtle = turtle->next;
rabbit = rabbit->next->next;
if (turtle == rabbit)
return (1);
}
return (0);
}
