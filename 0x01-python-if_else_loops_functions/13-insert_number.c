#include "lists.h"

/**
 * insert_node - inserts a number into a sorted list
 * @head: the list
 * @number: the number to be inserted
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL, *previous = NULL, *result;

	if (head == NULL)
		return (NULL);
	current = *head;
	if (current == NULL)
		add_nodeint_end(&current, number);
	while (current != NULL)
	{
		int num = current->n;

		if (num > number)
		{
			listint_t *new = malloc(sizeof(listint_t));

			if (new == NULL)
				return (NULL);
			new->n = number;
			if (previous)
				previous->next = new;
			new->next = current;
			result = current;
			break;
		}
		else if (current->next == NULL)
		{
			listint_t *new = malloc(sizeof(listint_t));

			new->n = number;
			new->next = NULL;
			current->next = new;
			result = new;
			break;
		}
		previous = current;
		current = current->next;
	}
	return (result);
}
