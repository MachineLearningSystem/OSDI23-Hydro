import functools
import torch.optim

from .adadelta import Adadelta
from .adam import Adam
from .sgd import SGD
from .lr_scheduler import StepLR
from .utils import index_array_or_return_scalar, consolidate_hyperparams_and_determine_B

OPTIMIZERS_MAP = {
    torch.optim.Adadelta: Adadelta,
    torch.optim.Adam: Adam,
    torch.optim.SGD: SGD,
}

LR_SCHEDULER_MAP = {
    torch.optim.lr_scheduler.StepLR: StepLR,
}


def fuse_optimizer(torch_optim_class):
    return functools.partial(OPTIMIZERS_MAP[torch_optim_class])


def fuse_lr_scheduler(torch_lr_scheduler_class, B=1):
    if B > 0:
        return functools.partial(LR_SCHEDULER_MAP[torch_lr_scheduler_class], B=B)
    else:
        return torch_lr_scheduler_class
