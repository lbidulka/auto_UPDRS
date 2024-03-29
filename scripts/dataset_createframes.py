import cv2
import argparse
import os
import fnmatch
from tqdm import tqdm

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--videos_path", default="/mnt/CAMERA-data/CAMERA/CAMERA visits/Mobility Visit/Study Subjects/", help="input video dataset path", type=str)
    parser.add_argument("--outframes_path", default="/mnt/CAMERA-data/CAMERA/Other/lbidulka_dataset/", help="output frame data path", type=str)
    return parser.parse_args()

'''
Converts videos to a sequence of png frames
'''
def main():
    input_args = get_args()

    # Subject ID mapping -- I HATE THIS BUT I DONT WANNA DEAL WITH MODULE IMPORTING
    subjects_ALL_id_dict = {
                    'S01': 9291, 'S02': 9739, 'S03': 9285, 'S04': 9769, 'S05': 9964, 
                    'S06': 9746, 'S07': 9270, 'S08': 7399, 'S09': 9283, 'S10': 9107, 
                    'S11': 9455, 'S12': 9713, 'S13': 9317, 'S14': 9210, 'S16': 9403, 
                    'S17': 9791, 'S18': 9813, 'S19': 9525, 'S20': 9419, 'S21': 7532, 
                    'S22': 9339, 'S23': 9754, 'S24': 9392, 'S25': 9810, 'S26': 7339, 
                    'S27': 7399, 'S28': 7182, 'S29': 9986, 'S30': 9731, 'S31': 9629,  
                    'S32': 9314, 'S33': 9448, 'S34': 9993, 'S35': 9182,  
                    }        
    subjects_All_date = ['20210223','20191114','20191120','20191112','20191119','20200220','20191121',
                    '20191126','20191128','20191203','20191204','20200108','20200109','20200121','20200122','20200123',
                    '20200124','20200127','20200130','20200205','20200206','20200207','20200213','20200214','20200218',
                    '20191126','20200221','20210706','20210804','20200206','20210811','20191210','20191212','20191218',
                    '20200227']
    subjects_All = ['S01','S02','S03','S04','S05',
                'S06','S07','S08','S09','S10',
                'S11','S12','S13','S14','S16',
                'S17','S18','S19','S20','S21',
                'S22','S23','S24','S25','S26',
                'S27','S28','S29','S30','S31',
                'S32','S33','S34','S35']
    

    task = "free_form_oval" #"tug_stand_walk_sit_"
    chs = ["003", "004"]


    print("Looking in: ", input_args.videos_path)
    # iterate over the subjects_ALL_id_dict dict of (S_id: id) pairs
    for S_id, id in subjects_ALL_id_dict.items():
        for ch in chs:
            print("Processing ", S_id, "CH_" + ch, end='')
            # Construct paths
            subj_idx = subjects_All.index(S_id)
            in_file_end = subjects_All_date[subj_idx] + '/' + str(id)

            out_path = input_args.outframes_path + str(id) + '/' + task + '/' + ch + '/frames/'

            # Deal with bad formatting :/
            if os.path.exists(input_args.videos_path + in_file_end + '/Video Data/'):
                in_file_end += '/Video Data/'
            elif os.path.exists(input_args.videos_path + in_file_end + '/Video_Data/'):
                in_file_end += '/Video_Data/'
            else:
                print("  ERR its a really badly formatted one... : ", S_id, id, subjects_All_date[subj_idx])
                break
                
            in_file_end += 'CH_' + ch + '/'
            
            for file in os.listdir(input_args.videos_path + in_file_end):
                if fnmatch.fnmatch(file, '*' + task + '*.mp4'):
                    in_file_end += file

            in_file = input_args.videos_path + in_file_end
            
            print(" from: ", in_file_end, "...")

            # Make sure its all good to go
            if not os.path.exists(in_file):
                print("  ERR Input file not found: ", in_file_end)
            if not os.path.exists(out_path):
                print("Creating output directory: ", out_path)
                os.makedirs(out_path)
            else:
                capture = cv2.VideoCapture(in_file)
                if not capture.isOpened():
                    print("  ERR Cannot open input file: ", in_file_end)
                    break

                # Process frames
                # TODO: LIMIT TO FIRST 2 MINS, AND MAKE SURE THE 30FPS ONES USE 30FPS INSTEAD OF 15FPS
                # TODO: DO THE 2 MINS EVEN CAPTURE RELEVANT MOTION?
                # TODO: DOWNSAMPLE THE IMAGES FROM 4k?
                for frame_nr in tqdm(range(0, 15 * 30)):
                    ret, frame = capture.read()
                    if ret: 
                        cv2.imwrite(out_path + '/' + str(frame_nr) + '.png', frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])   # Probably should swap to jpg....
                    else:
                        break
                capture.release()
                print("  Success.")

if __name__ == '__main__':
    main()
