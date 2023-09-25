/*
 * File: 103-python.c
 * Auth: Type Your Name Here
 */

#include <Python.h>

void print_python_list(PyObject *p);

void print_python_float(PyObject *p);

void print_python_bytes(PyObject *p);

/**
 * print_python_list - A function that prints basic inform about the
 * Python lists.
 * @p: the object of the PyObject lists.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t sizez, allocc, x;
	const char *typee;
	PyListObject *lists = (PyListObject *)p;
	PyVarObject *varr = (PyVarObject *)p;

	sizez = varr->ob_size;
	allocc = lists->allocated;
	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
	printf("  [ERROR] Invalid List Object\n");
	return;
	}
	printf("[*] Size of the Python List = %ld\n", sizez);
	printf("[*] Allocated = %ld\n", allocc);
	for (x = 0; x < sizez; x++)
	{
	typee = lists->ob_item[x]->ob_type->tp_name;
	printf("Element %ld: %s\n", x, typee);
	if (strcmp(typee, "bytes") == 0)
		print_python_bytes(lists->ob_item[x]);
	else if (strcmp(typee, "float") == 0)
		print_python_float(lists->ob_item[x]);
	}
}

/**
 * print_python_bytes - A function that prints the basic information
 * about Python byte objects.
 * @p: the byte of the PyObject lists.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t sizez, x;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
	printf("  [ERROR] Invalid Bytes Object\n");
	return;
	}
	printf("  sizez: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size >= 10)
		sizez = 10;
	else
		sizez = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %ld bytes: ", sizez);
	for (x = 0; x < sizez; x++)
	{
	printf("%02hhx", bytes->ob_sval[x]);
	if (x == (sizez - 1))
		printf("\n");
	else
		printf(" ");
	}
}

/**
 * print_python_float - A function that prints that basic information
 * about Python float objects.
 * @p: A float of the PyObject lists.
 */

void print_python_float(PyObject *p)

{
	char *bufferr = NULL;

	PyFloatObject *floatt_obj = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
	printf("  [ERROR] Invalid Float Object\n");
	return;
	}
	bufferr = PyOS_double_to_string(floatt_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", bufferr);
	PyMem_Free(bufferr)
}
