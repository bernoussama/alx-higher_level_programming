#include "lists.h"
#include <stdlib.h>

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
	unsigned int *arr;
	unsigned int *tail;
	unsigned int *top;
	unsigned int offset;
	int palindrome = 0;

	if (*head == NULL)
	{
		return 0;
	}

	current = *head;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	arr = malloc(sizeof(unsigned int) * n);
	if (!arr)
	{
		free(arr);
		return (0);
	}
	tail = &arr[n - 1];

	current = *head;
	offset = 0;
	while (current != NULL)
	{
		arr[offset++] = current->n;
		current = current->next;
	}

	palindrome = 1;
	offset = 0;
	while (offset < n / 2)
	{
		if (top[offset] != tail[-offset])
		{
			palindrome = 0;
			return (palindrome);
		}
		offset++;
	}

	free(arr);
	return (palindrome);
}
