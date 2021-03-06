# Edge Cameras for Detecting Human Presence

### Project Category: Safety

## Project's Story: Conception, Motivation, and Execution

This project was **conceived** when we, Jacqueline and I, were brain-storming about the final project of the Intel Edge AI Scholarship <https://www.udacity.com/scholarships/intel-edge-ai-scholarship>. We talked about many tentative topics. But we were limited by the trained models available. The most popular trained models detect humans. So, we decided to think about human activities. Then, I tought about security cameras. And I remembered that the trained model of **"Part 2. Intel® Edge AI Foundation Course; Lesson 4: The Inference Engine; Video Lecture 13. Exercise: Integrate into an App"** contained a class **people** in its categories for semantic segmentation. I also remembered that I programmed a very sophisticated visualization with transparencies for my project **Semantic Segmentation for Self-Driving Cars with OpenVINO <https://youtu.be/Urph3UHLivY>**. And I said: Why not doing it for detecting human presence in security cameras? Then, this project was born.

My **motivation** for programming this project is very personal. I have a system of 8 security cameras in my building. Many neighbors always ask me for videos of thieves who stole them something or videos of abnormal activities in my neighborhood. When such abuses occur at a specific time and date, it is easy to find the correct videos. However, sometimes things are stolen in the night when nobody is present. That kind of videos are hard to find. And I need to search throughout hours of videos in multiple cameras. The fast forward function accelerates the process. But, when you accelerate videos too much, you can easily miss important events in the videos. So, it's difficult to track human activities. Moreover, at x8 times faster, 8 hours of video can be seen in 1 hour of human attention, making this process tiring and boring for humans who have a decent attention span of 15 minutes. So, histograms of human activities through time are wildly needed because they will show us specific periods of time when humans are present in videos. That's why this project is so important. In the future, edge cameras should include realtime functions for this kind of video analysis.

We **executed** the implementation of this project through:
- the OpenVINO Toolkit;
- the pretrained model semantic-segmentation-adas-0001 <https://docs.openvinotoolkit.org/2018_R5/_docs_Transportation_segmentation_semantic_segmentation_icnet_icv_caffe_desc_semantic_segmentation_adas_0001.html>; 
- semantic segmentation with red transparencies for 2 classes (person and rider);
- logging the frames with human pixels;
- and histograms of human presence through time.

## INSTALLATION INSTRUCTIONS AND COMMANDS

There are 2 ways to execute this project:
- via Udacity workspaces (the easy way);
- and by installing the OpenVINO toolkit in your computer (the hard way).

### Installation via Udacity workspaces (the easy way)

1. Go to the website of the **Intel® Edge AI Scholarship Foundation Course Nanodegree Program.**
2. Go to:
  - Part 2. Intel® Edge AI Foundation Course
  - Lesson 4: The Inference Engine
  - Video Lecture 13. Exercise: Integrate into an App
3. Upload the following files of this github repository into the file system of **13. Exercise: Integrate into an App.** Here is the file structure to upload:
  - models/semantic-segmentation-adas-0001.bin
  - models/semantic-segmentation-adas-0001.xml
  - Histograms.ipynb
  - ch05_20200307012540.mp4.txt
  - ch06_20200307012540.mp4.txt
  - edge_camera.py
  - inspect-edge-cameras.sh
4. Upload the 2 videos of the **Google Drive folder "edge_cameras" <https://drive.google.com/open?id=1NnT8Fcu6XCKArtrCTb35iVgBYLS4PxFU>** into the file system of **13. Exercise: Integrate into an App.** Here is the file structure to upload:
  - ch05_20200307012540.mp4
  - ch06_20200307012540.mp4

### Installing the OpenVINO toolkit in your computer (the hard way)

1. Install Conda with Python 3.5: https://docs.conda.io/projects/conda/en/latest/user-guide/install/
2. Open a Terminal and execute the command: 

```
conda create -n edge-cameras python=3.5
```

3. Activate the conda environment `edge-cameras` with the command: 

```
source activate edge-cameras
```
4. Install OpenCV for Python with the commands:

```
sudo apt update
sudo apt install python3-opencv
```
5. Verify if Open CV was correctly installed with the command:

```
python3 -c "import cv2; print(cv2.__version__)"
```
6. Install the OpenVINO Toolkit with the following instructions:
https://docs.openvinotoolkit.org/latest/_docs_install_guides_installing_openvino_linux.html

7. Download the following files of this github repository into your file system. Here is the file structure to download:
  - models/semantic-segmentation-adas-0001.bin
  - models/semantic-segmentation-adas-0001.xml
  - Histograms.ipynb
  - ch05_20200307012540.mp4.txt
  - ch06_20200307012540.mp4.txt
  - edge_camera.py
  - inspect-edge-cameras.sh
8. Download the 2 videos of the **Google Drive folder "edge_cameras" <https://drive.google.com/open?id=1NnT8Fcu6XCKArtrCTb35iVgBYLS4PxFU>** into your file system. Here is the file structure to download:
  - ch05_20200307012540.mp4
  - ch06_20200307012540.mp4


### Running the project

Open a Terminal and `cd` into the project directory. Run the Unix command `./inspect-edge-cameras.sh` in the terminal. This command will process the 2 input video files `ch05_20200307012540.mp4` and `ch06_20200307012540.mp4`. And this command will produce 4 output files: 2 output video files `(out_*.mp4)` and 2 log files `(*.mp4.txt)`.
  - out_ch05_20200307012540.mp4
  - out_ch06_20200307012540.mp4
  - ch05_20200307012540.mp4.txt
  - ch06_20200307012540.mp4.txt

