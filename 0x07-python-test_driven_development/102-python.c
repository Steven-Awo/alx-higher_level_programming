#include "Python.h"

/**
 * print_python_string - A function that prints out the information
 * about the Python strings.
 * @p: the PyObject string object.
 */

void print_python_string(PyObject *p)

{
	Py_ssize_t length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
        printf("  [ERROR] Invalid String Object\n");
        return;
	}
	length = ((PyUnicodeObject *)p)->length;
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
	printf("  type: compact ascii\n");
	}
	else
	{
	printf("  type: compact unicode object\n");
	}
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}

