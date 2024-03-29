import numpy as np

# Define all the relevant stats for the datasets to look up

# Number of samples
SAMPLE_DICT = {
    "imagenet21": 11801680,
    "imagenet": 1281167,
    "imagenette-160": 9469,
    "imagenette-160-stylized": 9469,
    "imagenet_real": 1281167,
    "tinyimagenet": 100000,
    "cifar10": 50000,
    "cifar100": 50000,
    "stl10": 5000,
}

# Number of classes
CLASS_DICT = {
    "imagenet21": 11230,
    "in21k": 11230,         # Need the short name here too for loading models
    "imagenet": 1000,
    "imagenette-160": 10,
    "imagenette-160-stylized": 10,
    "in1k": 1000,           # Need the short name here too for loading models
    'imagenet_real': 1000,
    "tinyimagenet": 200,
    "cifar10": 10,
    "cifar100": 100,
    "stl10": 10,
}

# Image resolutions
DEFAULT_RES_DICT = {
    "imagenet21": 64,
    "imagenet": 64,
    "imagenette-160": 160,
    "imagenette-160-stylized": 160,
    "imagenet_real": 64,
    "tinyimagenet": 64,
    "cifar10": 32,
    "cifar100": 32,
    "stl10": 64,
}


# Parent directory name
DATA_DICT = {
    "imagenet21": "imagenet21",
    "imagenet": "imagenet",
    "imagenette-160": "imagenette-160",
    "imagenette-160-stylized": "imagenette-160-stylized",
    "tinyimagenet": "tiny-imagenet-200",
    "imagenet_real": "imagenet",
    "cifar10": "cifar10",
    "cifar100": "cifar100",
    "stl10": "stl10",
}

MODE_DICT = {
    "imagenet21": "test",
    "imagenet": "val",
    "imagenette-160": "test",
    "imagenette-160-stylized": "test",
    'imagenet_real': "val",
    "tinyimagenet": "val",
    "cifar10": "val",
    "cifar100": "test",
    "stl10": "val",
}

# Standardization statistics
MEAN_DICT = {
    "imagenet21": np.array([0.485, 0.456, 0.406]) * 255,
    "imagenet": np.array([0.485, 0.456, 0.406]) * 255,
    "imagenette-160": np.array([0.467, 0.459, 0.43]),
    "imagenette-160-stylized": np.array([0.5039, 0.4678, 0.419]),
    "imagenet_real": np.array([0.485, 0.456, 0.406]) * 255,
    "tinyimagenet": np.array([0.485, 0.456, 0.406]),
    "cifar10": np.array([0.49139968, 0.48215827, 0.44653124]),
    "cifar100": np.array([0.49139968, 0.48215827, 0.44653124]),
    "stl10": np.array([0.4914, 0.4822, 0.4465]) * 255,
}


STD_DICT = {
    "imagenet21": np.array([0.229, 0.224, 0.225]) * 255,
    "imagenet": np.array([0.229, 0.224, 0.225]) * 255,
    "imagenette-160": np.array([0.2793, 0.2759, 0.2976]),
    "imagenette-160-stylized": np.array([0.262, 0.254, 0.2531]),
    "imagenet_real": np.array([0.229, 0.224, 0.225]) * 255,
    "tinyimagenet": np.array([0.229, 0.224, 0.225]),
    "cifar10": np.array([0.24703233, 0.24348505, 0.26158768]),
    "cifar100": np.array([0.24703233, 0.24348505, 0.26158768]),
    "stl10": np.array([0.2471, 0.2435, 0.2616]) * 255,
}

# Whether dataset can be cached in memory
OS_CACHED_DICT = {
    "imagenet21": False,
    "imagenet": False,
    "imagenette-160": False,
    "imagenette-160-stylized": False,
    "imagenet_real": False,
    "tinyimagenet": True,
    "cifar10": True,
    "cifar100": True,
    "stl10": True,
    "pets": True,
    "coyo": False,
}
