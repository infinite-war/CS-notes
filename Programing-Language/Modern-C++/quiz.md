## +

```cpp
#include <iostream>

class Base {
    public:
        int a = 1;
        virtual void print(int n = 2) {
            std::cout << "Base: " << a + n << '\n';
        }
};

class Derive: public Base {
    public:
        int b = 3;
        virtual void print(int n = 10) {
            std::cout << "Derive: " << b + n << '\n';
        }
};

int main() {
    Base* p = new Derive[10];
    p[7].print();
    // Derive: 5

    Derive* p2 = new Derive;
    p2 -> print();
    // Derive: 13

    return 0;
}
```
这是为什么呢？
因为默认参数是Compile time的信息，所以具体取什么值看static type。
