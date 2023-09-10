#include "lists.h"

listint_t *revseerse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * revseerse_listint - A function of that revseerses a singly-linked
 * listint_t list.
 * @head: starting nod of a pointer of the list to revseerse.
 * Return: revseersed list.
 */
listint_t *revseerse_listint(listint_t **head)
{
	listint_t *nod = *head, *next, *prevse = NULL;

	while (nod)
	{
	next = nod->next;
	nod->next = prevse;
	prevse = nod;
	nod = next;
	}
	*head = prevse;
	return (*head);
}

/**
 * is_palindrome - A function that checks if a singly linked list is
 * actually a palindrome.
 * @head: the head pointer of the linked list.
 * Return: If the linked list isn't a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *revse, *mid;
	size_t size = 0, x;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp = *head;
	while (tmp)
	{
	size++;
	tmp = tmp->next;
	}
	tmp = *head;
	for (x = 0; x < (size / 2) - 1; x++)
		tmp = tmp->next;
	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);
	tmp = tmp->next->next;
	revse = revseerse_listint(&tmp);
	mid = revse;
	tmp = *head;
	while (revse)
	{
	if (tmp->n != revse->n)
		return (0);
	tmp = tmp->next;
	revse = revse->next;
	}
	revseerse_listint(&mid);
	return (1);
}
