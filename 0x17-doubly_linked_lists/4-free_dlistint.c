#include "lists.h"

/**
 * free_dlistint - frees a doubly linked list
 * @head: head of list
 *
 * Return: nothing
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *ptr = head, *for_free = NULL;

	while (ptr != NULL)
	{
		for_free = ptr->next;
		free(ptr);
		ptr = for_free;
	}
}
