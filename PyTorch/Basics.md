# Basics

## Common Operators in Pytorch
- From https://zhuanlan.zhihu.com/p/106788199
- Basic packages required
```python
import collections
import os
import shutil
import tqdm

import numpy as np
import PIL.Image
import torch
import torchvision
```
- 1. Basic config
```python
torch.__version__               # PyTorch version
torch.version.cuda              # Corresponding CUDA version
torch.backends.cudnn.version()  # Corresponding cuDNN version
torch.cuda.get_device_name(0)   # GPU type
```
	- Update
```sh
conda update pytorch torchvision -c pytorch
```
	- Random seed
```python
torch.manual_seed(0)
torch.cuda.manual_seed_all(0)
```
	- Device specification
```sh
CUDA_VISIBLE_DEVICES=0,1 python train.py
```
```python
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'
```
	- Cuda available()?
```python
torch.cuda.is_available()
```
	- cuDNN benchmark mode (faster but with randomness)
```python
torch.backends.cudnn.benchmark = True
torch.backends.cudnn.deterministic = True
```
	- Empty cuda cache manually (sometimes not released after Ctrl+C)
```python
torch.cuda.empty_cache()
```
	- or find python:
```sh
ps aux | grep python
kill -9 [pid]
```
	- or
```sh
nvidia-smi --gpu-reset -i [gpu_id]
```

## Tensor
- Basic info:
```python
tensor.type()   # Data type
tensor.size()   # Shape of the tensor. It is a subclass of Python tuple
tensor.dim()    # Number of dimensions.
```
- Type conversion
```python
# Set default tensor type. Float in PyTorch is much faster than double.
torch.set_default_tensor_type(torch.FloatTensor)
# Type convertions.
tensor = tensor.cuda()
tensor = tensor.cpu()
tensor = tensor.float()
tensor = tensor.long()
```
- With numpy
```python
# torch.Tensor -> np.ndarray.
ndarray = tensor.cpu().numpy()

# np.ndarray -> torch.Tensor.
tensor = torch.from_numpy(ndarray).float()
tensor = torch.from_numpy(ndarray.copy()).float()  # If ndarray has negative stride
```
- With PIL.Image. Pytorch: (N, D, H, W) with value range [0, 1]
```python
# torch.Tensor -> PIL.Image.
image = PIL.Image.fromarray(torch.clamp(tensor * 255, min=0, max=255
    ).byte().permute(1, 2, 0).cpu().numpy())
image = torchvision.transforms.functional.to_pil_image(tensor)  # Equivalently way
# PIL.Image -> torch.Tensor.
tensor = torch.from_numpy(np.asarray(PIL.Image.open(path))
    ).permute(2, 0, 1).float() / 255
tensor = torchvision.transforms.functional.to_tensor(PIL.Image.open(path))  # Equivalently way
```
- np.ndarray with PIL.Image
```python
# np.ndarray -> PIL.Image.
image = PIL.Image.fromarray(ndarray.astypde(np.uint8))
# PIL.Image -> np.ndarray.
ndarray = np.asarray(PIL.Image.open(path))
```
- Get value (save gpu and clean computational graph)
```python
value = tensor.item()
```
- Reshape, view. Reshape support non-continuous case;
```python
tensor = torch.reshape(tensor, shape)
tensor = tensor[torch.randperm(tensor.size(0))]  # Shuffle the first dimension
```
- Reverse: PyTorch does not support tensor[::-1], so:
```python
# Assume tensor has shape N*D*H*W.
tensor = tensor[:, :, :, torch.arange(tensor.size(3) - 1, -1, -1).long()]
```
- Copy
```python
# Operation                 |  New/Shared memory | Still in computation graph |
tensor.clone()            # |        New         |          Yes               |
tensor.detach()           # |      Shared        |          No                |
tensor.detach.clone()()   # |        New         |          No                |
```
- Concatenate: cat and stack. torch.cat along the axis; torch.stack will add a new dim. 3 (10, 5) tensor, torch.cat will produce (30, 5); torch.stack will be (3, 10, 5). 
```python
tensor = torch.cat(list_of_tensors, dim=0)
tensor = torch.stack(list_of_tensors, dim=0)
```
- One-hot
```python
N = tensor.size(0)
one_hot = torch.zeros(N, num_classes).long()
one_hot.scatter_(dim=1, index=torch.unsqueeze(tensor, dim=1), src=torch.ones(N, num_classes).long())
```
- Non-zero
```python
torch.nonzero(tensor)               # Index of non-zero elements
torch.nonzero(tensor == 0)          # Index of zero elements
torch.nonzero(tensor).size(0)       # Number of non-zero elements
torch.nonzero(tensor == 0).size(0)  # Number of zero elements
```
- Equal:
```python
torch.allclose(tensor1, tensor2)  # float tensor
torch.equal(tensor1, tensor2)     # int tensor
```
- Expand
```python
# Expand tensor of shape 64*512 to shape 64*512*7*7.
torch.reshape(tensor, (64, 512, 1, 1)).expand(64, 512, 7, 7)
```
- Matrix multiplication
```python
# Matrix multiplication: (m*n) * (n*p) -> (m*p).
result = torch.mm(tensor1, tensor2)

# Batch matrix multiplication: (b*m*n) * (b*n*p) -> (b*m*p).
result = torch.bmm(tensor1, tensor2)

# Element-wise multiplication.
result = tensor1 * tensor2
```
- Euclidean
```python
# X1 is of shape m*d, X2 is of shape n*d.
dist = torch.sqrt(torch.sum((X1[:,None,:] - X2) ** 2, dim=2))
```

