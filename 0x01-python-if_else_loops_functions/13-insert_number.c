#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	if (!head || !*head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;

	tmp = *head;
	while (tmp->next->n < new->n)
	{
		tmp = tmp->next;
	}
	new->next = tmp->next;
	tmp->next = new;

	return (new);
}
