#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	long int i;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i,
		       Py_TYPE(list->ob_item[i])->tp_name);
}
