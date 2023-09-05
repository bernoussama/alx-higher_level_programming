#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;

	tmp = *head;
	if (tmp)
	{

		if (tmp->next)
		{
			while (tmp->next->n < new->n)
			{
				if (!tmp->next)
					break;
				tmp = tmp->next;
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
	else
	{
		*head = new;
		(*head)->next = NULL;
	}

	return (new);
}
