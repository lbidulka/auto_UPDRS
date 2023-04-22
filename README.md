# !!! (Course Project) Self-Supervised 3D Human Pose Estimation for Parkinson’s Disease and Beyond !!!
I apologize for the extraneous code, as I did not end up having time to properly cleanup my codebase. I do my best here to specify the relevant code for this course project.


## MVP-3D Transfer to TUG data:
- create_PD_2d_dataset.py uses AlphaPose to get the 2D backbone poses on the UPDRS video data and/or filters the 2D poses to create the MVP-3D lifter dataset
    - 'data/body/body_dataset.py' contains the code for filtering the 2D poses (filter_alphapose_results() and filter_ap_detections()) 
    - 'utils/alphapose_filtering.py' contains the pixel-space filter definitions
- train_PD_bodylifter.py trains MVP-3D on the desired UPDRS task (Oval or TUG)

## UncertNet Correction Network:

- 'uncertnet_experiments.py' contains high level control for training and evaluating UncertNet
- 'uncertnet/uncertnet.py' defines the UncerNet and its training
- 'uncertnet/dataset.py' helps load and handle data for the UncertNet
- 'data/body/h36m/uncertnet' contains the numpy data files for training and testing


# (NOT COURSE PROJECT FROM HERE ON) auto_UPDRS
3D body extraction from videos of subjects performing UPDRS tasks & post-processing to evaluate their motion features and give UPDRS scores (in the future).

## 3D Body Pose Prediction
---

2D Proposal Network: [AlphaPose](https://github.com/MVIG-SJTU/AlphaPose) (Halpe Dataset, 26 keypoints)

### Setup:
1. Clone the [AlphaPose](https://github.com/MVIG-SJTU/AlphaPose) repo into "auto_UPDRS":
```
cd auto_UPDRS
git clone https://github.com/MVIG-SJTU/AlphaPose.git
```

1. Download the AlphaPose pretrained model weights halpe26_fast_res50_256x192.pth (see AlphaPose repo instructions) and place into your "auto_UPDRS/AlphaPose/pretrained_models" directory:

2. Verify that AlphaPose sample "demo_inference.py" script works on their example data:
```
cd auto_UPDRS/AlphaPose
python3 scripts/demo_inference.py --cfg configs/halpe_26/resnet/256x192_res50_lr1e-3_1x.yaml --checkpoint pretrained_models/halpe26_fast_res50_256x192.pth --indir examples/demo/ --save_img
```

3. Get the pretrained 3D lifter models from [PD_Gait_labeling](https://github.com/mgholamikn/PD_Gait_labeling). Currently we only use "model_lifter.pt", the 3D pose model fine-tuned on our PD walking data using 2 view cameras:
```
cd auto_UPDRS/model_checkpoints/Mohsens
pip install --upgrade --no-cache-dir gdown
gdown --folder --id 1GVjvla21_oXL4KpSbsEAPXRS7N93W1d5?usp=share_link
```
