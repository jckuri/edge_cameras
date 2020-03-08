# Edge Cameras for Detecting Human Presence

### Project Category: Safety

## Project's Story: Conception, Motivation, and Execution

This project was conceived when we, Jacqueline and I, were brain-storming about the final project of the Intel Edge AI Scholarship <https://www.udacity.com/scholarships/intel-edge-ai-scholarship>. 

**Semantic Segmentation for Self-Driving Cars with OpenVINO <https://youtu.be/Urph3UHLivY>**

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
4. Upload the 2 videos of the **Google Drive folder "edge_cameras" <https://drive.google.com/open?id=1NnT8Fcu6XCKArtrCTb35iVgBYLS4PxFU>** into the file system of **13. Exercise: Integrate into an App.** Here is the file structure:
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

### Running the project

Run the Unix command `./inspect-edge-cameras.sh` in the terminal. This command will process the 2 video files `ch05_20200307012540.mp4` and `ch06_20200307012540.mp4`. And this command will produce 4 output files: 2 output video files `(out_*.mp4)` and 2 log files `(*.mp4.txt)`.
  - out_ch05_20200307012540.mp4
  - out_ch06_20200307012540.mp4
  - ch05_20200307012540.mp4.txt
  - ch06_20200307012540.mp4.txt

Alternatively, you can see the contents of the Unix script `inspect-edge-cameras.sh`. It contains 3 lines:
  - `source /opt/intel/openvino/bin/setupvars.sh -pyver 3.5`
  - `python edge_camera.py -i ch05_20200307012540.mp4 -t "2020/03/07 01:25:40"`
  - `python edge_camera.py -i ch06_20200307012540.mp4 -t "2020/03/07 01:25:40"`
  
Similarly, you can process your own video files of your own security cameras with the following command:
```
python edge_camera.py -i <VIDEO FILE> -t "<YYYY/MM/DD HH:MM:SS>"
```
  
This command will produce 2 files: 1 output video file `(out_*.mp4)` and 1 log file `(*.mp4.txt)`. The output video file is the same video but its pixels detected as humans will be marked with red transparencies. So, security guards will be very aware of this parts of the video. The log file contains some metadata about the video processed and 3 columns of data: `frame_index`, `time`, and `color_counter`. This information will be recorded only when humans appear in some specific frames and the number of human pixels will be counted in order to draw a histogram of human pixels through time.

## Project's Goal

## How the "Intel® Edge AI Fundamentals Course" helped us

## Team Members

Juan Carlos Kuri Pinto / @Juan Carlos Kuri Pinto, Jacqueline Susan Mejía Cáceres / @susyjam 

## Edge Cameras for Detecting Human Presence (Camera 5)<br/>
<b>YouTube video: https://youtu.be/1PgzfK5YIpk</b>

![Camera 5](/images/cam5.jpg)

![Camera 5](/images/hist5.jpg)

## Edge Cameras for Detecting Human Presence (Camera 6)<br/>
<b>YouTube video: https://youtu.be/o6oEQlBGtCg</b>

![Camera 6](/images/cam6.jpg)

![Camera 6](/images/hist6.jpg)

# The Evaluation Criteria:

## Innovation & Creativity (30%) 
It evaluates on the novelty, innovation and creativity introduced in the project such that it is appealing.

## Relevance & Potential (30%) 
It evaluates the project on the impact that the project may create on the society, or for the betterment of technology, humanity or as a business model which solves a major issue.

## Model Accuracy & Demonstration of the Course materials (20%) 
It evaluates the project on the test accuracy and how much the project demonstrates what is learned from the Challenge.

## Speed, Robustness & Fairness (10%) 
How fast is the model in generating results in production environment as well as how robust the model is to anomalies and Trusted AI issues i.e. whether the model is fair or seems biased.

## Ease of Use, Scalability & Flexibility (10%) 
How well is the code written, is it modular and well documented, easy to train and test, is the model scalable and is it flexible enough to change various parameters (data, hyperparams, model, etc.)