## Model
- Convolution:
```python
conv = torch.nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=True)
conv = torch.nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=1, padding=0, bias=True)
```
	- Convolution Visualizer: https://ezyang.github.io/convolution-visualizer/index.html
- GAP (Global average pooling):
```python
gap = torch.nn.AdaptiveAvgPool2d(output_size=1)
```
- Bilinear pooling
```python
X = torch.reshape(N, D, H * W)                        # Assume X has shape N*D*H*W
X = torch.bmm(X, torch.transpose(X, 1, 2)) / (H * W)  # Bilinear pooling
assert X.size() == (N, D, D)
X = torch.reshape(X, (N, D * D))
X = torch.sign(X) * torch.sqrt(torch.abs(X) + 1e-5)   # Signed-sqrt normalization
X = torch.nn.functional.normalize(X)                  # L2 normalization
```
- Batch normalization
	- By default, when torch.nn.DataParallel on multiple GPU, each card has own mean and std.
	- https://github.com/vacancy/Synchronized-BatchNorm-PyTorch
	- Official version
```python
sync_bn = torch.nn.SyncBatchNorm(num_features, eps=1e-05, momentum=0.1, affine=True, 
                                 track_running_stats=True)
```
	- Change all BN to sync-BN:
```python
def convertBNtoSyncBN(module, process_group=None):
    '''Recursively replace all BN layers to SyncBN layer.

    Args:
        module[torch.nn.Module]. Network
    '''
    if isinstance(module, torch.nn.modules.batchnorm._BatchNorm):
        sync_bn = torch.nn.SyncBatchNorm(module.num_features, module.eps, module.momentum, 
                                         module.affine, module.track_running_stats, process_group)
        sync_bn.running_mean = module.running_mean
        sync_bn.running_var = module.running_var
        if module.affine:
            sync_bn.weight = module.weight.clone().detach()
            sync_bn.bias = module.bias.clone().detach()
        return sync_bn
    else:
        for name, child_module in module.named_children():
            setattr(module, name) = convert_syncbn_model(child_module, process_group=process_group))
        return module
```
	- Inplace for sliding
```python
class BN(torch.nn.Module)
    def __init__(self):
        ...
        self.register_buffer('running_mean', torch.zeros(num_features))

    def forward(self, X):
        ...
        self.running_mean += momentum * (current - self.running_mean)
```
	- Number of parameters
```python
num_parameters = sum(torch.numel(parameter) for parameter in model.parameters())
```
	- More model summary like model.summary() in Keras: https://github.com/sksq96/pytorch-summary
