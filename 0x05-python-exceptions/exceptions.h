#ifndef EXCEPTIONS_H
#define EXCEPTIONS_H

#include <stdio.h>
#include <Python.h>

int safe_print_list(int *my_list, int size, int x);
int safe_print_integer(int value);
int safe_print_list_integers(int *my_list, int size, int x);
float safe_print_division(int a, int b);
int *list_division(int *my_list_1, int *my_list_2, int size);
void raise_exception();
void raise_exception_msg(const char *message);
int safe_print_integer_err(int value);
void safe_function(void (*fct)(), ...);

void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

#endif /* EXCEPTIONS_H */
