#include <Python.h>

/**
 * print_python_list_info - prints some basic info about python lists.
 * @p: python object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int alloc;
	Py_ssize_t size, i;
	PyListObject *obj = (PyListObject *)p;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", (int) size);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < size; i++)
	{
		PyObject *item;

		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", (int) i, Py_TYPE(item)->tp_name);
	}
}
