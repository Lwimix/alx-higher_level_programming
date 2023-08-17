#include "lists.h"

/**
 * add_dnodeint_end - adds node at end of linked list
 * @head: head node of list
 * @n: value of node
 *
 * Return: address of new element
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_ptr = NULL, *ptr = NULL;

	new_ptr = (dlistint_t *) malloc(sizeof(dlistint_t));
	if (new_ptr == NULL)
	{
		printf("Malloc Error\n");
		return (NULL);
	}
	new_ptr->n = n;
	new_ptr->next = NULL;
	new_ptr->prev = NULL;
	if (*head == NULL)
	{
		*head = new_ptr;
		return (*head);
	}
	ptr = *head;
	while (ptr->next != NULL)
		ptr = ptr->next;
	ptr->next = new_ptr;
	new_ptr->prev = ptr;
	return (new_ptr);
}
