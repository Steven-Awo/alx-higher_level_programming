#include "lists.h"

/**
 * check_cycle - a function that checks if a linked list
 * contains a cycle in it
 * @list: the linked list to checked
 * Return: 1 (true) 0 (false)
 */

int check_cycle(listint_t *list)

{
	listint_t *slowr = list;
	listint_t *fastr = list;

	if (!list)
	{
	return (0);
	}
	while (slowr && fastr && fastr->next)
	{
	slowr = slowr->next;
	fastr = fastr->next->next;
	if (slowr == fastr)
	{
	return (1);
	}
	}
	return (0);
}
