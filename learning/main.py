import os
import pickle

if __name__ == '__main__':

    train_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp/train.pkl'))

    train_data = []
    with open(train_data_path, 'r') as f:
        train_data = pickle.load(f)
