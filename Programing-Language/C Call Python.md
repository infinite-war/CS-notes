场景：性能不敏感，且Python有成熟的效果不错的库

在Ubuntu上，能比较简单的完成，下面是一个简单的Demo
```cpp
// python_demo.c
// g++ python_demo.c -lpython3.10 && ./a.out
#include <python3.10/Python.h>
#include <stdio.h>

void handle_err(int cnt, ...) __attribute__((noreturn));
void handle_err(int cnt, ...) {
    PyErr_Print();

    va_list args;
    va_start(args, cnt);
    for (int i = 0; i < cnt; ++i) {
        PyObject *arg = va_arg(args, PyObject *);
        Py_DECREF(args);
    }
    exit(1);
}

int main() {
    Py_Initialize();
    printf("Init Python Interpreter.\n");

    printf("import python module: rich.\n");
    PyObject *module = PyImport_ImportModule("rich");
    if (module == NULL) { handle_err(0); }

    // printf("Get Python Object.\n");
    // PyObject *obj = PyObject_GetAttrString(module, "module name");
    // if (obj == NULL) { handle_err(1, module); }

    printf("Get Python function.\n");
    PyObject *func = PyObject_GetAttrString(module, "print");
    if (func == NULL) { handle_err(1, module); }

    printf("function args.\n");
    PyObject *args = PyTuple_New(1); // 参数: 个数
    PyTuple_SetItem(args, 0, PyLong_FromLong(42));
    // 参数: 函数参数对象, 位置, 值(要转换下)

    printf("Call.\n");
    PyObject *result = PyObject_CallObject(func, args);

    // printf("Handle Return Value.\n");
    // if (result != NULL) {
    //     int ret = PyLong_AsLong(result);
    //     if (ret == -1 && PyErr_Occurred()) {
    //         handle_err(4, module, func, args, result);
    //     } else {
    //     }
    // } else {
    //     handle_err(4, module, func, args, result);
    // }

    printf("Release.\n");
    Py_DECREF(module);
    Py_DECREF(func);
    Py_DECREF(args);
    Py_DECREF(result);

    printf("Close.\n");
    Py_Finalize();

    return 0;
}


#include <Python.h>
#include <stdio.h>
int main() {
    Py_SetPath(
        L"D:\\Scoop\\apps\\python310\\current\\Lib;D:\\Scoop\\apps\\python310\\current\\DLLs;D:\\Scoop\\apps\\python310\\current\\libs;D:\\Scoop\\apps\\python310\\current\\Lib\\site-packages");

    Py_Initialize();

    PyObject *sys = PyImport_ImportModule("sys");
    if (sys == NULL) {
        PyErr_Print();
        return 1;
    }
    PyObject *path = PyObject_GetAttrString(sys, "path");
    if (path == NULL) {
        PyErr_Print();
        Py_DECREF(sys);
        return 1;
    }
    for (int i = 0; i < PyList_Size(path); ++i) {
        PyObject *item = PyList_GetItem(path, i);
        if (item != NULL) {
            const char *str = PyUnicode_AsUTF8(item);
            printf("%s\n", str);
        }
    }

    Py_DECREF(sys);
    Py_DECREF(path);

    PyObject *module = PyImport_ImportModule("rich");
    if (module == NULL) { PyErr_Print(); }

    printf("Get Python function.\n");
    PyObject *func = PyObject_GetAttrString(module, "print");
    // if (func == NULL) { handle_err(1, module); }

    printf("function args.\n");
    PyObject *args = PyTuple_New(1); // 参数: 个数
    PyTuple_SetItem(args, 0, PyLong_FromLong(42));
    // 参数: 函数参数对象, 位置, 值(要转换下)

    printf("Call.\n");
    PyObject *result = PyObject_CallObject(func, args);

    return 0;
}
```


