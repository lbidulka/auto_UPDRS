import torch
import torch.nn as nn


class Lifter(nn.Module):
    '''
    Note that output keypoints are in canonical (world) space and have 
    a format of (3, 15), xyz by 15 keypoints:

    TODO: VERIFY THIS ORDERING, I THINK THE LEGS ARE SWAPPED
        0:  pelvis
        1:  right hip
        2:  right knee
        3:  right ankle
        4:  left hip
        5:  left knee
        6:  left ankle
        7:  neck
        8:  head
        9:  right shoulder
        10: right elbow
        11: right hand
        12: left shoulder
        13: left elbow
        14: left hand
    '''
    def __init__(self):
        super(Lifter, self).__init__()
        num_joints=15
        self.upscale = nn.Linear((num_joints*2+num_joints), 1024)
        self.res_common = res_block()
        self.res_pose1 = res_block()
        self.res_pose2 = res_block()
        self.res_cam1 = res_block()
        self.res_cam2 = res_block()
        self.pose3d = nn.Linear(1024, num_joints*3)
        self.enc_rot = nn.Linear(1024, 3)
        self.enc_trans = nn.Linear(1024, 3)

    def forward(self, p2d, conf):

        x = torch.cat((p2d, conf), axis=1)
        
        x = self.upscale(x)
        x = nn.LeakyReLU()(self.res_common(x))

        # pose path
        xp = nn.LeakyReLU()(self.res_pose1(x))
        xp = nn.LeakyReLU()(self.res_pose2(xp))
        x_pose = self.pose3d(xp)

        # camera path
        xc = nn.LeakyReLU()(self.res_cam1(x))
        xc = nn.LeakyReLU()(self.res_cam2(xc))
        xc = self.enc_rot(xc)

        # # transition path
        # xt = nn.LeakyReLU()(self.res_cam1(x))
        # xt = nn.LeakyReLU()(self.res_cam2(xt))
        # xt = self.enc_trans(xt)

        return x_pose, xc
    
class res_block(nn.Module):
    def __init__(self):
        super(res_block, self).__init__()
        self.l1 = nn.Linear(1024, 1024)
        self.l2 = nn.Linear(1024, 1024)
        #self.bn1 = nn.BatchNorm1d(1024)
        #self.bn2 = nn.BatchNorm1d(1024)

    def forward(self, x):
        inp = x
        x = nn.LeakyReLU()(self.l1(x))
        x = nn.LeakyReLU()(self.l2(x))
        x += inp

        return x