Alternatively, you can see the contents of the Unix script `inspect-edge-cameras.sh`. It contains 3 lines:
  - `source /opt/intel/openvino/bin/setupvars.sh -pyver 3.5` (This command configures the OpenVINO variables.)
  - `python edge_camera.py -i ch05_20200307012540.mp4 -t "2020/03/07 01:25:40"`
  - `python edge_camera.py -i ch06_20200307012540.mp4 -t "2020/03/07 01:25:40"`
  
Similarly, you can process your own video files of your own security cameras with the following command:
```
python edge_camera.py -i <INPUT VIDEO FILE> -t "<YYYY/MM/DD HH:MM:SS>"
```
  
This command will produce 2 output files: 1 output video file `(out_*.mp4)` and 1 log file `(*.mp4.txt)`. The output video file is the same input video but its pixels detected as humans will be marked with red transparencies. So, security guards will be very aware of these parts of the video. The log file contains some metadata about the video processed and 3 columns of data: `frame_index`, `time`, and `color_counter`. This information will be recorded only when humans appear in some specific frames and the number of human pixels will be counted in order to draw a histogram of human pixels through time.

## Project's Goal

The goal of this project is to analyze videos in realtime in order to detect human activities. So, important statistics are simultaneously precomputed when videos in security cameras are being filmed. The ultimate goal is to create "edge cameras" that are constantly filming and at the same time analyzing videos in realtime. While this goal is not fully achieved in this project, a proof-of-concept is shown. Semantic segmentation is slow. But, future "edge devices" will have an enormous computational power due to Moore's law and the Kurzweil's Law of Accelerating Returns: <https://www.kurzweilai.net/the-law-of-accelerating-returns>

While this project is very general and can be applied to any security camera, the goal of this project is easier to see with a personal example: I have a system of 8 security cameras in my building. Many neighbors always ask me for videos of thieves who stole them something or videos of abnormal activities in my neighborhood. When such abuses occur at a specific time and date, it is easy to find the correct videos. However, sometimes things are stolen in the night when nobody is present. That kind of videos are hard to find. And I need to search throughout hours of videos in multiple cameras. The fast forward function accelerates the process. But, when you accelerate videos too much, you can easily miss important events in the videos. So, it's difficult to track human activities. Moreover, at x8 times faster, 8 hours of video can be seen in 1 hour of human attention, making this process tiring and boring for humans who have a decent attention span of 15 minutes. So, histograms of human activities through time are wildly needed because they will show us specific periods of time when humans are present in videos. That's why this project is so important. In the future, edge cameras should include realtime functions for this kind of video analysis.

## How the "Intel® Edge AI Fundamentals Course" helped us

The "Intel® Edge AI Fundamentals Course" taught us the programming tools and techniques to program this project. Learning the OpenVINO Toolkit and how to exploit its pretrained models was fundamental to build this project. We have learned a lot and we are very thankful to Udacity for this exciting learning opportunity.

Specifically, when we brain-storming about the initial aspects of this project, I remembered that the trained model of **"Part 2. Intel® Edge AI Foundation Course; Lesson 4: The Inference Engine; Video Lecture 13. Exercise: Integrate into an App"** contained a class **people** in its categories for semantic segmentation. I also remembered that I programmed a very sophisticated visualization with transparencies for my project **Semantic Segmentation for Self-Driving Cars with OpenVINO <https://youtu.be/Urph3UHLivY>**. And I said: Why not doing it for detecting human presence in security cameras? Then, this project was born.

## Team Members

Juan Carlos Kuri Pinto / @Juan Carlos Kuri Pinto, Jacqueline Susan Mejía Cáceres / @susyjam 

## Edge Cameras for Detecting Human Presence (Camera 5)<br/>
<b>YouTube video: https://youtu.be/1PgzfK5YIpk</b>

My acting skills as a thief are absolutely amazing. (No actor would play the role of a thief by greeting at both cameras.)

In the video, I appear at 0:33 and I disappear at 1:05. Pixels in red are counted as human pixels and will be shown in the histogram of human pixels through time.

![Camera 5](/images/cam5.jpg)

In like manner, the histogram of human pixels through time shows human presence from 0:34 to 1:03, approximately. This histogram was computed by the Jupyter notebook [Histograms.ipynb](Histograms.ipynb).

![Camera 5](/images/hist5.jpg)

## Edge Cameras for Detecting Human Presence (Camera 6)<br/>
<b>YouTube video: https://youtu.be/o6oEQlBGtCg</b>

In the video, I appear at 0:20 and I disappear at 1:07. Pixels in red are counted as human pixels and will be shown in the histogram of human pixels through time.

![Camera 6](/images/cam6.jpg)

In like manner, the histogram of human pixels through time shows human presence from 0:30 to 1:06, approximately. This histogram was computed by the Jupyter notebook [Histograms.ipynb](Histograms.ipynb).

![Camera 6](/images/hist6.jpg)

We can conclude the detection of human presence is somewhat accurate with some false negatives and zero false positives! False negatives are pixels where I appear that are not detected by the model. And false positives are non-human objects marked as humans. (Fortunately, we have no false positives in the tests.) The little amount of false negatives is compensated by the presence of true positives that make a blob of human presence in the histogram. And the zero amount of false positives is wonderful because security guards won't waste their time analyzing annoying false positives. So, this detector is very good and we are proud of it.
