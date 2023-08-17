#include "lists.h"

/**
 * insert_dnodeint_at_index - inserts new node at index
 * @h: head of list
 * @idx: index value
 * @n: value to be added
 *
 * Return: address of new node
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	int just_before_idx = 0, count = 0;
	dlistint_t *ptr, *new_ptr = NULL;

	if (idx == 0)
	{

	}
	just_before_idx = idx - 1;
	ptr = *h;
	new_ptr = (dlistint_t *) malloc(sizeof(dlistint_t));
	if (new_ptr == NULL)
	{
		printf("Malloc error\n");
		return (NULL);
	}
	new_ptr->n = n;
	while (ptr != NULL)
	{
		if (count == just_before_idx)
		{
			new_ptr->next = ptr->next;
			ptr->next = new_ptr;
			new_ptr->prev = ptr;
			return (new_ptr);
		}
		++count;
		ptr = ptr->next;
	}
	return (NULL);
}
