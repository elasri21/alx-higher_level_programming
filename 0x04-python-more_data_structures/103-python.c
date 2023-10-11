#include <Python.h>
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
/**
 * print_python_list - print info about py lists
 * @p: python object
 * Return: void
 */
void print_python_list(PyObject *p)
{
long int i, s;
PyListObject *p_l;
PyObject *p_o;
s = ((PyVarObject *)(p))->ob_size;
p_l = (PyListObject *)p;
printf("[*] Python list info\n";
printf("[*] Size of thePython List = %ld\n", s);
printf("[*] Allocated = %ld\n", p_l->allocated);
for (i = 0; i < s; i++)
{
p_o = ((PyListObject *)p)->ob_item[i];
printf("Element %ld: %s\n", ((p_o)->ob_type)->tp_name);
if (PyBytes_check(p_o))
print_python_bytes(p_o);
}
}
/**
 * print_python_bytes - print info about py bytes
 * @p: python object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
char *st;
long int s, i, l;
printf("[.] bytes object info\n");
if (!Py_bytes_check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
s = ((PyVarObject *)(p))->ob_size;
st = ((PyBytesObject *)p)->ob_sval;
if (s >= 10)
l = 10;
else
l = s + 1;
printf("  first %ld bytes:", l);
for (i = 0; i < l; i++)
{
if (st[i] >= 0)
printf(" %02x", st[i]);
else
printf(" %02x", 256 + st[i]);
}
printf("\n");
}
