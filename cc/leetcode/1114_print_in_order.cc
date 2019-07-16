// Solution 1:
class Foo {   
    mutex m1, m2;
public:
    Foo() {
        m1.lock(), m2.lock();
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        m1.unlock();
    }

    void second(function<void()> printSecond) {
        m1.lock();
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        m1.unlock();
        m2.unlock();
    }

    void third(function<void()> printThird) {
        m2.lock();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
        m2.unlock();
    }
};

void printFirst() {
    cout << "first";
}

void printSecond() {
    cout << "second";
}

void printThird() {
    cout << "third";
}

int main(int argc, char** argv) {
    Foo foo;

    auto func = [&foo](void (Foo::*fp)(function<void()>), function<void()> p) -> void {
        (foo.*fp)(p);
    };

    thread t1(func, &Foo::first, printFirst);
    thread t2(func, &Foo::second, printSecond);
    thread t3(func, &Foo::third, printThird);
    t3.join();
    t1.join();
    t2.join();
    return 0;
}
