#include "lists.h"

/**
 * get_dnodeint_at_index - gets value at index
 * @head: head of list
 * @index: index value 
 *
 * Return: nth node
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int count = 0;
	dlistint_t *cpy_ptr = head;

	if (head == NULL)
		return (NULL);
	while (cpy_ptr != NULL)
	{
		if (count == index)
			return (cpy_ptr);
		++count;
		cpy_ptr = cpy_ptr->next;
	}
	return (NULL);
}
