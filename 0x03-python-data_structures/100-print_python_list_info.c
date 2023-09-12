#include "/usr/include/python3.4"
#include <stdio.h>

void print_python_list_info(PyObject *p);

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;
	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		printf("[*] Size of the Python List = %ld", size);
		allocated = Py_REFCNT(p);
		printf("[*] Allocated = %ld", allocated);
		for (i = 0; i < size; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %ld: %s", i, Py_TYPE(item));
		}
	}
}