- Model Initialization: notice difference between model.modules() and model.children(). model.modules() will iterate over all sublayers; model.children() 1-layer only.
```python
# Common practise for initialization.
for layer in model.modules():
    if isinstance(layer, torch.nn.Conv2d):
        torch.nn.init.kaiming_normal_(layer.weight, mode='fan_out',
                                      nonlinearity='relu')
        if layer.bias is not None:
            torch.nn.init.constant_(layer.bias, val=0.0)
    elif isinstance(layer, torch.nn.BatchNorm2d):
        torch.nn.init.constant_(layer.weight, val=1.0)
        torch.nn.init.constant_(layer.bias, val=0.0)
    elif isinstance(layer, torch.nn.Linear):
        torch.nn.init.xavier_normal_(layer.weight)
        if layer.bias is not None:
            torch.nn.init.constant_(layer.bias, val=0.0)
# Initialization with given tensor.
layer.weight = torch.nn.Parameter(tensor)
```
	- Partially init: notice if ckpt is torch.nn.DataParallel, then current model should also be torch.nn.DataParallel. torch.nn.DataParallel(model).module == model.
```python
model.load_state_dict(torch.load('model.pth'), strict=False)
```
	- Load to cpu:
```python
model.load_state_dict(torch.load('model.pth', map_location='cpu'))
```


## Data Preparation, Feature Extraction and Finetuning
- image shuffle/region confusion mechanism，RCM [2]
```python
# X is torch.Tensor of size N*D*H*W.
# Shuffle rows
Q = (torch.unsqueeze(torch.arange(num_blocks), dim=1) * torch.ones(1, num_blocks).long()
     + torch.randint(low=-neighbour, high=neighbour, size=(num_blocks, num_blocks)))
Q = torch.argsort(Q, dim=0)
assert Q.size() == (num_blocks, num_blocks)

X = [torch.chunk(row, chunks=num_blocks, dim=2)
     for row in torch.chunk(X, chunks=num_blocks, dim=1)]
X = [[X[Q[i, j].item()][j] for j in range(num_blocks)]
     for i in range(num_blocks)]

# Shulle columns.
Q = (torch.ones(num_blocks, 1).long() * torch.unsqueeze(torch.arange(num_blocks), dim=0)
     + torch.randint(low=-neighbour, high=neighbour, size=(num_blocks, num_blocks)))
Q = torch.argsort(Q, dim=1)
assert Q.size() == (num_blocks, num_blocks)
X = [[X[i][Q[i, j].item()] for j in range(num_blocks)]
     for i in range(num_blocks)]

Y = torch.cat([torch.cat(row, dim=2) for row in X], dim=1)
```
- Video: load from cv2
```python
import cv2
video = cv2.VideoCapture(mp4_path)
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))
video.release()
```
	-  TSN each segment sampling for video[3]
```python
K = self._num_segments
if is_train:
    if num_frames > K:
        # Random index for each segment.
        frame_indices = torch.randint(
            high=num_frames // K, size=(K,), dtype=torch.long)
        frame_indices += num_frames // K * torch.arange(K)
    else:
        frame_indices = torch.randint(
            high=num_frames, size=(K - num_frames,), dtype=torch.long)
        frame_indices = torch.sort(torch.cat((
            torch.arange(num_frames), frame_indices)))[0]
else:
    if num_frames > K:
        # Middle index for each segment.
        frame_indices = num_frames / K // 2
        frame_indices += num_frames // K * torch.arange(K)
    else:
        frame_indices = torch.sort(torch.cat((                              
            torch.arange(num_frames), torch.arange(K - num_frames))))[0]
assert frame_indices.size() == (K,)
return [frame_indices[i] for i in range(K)]
```
- ImageNet:
```python
# VGG-16 relu5-3 feature.
model = torchvision.models.vgg16(pretrained=True).features[:-1]
# VGG-16 pool5 feature.
model = torchvision.models.vgg16(pretrained=True).features
# VGG-16 fc7 feature.
model = torchvision.models.vgg16(pretrained=True)
model.classifier = torch.nn.Sequential(*list(model.classifier.children())[:-3])
# ResNet GAP feature.
model = torchvision.models.resnet18(pretrained=True)
model = torch.nn.Sequential(collections.OrderedDict(
    list(model.named_children())[:-1]))

with torch.no_grad():
    model.eval()
    conv_representation = model(image)
```
- Feature extraction
```python
class FeatureExtractor(torch.nn.Module):
    """Helper class to extract several convolution features from the given
    pre-trained model.

    Attributes:
        _model, torch.nn.Module.
        _layers_to_extract, list<str> or set<str>

    Example:
        >>> model = torchvision.models.resnet152(pretrained=True)
        >>> model = torch.nn.Sequential(collections.OrderedDict(
                list(model.named_children())[:-1]))
        >>> conv_representation = FeatureExtractor(
                pretrained_model=model,
                layers_to_extract={'layer1', 'layer2', 'layer3', 'layer4'})(image)
    """
    def __init__(self, pretrained_model, layers_to_extract):
        torch.nn.Module.__init__(self)
        self._model = pretrained_model
        self._model.eval()
        self._layers_to_extract = set(layers_to_extract)
    
    def forward(self, x):
        with torch.no_grad():
            conv_representation = []
            for name, layer in self._model.named_children():
                x = layer(x)
                if name in self._layers_to_extract:
                    conv_representation.append(x)
            return conv_representation
```
	- Other pretrained: https://github.com/Cadene/pretrained-models.pytorch
