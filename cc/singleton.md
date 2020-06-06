
```cpp
class Singleton {
    private:
        /* Here will be the instance stored. */
        static Singleton* instance;

        /* Private constructor to prevent instancing. */
        Singleton() {}

    public:
        /* Static access method. */
        static Singleton* getInstance() {
            if (instance == nullptr) {
                instance = new Singleton();
            }

            return instance;
        }
        
    Singleton(const Singleton& s) = delete;
    Singleton operator=(const Singleton& s) = delete;
};

/* Null, because instance will be initialized on demand. */
Singleton* Singleton::instance = nullptr;

int main()
{
    //new Singleton(); // Won't work
    Singleton* s = Singleton::getInstance(); // Ok
    Singleton* r = Singleton::getInstance();

    /* The addresses will be the same. */
    std::cout << s << std::endl;
    std::cout << r << std::endl;
}
```