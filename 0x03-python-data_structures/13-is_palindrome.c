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
	listint_t *tmp = NULL;
	listint_t *tmp2 = NULL;
	int palindrome = 1;

	if (!(*head))
		return (palindrome);

	fast = *head;
	slow = *head;
	while (fast && fast->next)
	{
		prev = slow;
		fast = fast->next->next;
		slow = slow->next;
	}

	if (fast == slow)
	{
		return (palindrome);
	}
	while (slow)
	{
		tmp2 = slow->next;
		slow->next = tmp;
		tmp = slow;
		slow = tmp2;
	}

	slow = tmp;
	tmp2 = *head;
	while (slow && tmp2)
	{
		if (slow->n != tmp2->n)
		{
			palindrome = 0;
			break;
		}
		slow = slow->next;
		tmp2 = tmp2->next;
	}

	slow = tmp;
	tmp = NULL;
	tmp2 = NULL;
	while (slow)
	{
		tmp2 = slow->next;
		slow->next = tmp;
		tmp = slow;
		slow = tmp2;
	}
	prev->next = tmp;

	return (palindrome);
}