- Finetuning:
```python
model = torchvision.models.resnet18(pretrained=True)
for param in model.parameters():
    param.requires_grad = False
model.fc = nn.Linear(512, 100)  # Replace the last fc layer
optimizer = torch.optim.SGD(model.fc.parameters(), lr=1e-2, momentum=0.9, weight_decay=1e-4)
```
- Different lr for finetuning:
```python
model = torchvision.models.resnet18(pretrained=True)
finetuned_parameters = list(map(id, model.fc.parameters()))
conv_parameters = (p for p in model.parameters() if id(p) not in finetuned_parameters)
parameters = [{'params': conv_parameters, 'lr': 1e-3}, 
              {'params': model.fc.parameters()}]
optimizer = torch.optim.SGD(parameters, lr=1e-2, momentum=0.9, weight_decay=1e-4)
```

## Model Training
- Preprocessing:
```python
train_transform = torchvision.transforms.Compose([
    torchvision.transforms.RandomResizedCrop(size=224,
                                             scale=(0.08, 1.0)),
    torchvision.transforms.RandomHorizontalFlip(),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406),
                                     std=(0.229, 0.224, 0.225)),
 ])
 val_transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize(256),
    torchvision.transforms.CenterCrop(224),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406),
                                     std=(0.229, 0.224, 0.225)),
])
```
- Training
```python
for t in epoch(80):
    for images, labels in tqdm.tqdm(train_loader, desc='Epoch %3d' % (t + 1)):
        images, labels = images.cuda(), labels.cuda()
        scores = model(images)
        loss = loss_function(scores, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```
- label smoothing [4]
```python
for images, labels in train_loader:
    images, labels = images.cuda(), labels.cuda()
    N = labels.size(0)
    # C is the number of classes.
    smoothed_labels = torch.full(size=(N, C), fill_value=0.1 / (C - 1)).cuda()
    smoothed_labels.scatter_(dim=1, index=torch.unsqueeze(labels, dim=1), value=0.9)

    score = model(images)
    log_prob = torch.nn.functional.log_softmax(score, dim=1)
    loss = -torch.sum(log_prob * smoothed_labels) / N
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```
- Mixup[5]
```python
beta_distribution = torch.distributions.beta.Beta(alpha, alpha)
for images, labels in train_loader:
    images, labels = images.cuda(), labels.cuda()

    # Mixup images.
    lambda_ = beta_distribution.sample([]).item()
    index = torch.randperm(images.size(0)).cuda()
    mixed_images = lambda_ * images + (1 - lambda_) * images[index, :]

    # Mixup loss.    
    scores = model(mixed_images)
    loss = (lambda_ * loss_function(scores, labels) 
            + (1 - lambda_) * loss_function(scores, labels[index]))

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```
- Regularization
```python
l1_regularization = torch.nn.L1Loss(reduction='sum')
loss = ...  # Standard cross-entropy loss
for param in model.parameters():
    loss += lambda_ * torch.sum(torch.abs(param))
loss.backward()
```
	- Weight decay for specified parameters (not for bias/...)
