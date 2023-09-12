#include "lists.h"

/**
 * is_palindrome - check if linked list is palindrome
 *
 * @head: linked lists head
 *
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */
	// unsigned int *arr;
	unsigned int offset;

	if (*head == NULL)
	{
		return (1);
	}

	current = *head;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	unsigned int array[n];
	// arr = malloc(sizeof(unsigned int) * n);
	// if (!arr)
	// {
	// 	free(arr);
	// 	return (0);
	// }

	current = *head;
	offset = 0;
	while (current != NULL)
	{
		array[offset] = current->n;
		current = current->next;
		offset++;
	}

	offset = 0;
	while (offset <= n / 2)
	{
		if (array[offset] != array[n - 1 - offset])
		{
			return (0);
		}
		offset++;
	}

	// free(arr);
	return (1);
}
