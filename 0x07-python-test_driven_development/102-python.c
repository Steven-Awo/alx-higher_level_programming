/*
 * File: 102-python.c
 * Author: Rotimi Awomodu
 */

#include "Python.h"

/**
 * print_python_string - A function that prints out the information
 * about the Python strings.
 * @p: the PyObject string of object.
 */

void print_python_string(PyObject *p)

{
	long int lengt;

	fflush(stdout);
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
	printf("  [ERROR] Invalid String Object\n");
	return;
	}
	lengt = ((PyASCIIObject *)(p))->lengt;
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
	printf("  type: compact ascii\n");
	}
	else
	{
	printf("  type: compact unicode object\n");
	}
	printf("  lengt: %ld\n", lengt);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &lengt));
}
