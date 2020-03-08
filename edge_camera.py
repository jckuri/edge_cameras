import argparse
import cv2
import numpy as np
import os
from openvino.inference_engine import IENetwork, IECore

MODEL = 'models/semantic-segmentation-adas-0001.xml'
CPU_EXTENSION = "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"

class Network:

    def __init__(self):
        self.plugin = None
        self.network = None
        self.input_blob = None
        self.output_blob = None
        self.exec_network = None
        self.infer_request = None

    def load_model(self, model, device="CPU", cpu_extension=None):
        model_xml = model
        model_bin = os.path.splitext(model_xml)[0] + ".bin"
        self.plugin = IECore()
        if cpu_extension and "CPU" in device:
            self.plugin.add_extension(cpu_extension, device)
        self.network = IENetwork(model=model_xml, weights=model_bin)
        self.exec_network = self.plugin.load_network(self.network, device)
        self.input_blob = next(iter(self.network.inputs))
        self.output_blob = next(iter(self.network.outputs))

    def get_input_shape(self):
        return self.network.inputs[self.input_blob].shape

    def sync_inference(self, image):
        self.exec_network.infer({'data': image})

    def extract_output(self):
        return self.exec_network.requests[0].outputs

def get_args():
    parser = argparse.ArgumentParser("Run inference on an input video")
    m_desc = "The location of the model XML file"
    i_desc = "The location of the input file"
    t_desc = "Start time of the video ('YYYY/MM/DD HH:MM:SS.CC')"
    d_desc = "The device name, if not 'CPU'"
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    required.add_argument("-i", help=i_desc, required = True)
    required.add_argument("-t", help=t_desc, required = True)
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument("-m", help=m_desc, default = MODEL)
    optional.add_argument("-d", help=d_desc, default='CPU')
    c_desc = "CPU extension file location, if applicable"
    optional.add_argument("-c", help=c_desc, default=CPU_EXTENSION)
    args = parser.parse_args()
    return args

def preprocessing(input_image, height, width):
    image = np.copy(input_image)
    #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (width, height))
    image = image.transpose((2, 0, 1))
    image = image.reshape(1, 3, height, width)
    return image

def revert_preprocessing(input_image, height, width):
    image = np.copy(input_image)
    image = image[0]
    image = image.transpose((1, 2, 0))
    image = cv2.resize(image, (width, height))
    return image

yellow = [255, 255, 0]
red = [255, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]

colors = [\
 (None, 'road'),
 (None, 'sidewalk'),
 (None, 'building'),
 (None, 'wall'),
 (None, 'fence'),
 (None, 'pole'),
 (None, 'traffic light'),
 (None, 'traffic sign'),
 (None, 'vegetation'),
 (None, 'terrain'),
 (None, 'sky'),
 (red, 'person'),
 (red, 'rider'),
 (None, 'car'),
 (None, 'truck'),
 (None, 'bus'),
 (None, 'train'),
 (None, 'motorcycle'),
 (None, 'bicycle'),
 (None, 'ego-vehicle')
]

def compute_colors_image(frame, labels_images):
    colors_image = np.copy(frame)
    size = labels_images.shape
    color_counter = 0
    for i in range(size[2]):
        for j in range(size[3]):
            index = int(labels_images[0, 0, i, j])
            color = colors[index][0]
            if color is not None:
                colors_image[0, 0, i, j] = color[2]
                colors_image[0, 1, i, j] = color[1]
                colors_image[0, 2, i, j] = color[0]
                color_counter += 1
    return colors_image, color_counter

def seconds_to_time(seconds):
    t = seconds
    cents = t - int(t)
    cents = int(cents * 100)
    t = int(t)
    hours = int(t / 60 / 60)
    t -= hours * 60 * 60
    minutes = int(t / 60)
    t -= minutes * 60
    secs = t
    if hours > 0:
        return '{}:{:02d}:{:02d}.{:02d}'.format(hours, minutes, secs, cents)
    return '{:02d}:{:02d}.{:02d}'.format(minutes, secs, cents)

log_file = ''

def log(line, write_on_file = True):
    global log_file
    print(line)
    if not write_on_file: return
    with open(log_file, 'a') as f:
        f.write(line + '\n')
        
def clear_log():
    global log_file
    with open(log_file, 'w') as f:
        f.write('')

def infer_on_video(args):
    global log_file
    log_file = '{}.txt'.format(args.i)
    clear_log()
    network = Network()
    network.load_model(args.m, args.d, args.c)
    cap = cv2.VideoCapture(args.i)
    cap.open(args.i)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_period = 1. / frame_rate
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    n_seconds = n_frames * frame_period
    total_time = seconds_to_time(n_seconds)
    log('start_time={}, frame_rate={}, frame_period={}, n_frames={}, n_seconds={}, total_time={}'.format(args.t, frame_rate, frame_period, n_frames, n_seconds, total_time))
    log('frame_index, time, color_counter')
    width = int(cap.get(3))
    height = int(cap.get(4))
    output_video = 'out_{}'.format(args.i)
    out = cv2.VideoWriter(output_video, 0x00000021, 30, (width,height))
    frame_index = 0
    while cap.isOpened():
        seconds = frame_index * frame_period
        flag, frame = cap.read()
        if not flag: break
        key_pressed = cv2.waitKey(60)
        input_shape = network.get_input_shape()
        frame = preprocessing(frame, input_shape[2], input_shape[3])
        network.sync_inference(frame)
        output = network.extract_output()
        labels_images = output['argmax']
        colors_image, color_counter = compute_colors_image(frame, labels_images)
        opacity = 0.5
        frame = cv2.addWeighted(src1 = colors_image, alpha = opacity, src2 = frame, beta = 1. - opacity, gamma = 0)
        frame = revert_preprocessing(frame, height, width)
        time = seconds_to_time(frame_index * frame_period)
        line = '{}, {}, {}'.format(frame_index, time, color_counter)
        write_cond = color_counter > 0 or frame_index == 0 or frame_index == n_frames - 1
        log(line, write_cond)
        cv2.imwrite('FRAME.PNG', frame)
        out.write(frame)
        frame_index += 1
        if key_pressed == 27: break
    out.release()
    cap.release()
    cv2.destroyAllWindows()

def main():
    args = get_args()
    infer_on_video(args)

if __name__ == "__main__":
    main()