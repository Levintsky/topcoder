# Concurrency (Chap 15 of a Tour of C++)

## Overview
- Introduction
- Tasks and threads
- Passing Arguments
- Returning Results
- Sharing Data
- Waiting for Events
- Communicating Tasks
	- future and promise; packaged_task; async()
- Advice

## Thread
```cpp
int g_i = 0;
std::mutex g_i_mutex;  // protects g_i
 
void safe_increment() {
    std::lock_guard<std::mutex> lock(g_i_mutex);
    ++g_i;
}

int main() {
  std::thread t1(safe_increment);
  std::thread t2(safe_increment);

  // join to synchronize
  t1.join();
  t2.join();

  // will output 2
  std::cout << g_i << std::endl;

  return 0;
}
```
- Execution
	- Execute only once, even if concurrently
```cpp
std::call_once(flag, callable&& f, Args&&... args);
```
- Lock
	- mutex: a mutex class is a synchronization primitive that can be used to protect shared data from being simultaneously accessed by multiple threads.
```cpp
std::mutex mutex_;
```
	- lock_guard: have effect in visible scope; will disappear after function return;
```cpp
void some_func() {
  std::lock_guard<std::mutex> lock(mutex_);
  // do something ...

  // goes out of scope
}
```