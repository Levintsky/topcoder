# Basics

## Resources
- https://www.youtube.com/watch?v=QLfF5sT23f8&list=PLSVM68VUM1eWsEX0yPliaL3pTZoKqJWfi

## Architecture
- CPU: on each processor:
	- System Bus
	- L2 Cache
	- L1 Cache
	- CPU Core
- GPU
	- 5000+ cores
- 64K shared memory (L1 Cache)

## Tools
- Compiler: nvcc
- Debugger: nvcc-gdb
- Performance: nsight, nvprof
- Function library: nvblas, cusolver, cufftw, cusparse, nvgraph

## Sample codes
- https://github.com/huiscliu/tutorials

## Terminology
- SPA (Streaming Processor Array);
- TPC/GPC (Texture/Graphics Processor Cluster)
	- 3 SM + TEX
- SM (streaming multiprocessor): 32 SP
- SP (CUDA Core/Streaming processor)

## Running
- Kernel -> grid -> block;
- 32-thread: a warp;
- Memory system:
	- Local memory: per-thread;
	- Shared memory: per-block (threads in the same block);
	- Global memory: per-application;
- Design:
	- Different thread visits different bank (fast);
	- A bank = half warp;
