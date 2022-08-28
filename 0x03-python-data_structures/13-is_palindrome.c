#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: the address of the first element in the list
 * Return: 1, if it is a palindrome and 0 if otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *last_element, *first_element;
	int size = 0, i = 0;

	if (!head)
		return (0);
	current = *head;
	if (!current)
		return (1);
	size = 1;
	while (current->next)
	{
		current = current->next;
		size++;
	}
	current = *head;
	while (i < size / 2)
	{
		int last_elem = size - i - 1, first_elem = i;
		int j;

		first_element = current;
		last_element = current;
		for (j = 0; j < last_elem + 1; j++)
		{
			if (j != first_elem)
				first_element = first_element->next;
			if (j != last_elem)
				last_element = last_element->next;
		}
		if (last_element->n != first_element->n)
			return (0);
		i++;
	}
	return (1);
}
