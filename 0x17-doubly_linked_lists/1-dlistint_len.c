#include "lists.h"

/**
 * dlistint_len - calculates number of elements in a list
 * @h: head of the linked list
 *
 * Return: the number of elements
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;
	dlistint_t *ptr = (dlistint_t *)h;

	while (ptr != NULL)
	{
		++count;
		ptr = ptr->next;
	}
	return (count);
}
