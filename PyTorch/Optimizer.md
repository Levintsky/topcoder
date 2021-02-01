# Optimizer

## Basics
- In torch/optim/, find optimizer.py and lr_scheduler.py
```python
torch.optim

class Optimizer(object):
```
- Parameters are of following type located in torch/nn/parameter.py:
```python
torch.nn.parameter.Parameter
```
- Refer to https://pytorch.org/docs/stable/optim.html
- Common practice
```python
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
optimizer = optim.Adam([var1, var2], lr=0.0001)
```
- Per-layer learning rate:
```python
optim.SGD([
    {'params': model.base.parameters()},
    {'params': model.classifier.parameters(), 'lr': 1e-3}
], lr=1e-2, momentum=0.9)
```
- Then during learning:
```python
for input, target in dataset:
    optimizer.zero_grad()
    output = model(input)
    loss = loss_fn(output, target)
    loss.backward()
    optimizer.step()
```

## General Design
```python
class Optimizer(object):
    def __init__(self, params, defaults):
		self.state = defaultdict(dict)
        self.param_groups = []

    def state_dict(self):

    def load_state_dict(self, state_dict):

    def zero_grad(self):

    def step(self, closure):

    def add_param_group(self, param_group):
```
- SGD, Rprop, Adam, SparseAdam, Adagrad, ASGD, Adamax are all derived class
- LBFGS

## Adjust learning rate
- Basic class:
```python
class _LRScheduler(object):
```
