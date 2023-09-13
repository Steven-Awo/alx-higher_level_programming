#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - A function that prints bytes info
 * @p: the python object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *stringg;
	long int sizez, x, limits;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
	printf("  [ERROR] Invalid Bytes Object\n");
	return;
	}
	sizez = ((PyVarObject *)(p))->ob_size;
	stringg = ((PyBytesObject *)p)->ob_sval;
	printf("  sizez: %ld\n", sizez);
	printf("  trying stringg: %s\n", stringg);
	if (sizez >= 10)
		limits = 10;
	else
		limits = sizez + 1;
	printf("  first %ld bytes:", limits);
	for (x = 0; x < limits; x++)
		if (stringg[x] >= 0)
			printf(" %02x", stringg[x]);
		else
			printf(" %02x", 256 + stringg[x]);
	printf("\n");
}

/**
 * print_python_list - the function that prints list info
 * @p: the python object
 * Return: void
 */
void print_python_list(PyObject *p)

{
	long int sizez, x;
	PyListObject *list;
	PyObject *obj;

	sizez = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", sizez);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (x = 0; x < sizez; x++)
	{
	obj = ((PyListObject *)p)->ob_item[x];
	printf("Element %ld: %s\n", x, ((obj)->ob_type)->tp_name);
	if (PyBytes_Check(obj))
	{
	print_python_bytes(obj);
	}
	}
}
