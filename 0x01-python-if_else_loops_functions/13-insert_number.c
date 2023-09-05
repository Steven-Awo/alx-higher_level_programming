#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nod = *head, *newly;
	newly = malloc(sizeof(listint_t));
	if (newly == NULL)
	{
	return (NULL);
	}
	newly->n = number;
	if (nod == NULL || nod->n >= number)
	{
	newly->next = nod;
	*head = newly;
	return (newly);
	}
	while (nod && nod->next && nod->next->n < number)
		nod = nod->next;
	newly->next = nod->next;
	nod->next = newly;
	return (newly);
}
