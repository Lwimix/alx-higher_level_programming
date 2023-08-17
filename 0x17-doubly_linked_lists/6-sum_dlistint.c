#include "lists.h"

/**
 * sum_dlistint - calculates sum of values in list
 * @head: head of list
 *
 * Return: sum of all values
 */
int sum_dlistint(dlistint_t *head)
{
	int added = 0;
	dlistint_t *cpy_list = head;

	while (cpy_list != NULL)
	{
		added += cpy_list->n;
		cpy_list = cpy_list->next;
	}
	return (added);
}
