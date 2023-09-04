#include "lists.h"

/**
 * check_cycle - checks for a cycle in linked list
 *
 * @list: list head
 *
 * Return: 1 if there's a cycle 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