```python
bias_list = (param for name, param in model.named_parameters() if name[-4:] == 'bias')
others_list = (param for name, param in model.named_parameters() if name[-4:] != 'bias')
parameters = [{'parameters': bias_list, 'weight_decay': 0},                
              {'parameters': others_list}]
optimizer = torch.optim.SGD(parameters, lr=1e-2, momentum=0.9, weight_decay=1e-4)
```
- Gradient clipping:
```python
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=20)
```
- Softmax output accuracy:
```python
score = model(images)
prediction = torch.argmax(score, dim=1)
num_correct = torch.sum(prediction == labels).item()
accuruacy = num_correct / labels.size(0)
```
- Visualization:
	- https://github.com/szagoruyko/pytorchviz
	- Facebook: Visdom https://github.com/facebookresearch/visdom
	- Facebook: TensorboardX: https://pytorch.org/docs/stable/tensorboard.html
```python
# Example using Visdom.
vis = visdom.Visdom(env='Learning curve', use_incoming_socket=False)
assert self._visdom.check_connection()
self._visdom.close()
options = collections.namedtuple('Options', ['loss', 'acc', 'lr'])(
    loss={'xlabel': 'Epoch', 'ylabel': 'Loss', 'showlegend': True},
    acc={'xlabel': 'Epoch', 'ylabel': 'Accuracy', 'showlegend': True},
    lr={'xlabel': 'Epoch', 'ylabel': 'Learning rate', 'showlegend': True})

for t in epoch(80):
    tran(...)
    val(...)
    vis.line(X=torch.Tensor([t + 1]), Y=torch.Tensor([train_loss]),
             name='train', win='Loss', update='append', opts=options.loss)
    vis.line(X=torch.Tensor([t + 1]), Y=torch.Tensor([val_loss]),
             name='val', win='Loss', update='append', opts=options.loss)
    vis.line(X=torch.Tensor([t + 1]), Y=torch.Tensor([train_acc]),
             name='train', win='Accuracy', update='append', opts=options.acc)
    vis.line(X=torch.Tensor([t + 1]), Y=torch.Tensor([val_acc]),
             name='val', win='Accuracy', update='append', opts=options.acc)
    vis.line(X=torch.Tensor([t + 1]), Y=torch.Tensor([lr]),
             win='Learning rate', update='append', opts=options.lr)
```
- Learning-rate
	- Current lr
```python
# If there is one global learning rate (which is the common case).
lr = next(iter(optimizer.param_groups))['lr']

# If there are multiple learning rates for different layers.
all_lr = []
for param_group in optimizer.param_groups:
    all_lr.append(param_group['lr'])
```
	- lr decay:
```python
# Reduce learning rate when validation accuarcy plateau.
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', patience=5, verbose=True)
for t in range(0, 80):
    train(...); val(...)
    scheduler.step(val_acc)

# Cosine annealing learning rate.
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=80)
# Reduce learning rate by 10 at given epochs.
scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones=[50, 70], gamma=0.1)
for t in range(0, 80):
    scheduler.step()    
    train(...); val(...)

# Learning rate warmup by 10 epochs.
scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=lambda t: t / 10)
for t in range(0, 10):
    scheduler.step()
    train(...); val(...)
```
- Checkpoint
```python
# Save checkpoint.
is_best = current_acc > best_acc
best_acc = max(best_acc, current_acc)
checkpoint = {
    'best_acc': best_acc,    
    'epoch': t + 1,
    'model': model.state_dict(),
    'optimizer': optimizer.state_dict(),
}
model_path = os.path.join('model', 'checkpoint.pth.tar')
torch.save(checkpoint, model_path)
if is_best:
    shutil.copy('checkpoint.pth.tar', model_path)

# Load checkpoint.
if resume:
    model_path = os.path.join('model', 'checkpoint.pth.tar')
    assert os.path.isfile(model_path)
    checkpoint = torch.load(model_path)
    best_acc = checkpoint['best_acc']
    start_epoch = checkpoint['epoch']
    model.load_state_dict(checkpoint['model'])
    optimizer.load_state_dict(checkpoint['optimizer'])
    print('Load checkpoint at epoch %d.' % start_epoch)
```
- Precision/recall
```python
# data['label'] and data['prediction'] are groundtruth label and prediction 
# for each image, respectively.
accuracy = np.mean(data['label'] == data['prediction']) * 100

# Compute recision and recall for each class.
for c in range(len(num_classes)):
    tp = np.dot((data['label'] == c).astype(int),
                (data['prediction'] == c).astype(int))
    tp_fp = np.sum(data['prediction'] == c)
    tp_fn = np.sum(data['label'] == c)
    precision = tp / tp_fp * 100
    recall = tp / tp_fn * 100
```

