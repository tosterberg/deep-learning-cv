import os
from PIL import Image


def describe_data():
    train_path = "./data/train"
    test_path = "./data/valid"
    training_files, img_h, img_w = get_file_count(train_path)
    print(f'Train Count: {training_files}, Minimum Dimensions: {img_h} x {img_w}')  # 69h X 130w
    test_files, img_h, img_w = get_file_count(test_path)
    print(f'Test Count: {test_files}, Minimum Dimensions: {img_h} x {img_w}')  # 100h X 150w


def get_file_count(directory):
    count = 0
    min_width, min_height = 10000, 10000
    w, h = None, None
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            im = Image.open(os.path.join(directory, path))
            w, h = im.size
            count += 1
        if os.path.isdir(os.path.join(directory, path)):
            add, h, w = get_file_count(os.path.join(directory, path))
            count += add
        min_width = min(min_width, w)
        min_height = min(min_height, h)
    print(f'File count for {directory}:', count)
    return count, min_width, min_height


def rearrange_data():
    return None


if __name__ == "__main__":
    print('Running...')
    describe_data()
    print('Done.')
