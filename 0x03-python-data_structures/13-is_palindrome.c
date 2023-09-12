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
	listint_t *fast;
	listint_t *slow;
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *tmp = NULL;
	int palindrome = 1;

	if (!*head)
		return (palindrome);

	fast = *head;
	slow = *head;
	while (fast && fast->next)
	{
		prev = slow; /* node before slow */
		fast = fast->next->next;
		slow = slow->next;
		next = slow; /* node after slow */
	}

	prev = slow;
	while (prev)
	{
		tmp = prev;
		prev = next;
		next->next = tmp;
		next = prev->next;
	}

	tmp = *head;
	while (tmp != slow)
	{
		if (tmp->n != next->n)
		{
			palindrome = 0;
			break;
		}
		tmp = tmp->next;
		next = next->next;
	}

	while (next != slow)
	{
		tmp = next;
		next = prev;
		prev->next = tmp;
		prev = next->next;
	}

	return (palindrome);
}
