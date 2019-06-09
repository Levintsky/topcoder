# TorchVision Package

## Datasets
- Contain all popular datasets
```python
__all__ = ('LSUN', 'LSUNClass',
           'ImageFolder', 'DatasetFolder', 'FakeData',
           'CocoCaptions', 'CocoDetection',
           'CIFAR10', 'CIFAR100', 'EMNIST', 'FashionMNIST',
           'MNIST', 'KMNIST', 'STL10', 'SVHN', 'PhotoTour', 'SEMEION',
           'Omniglot', 'SBU', 'Flickr8k', 'Flickr30k',
           'VOCSegmentation', 'VOCDetection', 'Cityscapes', 'ImageNet',
           'Caltech101', 'Caltech256', 'CelebA', 'SBDataset', 'VisionDataset',
           'USPS')
```
- For each dataset, a separate file for XXXDataset class derived from the abstract VisionDataset or , and implements its own init, getitem and len:
```python
class VisionDataset(data.Dataset):
    def __init__(self):
    def __getitem__(self, index):
        raise NotImplementedError
    def __len__(self):
        raise NotImplementedError

class ImageFolder(DatasetFolder):
    def __init__(self, ...)

class DatasetFolder(VisionDataset):
    def __init__(self):
    def __getitem__(self, index):
    def __len__(self):

class StandardTransform(object):
    def __init__(self, transform=None, target_transform=None):
    def __call__(self, input, target):
```

## C-Source
- Implement ROI-pooling, ROI-align, NMS
```cpp
std::tuple<at::Tensor, at::Tensor> ROIPool_forward(
    const at::Tensor& input, ...) {
#ifdef WITH_CUDA
    return ROIPool_forward_cuda(
        input, rois, spatial_scale, pooled_height, pooled_width);
#endif
    return ROIPool_forward_cpu(...);
}
at::Tensor ROIPool_backward(
    const at::Tensor& grad, ...);

at::Tensor ROIAlign_forward();
at::Tensor ROIAlign_backward();
at::Tensor nms();
```
- Binding cpp and cuda modules to python:
```cpp
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("nms", &nms, "non-maximum suppression");
  m.def("roi_align_forward", &ROIAlign_forward, "ROIAlign_forward");
  m.def("roi_align_backward", &ROIAlign_backward, "ROIAlign_backward");
  m.def("roi_pool_forward", &ROIPool_forward, "ROIPool_forward");
  m.def("roi_pool_backward", &ROIPool_backward, "ROIPool_backward");
#ifdef WITH_CUDA
  m.attr("CUDA_VERSION") = CUDA_VERSION;
#endif
}
```

## Models
- Classification: AlexNet, DenseNet, GoogleNet, Inception, MobileNet, ResNet, ShuffleNet, SqueezeNet

## Transforms