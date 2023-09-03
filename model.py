import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
import torchvision

class ResNet(nn.Module):
    """encoder + classifier"""
    def __init__(self, name='resnet152', num_classes=2):
        super(ResNet, self).__init__()
        if name == 'vgg19':
            self.encoder = torchvision.models.vgg19(pretrained=True)
            self.encoder.features[0] = nn.Conv2d(1, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            self.encoder.classifier[6] = nn.Identity()
            self.fc = nn.Linear(4096, num_classes)
        elif name=='vgg11':
            self.encoder = torchvision.models.vgg11(pretrained=True)
            self.encoder.features[0] = nn.Conv2d(1, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
            self.encoder.classifier[6] = nn.Identity()
            self.fc = nn.Linear(4096, num_classes)
        elif name=='resnet152':
            self.encoder = torchvision.models.resnet152(zero_init_residual=True)
            #self.encoder.conv1 = nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
            self.encoder.fc = nn.Identity()
            self.fc = nn.Linear(2048, num_classes)
            #self.sigmoid=nn.Sigmoid()
        elif name=='resnet101':
            self.encoder = torchvision.models.resnet101(zero_init_residual=True)
            self.encoder.conv1 = nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
            self.encoder.fc = nn.Identity()
            self.fc = nn.Linear(2048, num_classes)
        elif name=='resnet50':
            self.encoder = torchvision.models.resnet50(zero_init_residual=True)
            self.encoder.conv1 = nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
            self.encoder.fc = nn.Identity()
            self.fc = nn.Linear(2048, num_classes)
            self.sigmoid=nn.Sigmoid()
        elif name=='resnet34':
            self.encoder = torchvision.models.resnet34(pretrained=True)
            self.encoder.conv1 = nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
            self.encoder.fc = nn.Identity()
            self.fc = nn.Linear(512, num_classes)
        elif name=='resnet18':
            self.encoder = torchvision.models.resnet18(zero_init_residual=True)
            self.encoder.conv1 = nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
            self.encoder.fc = nn.Identity()
            self.fc = nn.Linear(512, num_classes)
        elif name=='densenet161':
            self.encoder = torchvision.models.densenet161(pretrained=True)
            self.encoder.features.conv0 = nn.Conv2d(1, 96, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
            self.encoder.classifier = nn.Identity()
            self.fc = nn.Linear(2208, num_classes)
        elif name=='densenet121':
            self.encoder = torchvision.models.densenet121(pretrained=True)
            self.encoder.features.conv0 = nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
            self.encoder.classifier = nn.Identity()
            self.fc = nn.Linear(1024, num_classes)
        elif name=='unet':
            self.encoder = torch.hub.load('mateuszbuda/brain-segmentation-pytorch', 'unet', in_channels=3, out_channels=num_classes, init_features=32, pretrained=True)
            #self.encoder = UNet(in_channels=1, out_channels=num_classes)
            self.fc = nn.Identity()
        else:
            self.encoder = torchvision.models.resnet152(pretrained=True)
            self.encoder.conv1 = nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
            self.encoder.fc = nn.Identity()
            self.fc = nn.Linear(2048, num_classes)
        
    def forward(self, x):

        return self.fc(self.encoder(x))

