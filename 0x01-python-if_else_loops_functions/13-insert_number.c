#include "lists.h"

/**
 * add_node - inserts a node in a list
 * @node: the node to make
 * @num: the number
 * Return: void
 */
void add_node(listint_t **node, int num)
{
	listint_t *current;

	current = malloc(sizeof(listint_t));
	current->n = num;
	current->next = NULL;
	*node = current;
}

/**
 * insert_node - inserts a number into a sorted list
 * @head: the list
 * @number: the number to be inserted
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL, *previous = NULL, *new = NULL;

	if (head == NULL)
	{
		add_node(&(*head), number);
		return (*head);
	}
	current = *head;
	if (current == NULL)
	{
		add_node(&(*head), number);
		return (*head);
	}
	while (current != NULL)
	{
		int num = current->n;

		if (num > number)
		{
			new = malloc(sizeof(listint_t));
			new->n = number;
			if (previous)
				previous->next = new;
			else
				*head = new;
			new->next = current;
			return (new);
		}
		else if (current->next == NULL)
		{
			new = malloc(sizeof(listint_t));
			new->n = number;
			current->next = new;
			return (new);
		}
		previous = current;
		current = current->next;
	}
	return (NULL);
}
