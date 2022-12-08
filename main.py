import collections
import os
from PIL import Image


def describe_data():
    train_path = "./data/train"
    test_path = "./data/valid"
    img_shapes = []
    training_files = get_file_count(train_path, img_shapes)
    print(f'Train Count: {training_files}')  # 69h X 130w
    test_files = get_file_count(test_path, img_shapes)
    print(f'Test Count: {test_files}')  # 100h X 150w

    test_x, test_y = img_shapes[0]
    print(f'{test_x}x{test_y}')
    x_avg, x_min, x_max = 0, 10000, 0
    y_avg, y_min, y_max = 0, 10000, 0

    x_s = []
    y_s = []

    for x, y in img_shapes:
        x_s.append(x)
        x_avg += x
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_s.append(y)
        y_avg += y
        y_min = min(y_min, y)
        y_max = max(y_max, y)

    x_mode = collections.Counter(x_s).most_common()[0][0]
    y_mode = collections.Counter(y_s).most_common()[0][0]

    x_avg = x_avg // len(img_shapes)
    y_avg = y_avg // len(img_shapes)

    print(f'Avg: {x_avg}x{y_avg}')
    print(f'Mode: {x_mode}x{y_mode}')
    print(f'Min: {x_min}x{y_min}')
    print(f'Max: {x_max}x{y_max}')


def get_file_count(directory, shapes):
    count = 0
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            im = Image.open(os.path.join(directory, path))
            shapes.append(im.size)
            count += 1
        if os.path.isdir(os.path.join(directory, path)):
            add = get_file_count(os.path.join(directory, path), shapes)
            count += add
    print(f'File count for {directory}:', count)
    return count


def rearrange_data():
    return None


if __name__ == "__main__":
    print('Running...')
    describe_data()
    print('Done.')
