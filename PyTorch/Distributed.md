# Distributed Training

## Typical Setup
- Backend
	- GLOO (default for CPU)
	- MPI (optional)
	- NCCL (GPU)
- Distributed URL:
	- "env://" style:
	- "TCP" style:
- World Size: how many nodes

## NCCL (Multi-GPU)
- In the main loop
```python
import torch.multiprocessing as mp

args.world_size = ngpus_per_node * args.world_size
mp.spawn(main_worker,
	nprocs=ngpus_per_node,
	args=(ngpus_per_node, args))
```
- In the function (main_worker in our case)
```python
import torch.distributed as dist

dist.init_process_group(backend="nccl",
	init_method=args.dist_url,
	world_size=args.world_size,
	rank=args.rank)

model = torch.nn.parallel.DistributedDataParallel(model)
```
- Single machine, multiple cards:
```python
model = torch.nn.DataParallel(model).cuda()
```
- Dataloader:
```python
train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset)

train_loader = torch.utils.data.DataLoader(
        train_dataset, batch_size=args.batch_size, shuffle=(train_sampler is None),
        num_workers=args.workers, pin_memory=True, sampler=train_sampler)
```
- Training:
```python
if args.distributed: train_sampler.set_epoch(epoch)
```
- Checkpointing:
```python
if args.rank % ngpus_per_ndoe == 0:
	torch.save(...)
```

## MPI
- https://zhuanlan.zhihu.com/p/64579496
- MPI (Message Passing Interface): an open standard
- Softwares: OpenMPI, MPICH, MVAPICH, Intel MPI
- Setup:
	- Cluster with InfiniBand
	- Every node will have Linux system with same username
	- Between nodes: ssh without password
	- Install an MPI implementation
	- An NFS
- Parallel:
	- Data (more popular)
	- Model
```python
# filename 'ptdist.py'
import torch
import torch.distributed as dist

def main(rank, world):
    if rank == 0:
        x = torch.tensor([1., -1.]) # Tensor of interest
        dist.send(x, dst=1)
        print('Rank-0 has sent the following tensor to Rank-1')
        print(x)
    else:
        z = torch.tensor([0., 0.]) # A holder for recieving the tensor
        dist.recv(z, src=0)
        print('Rank-1 has recieved the following tensor from Rank-0')
        print(z)

if __name__ == '__main__':
    dist.init_process_group(backend='mpi')
```
- Check running
```
cluster@miriad2a:~/nfs$ mpiexec -n 2 -ppn 1 -hosts miriad2a,miriad2b python ptdist.py
Rank-0 has sent the following tensor to Rank-1
tensor([ 1., -1.])
Rank-1 has recieved the following tensor from Rank-0
tensor([ 1., -1.])
```
- Synchronize gradients:
```python
model = LeNet()
# first synchronization of initial weights
sync_initial_weights(model, rank, world_size)

optimizer = optim.SGD(model.parameters(), lr=1e-3, momentum=0.85)

model.train()
for epoch in range(1, epochs + 1):
    for data, target in train_loader:
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()

        # The all-reduce on gradients
        sync_gradients(model, rank, world_size)

        optimizer.step()

def sync_initial_weights(model, rank, world_size):
    for param in model.parameters():
        if rank == 0:
            # Rank 0 is sending it's own weight
            # to all it's siblings (1 to world_size)
            for sibling in range(1, world_size):
                dist.send(param.data, dst=sibling)
        else:
            # Siblings must recieve the parameters
            dist.recv(param.data, src=0)


def sync_gradients(model, rank, world_size):
    for param in model.parameters():
        dist.all_reduce(param.grad.data, op=dist.reduce_op.SUM)
```