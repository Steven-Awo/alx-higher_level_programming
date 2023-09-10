#include <Python.h>
/**
 * print_python_list_info - A function that prints the basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int sizes, alloct, x;
	PyObject *obj;

	sizes = Py_SIZEs(p);
	alloct = ((PyListObject *)p)->allocated;
	printf("[*] Sizes of the Python List = %d\n", sizes);
	printf("[*] Allocated = %d\n", alloct);
	for (x = 0; x < sizes; x++)
	{
		printf("Element %d: ", x);
		obj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
