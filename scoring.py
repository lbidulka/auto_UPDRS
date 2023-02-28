import argparse
from utils import info, post_processing

# Full body tracking tasks (e.g. gait analysis)
def body_tasks(input_args):
    ts_path = input_args.data_path + 'body/time_series/outputs_finetuned/'

    subjects = info.subjects_All

    # Get some features
    gait_feats = post_processing.gait_features(subjects, ts_path)
    step_widths = gait_feats.step_width(subjects)
    print(step_widths)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", default="./auto_UPDRS/data/", help="input data path", type=str)
    parser.add_argument("--output_path", default="./auto_UPDRS/outputs/", help="output data path", type=str)
    return parser.parse_args()

def main():
    input_args = get_args()

    body_tasks(input_args)    
    
if __name__ == '__main__':
    main()