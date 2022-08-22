#include "lists.h"

/**
 * check_cycle - checks if a given list is a cycle
 * @list: list to be evaluated
 * Return: 0 or 1 based on the condition
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;
	while (current != NULL)
	{
		current = current->next;
		if (current == list)
			return (1);
	}
	return (0);
}
