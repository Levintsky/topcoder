# Communication

## MPI for Deep learning
- Mu Li: https://www.zhihu.com/question/55119470

## MPI
- A standardized and portable message-passing **standard**;
- Resources:
	- mpich: https://www.mpich.org/
	- openmpi: https://www.open-mpi.org/
- Details:
	- Compilation:
```
mpicc -o mpiProgram mpiProgram.c
```
	- MPI_Comm;
	- Message;
	- MPI object;
```cpp
#include <mpi.h>
void main(int argv,char* argv[]) {
    int rank,size;
    MPI_Init(&argc,&argv);    //初始化MPI环境
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);    //获取进程组中进程编号rank
    MPI_Comm_size(MPI_COMM_WORLD,&size);    //获取进程组中进程数size
    //...
    //...
    MPI_Finalize();    //退出MPI环境
}
```
- MPI in **Deep learning**:
	- https://www.zhihu.com/search?type=content&q=mpi
	- SGD + MPI + Allreduce;
- **Allreduce**: important in **deep learning**;
	- Especially when model is small (computer vision);
	- https://tech.preferred.jp/en/blog/technologies-behind-distributed-deep-learning-allreduce/
	- https://www.zhihu.com/search?type=content&q=allreduce
	- Many different implementations (also offered in openMPI):
		- reduce+broadcast
		- Recursive halving and doubling;
		- Butterfly;
		- **Ring AllReduce**;
	- **NCCL**: NVIDIA's Ring Allreduce for GPU;
		- NCCL 1.x (2015) for nodes in single machine;
		- NCCL 2.0 (2017) for multi-machine;
		- NCCL 2.4 (2019) **double binary tree**, faster than ring;
		- Focus on Allreduce communiation (MPI have many other funcstions);
	- **Gloo** (Facebook):
		- https://github.com/facebookincubator/gloo
		- Gloo is a collective communications library. It comes with a number of collective algorithms useful for machine learning applications. These include a barrier, broadcast, and allreduce.
	- **Horovod** (Uber): similar to NCCL;
		- https://github.com/horovod/horovod
		- Focus on Allreduce communication
		- Distributed training framework for TensorFlow, Keras, PyTorch, and Apache MXNet. https://eng.uber.com/horovod/
	- **2D-Torus** (Sony 2018)
	- **2D-Mesh** (Google)
	- **3D-Torus** (IBM)

## Parameter Server
- Resources:
	- https://www.zhihu.com/search?type=content&q=parameter%20server
- When model is big;