## Model Testing
- Precision, Recall, F1, 
```python
import sklearn.metrics

all_label = []
all_prediction = []
for images, labels in tqdm.tqdm(data_loader):
     # Data.
     images, labels = images.cuda(), labels.cuda()
     
     # Forward pass.
     score = model(images)
     
     # Save label and predictions.
     prediction = torch.argmax(score, dim=1)
     all_label.append(labels.cpu().numpy())
     all_prediction.append(prediction.cpu().numpy())

# Compute RP and confusion matrix.
all_label = np.concatenate(all_label)
assert len(all_label.shape) == 1
all_prediction = np.concatenate(all_prediction)
assert all_label.shape == all_prediction.shape
micro_p, micro_r, micro_f1, _ = sklearn.metrics.precision_recall_fscore_support(
     all_label, all_prediction, average='micro', labels=range(num_classes))
class_p, class_r, class_f1, class_occurence = sklearn.metrics.precision_recall_fscore_support(
     all_label, all_prediction, average=None, labels=range(num_classes))
# Ci,j = #{y=i and hat_y=j}
confusion_mat = sklearn.metrics.confusion_matrix(
     all_label, all_prediction, labels=range(num_classes))
assert confusion_mat.shape == (num_classes, num_classes)
```
- Save results into a csv:
```python
import csv

# Write results onto disk.
with open(os.path.join(path, filename), 'wt', encoding='utf-8') as f:
     f = csv.writer(f)
     f.writerow(['Class', 'Label', '# occurence', 'Precision', 'Recall', 'F1',
                 'Confused class 1', 'Confused class 2', 'Confused class 3',
                 'Confused 4', 'Confused class 5'])
     for c in range(num_classes):
         index = np.argsort(confusion_mat[:, c])[::-1][:5]
         f.writerow([
             label2class[c], c, class_occurence[c], '%4.3f' % class_p[c],
                 '%4.3f' % class_r[c], '%4.3f' % class_f1[c],
                 '%s:%d' % (label2class[index[0]], confusion_mat[index[0], c]),
                 '%s:%d' % (label2class[index[1]], confusion_mat[index[1], c]),
                 '%s:%d' % (label2class[index[2]], confusion_mat[index[2], c]),
                 '%s:%d' % (label2class[index[3]], confusion_mat[index[3], c]),
                 '%s:%d' % (label2class[index[4]], confusion_mat[index[4], c])])
         f.writerow(['All', '', np.sum(class_occurence), micro_p, micro_r, micro_f1, 
                     '', '', '', '', ''])
```

## PyTorch Other Misc
- Model definition:
	- Pooling: torch.nn (torch.nn contains parameters)
	- Activation: torch.nn.functional
```python
def forward(self, x):
    ...
    x = torch.nn.functional.dropout(x, p=0.5, training=self.training)
```
- model.train() and model.eval()
- "with torch.no_grad()". model.eval() v.s. torch.no_grad() difference: 
	- model.eval() use eval model for BN, dropout;
	- torch.no_grad() disable autograd and loss.backward().
- torch.nn.CrossEntropyLoss = torch.nn.functional.log_softmax + torch.nn.NLLLoss.
- loss.backward() remember to call optimizer.zero_grad() to clean gradient. optimizer.zero_grad() and model.zero_grad().
- Performance
	- torch.utils.data.DataLoader recommend pin_memory=True (unless super-small like MNIST);
	- num_workers: hand-tune for best performance;
	- del for unused intermediate;
	- inplace save gpu
```python
x = torch.nn.functional.relu(x, inplace=True)
```
	- Assert shape for safety check and debugging;
	- Avoid 1d tensor except label;
- Time consumption of each module:
```python
with torch.autograd.profiler.profile(enabled=True, use_cuda=False) as profile:
    ...
print(profile)
```
	- or
```sh
python -m torch.utils.bottleneck main.py
```