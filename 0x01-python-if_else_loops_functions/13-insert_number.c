#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;

	tmp = *head;
	if (head && tmp)
	{

		if (tmp->n > new->n)
		{
			new->next = tmp;
			*head = new;
		}
		else
		{

			while (tmp->next)
			{
				if (tmp->next->n < new->n)
				{
					tmp = tmp->next;
				}
				else
				{
					break;
				}
			}
			if (tmp)
			{
				new->next = tmp->next;
			}
			else
			{
				new->next = NULL;
			}
			tmp->next = new;
		}
	}
	else
	{
		*head = new;
		(*head)->next = NULL;
	}

	return (new);
}
