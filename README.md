# UIoT-Crowd-Detector

## Description
The system proposed in this work presents an innovative solution for identifying gatherings in controlled environments, using an IoT network and fog computing. Through distributed processing of IP camera images, the system employs computer vision algorithms, such as YOLOv4-tiny, to detect and monitor potential violations of social distancing. This cost-effective approach, with SBC devices installed on the same local network as the cameras, enables efficient image processing without the need for sending them to a centralized system, resulting in savings in transmission and storage resources. The system architecture, based on fog computing, facilitates real-time detection and notification to relevant authorities, making it a valuable tool for managing situations that require intervention to ensure social distancing and prevent disease spread, such as in the context of the COVID-19 pandemic.

Reference of the scientific article:
- Dias, B. S. S.; Mello, I. P. E.; Caldas Filho, F. L.; Mata, R. Z. A.; Almeida, L. O.; Mendonca, F. L. L.; Sousa Jr, R. T.. System for the identification of gatherings operating in IoT Networks and Fog Computing. RISTI (Porto, Portugal), v. 47, p. 300-311, 2022. ISSN: 1646-9895.

The full article is available at [link](https://www.proquest.com/docview/2648272139?pq-origsite=gscholar&fromopenview=true&sourcetype=Scholarly%20Journals).

## Requirements
- Python 3.8^
- Pip 20.2.3^
- Virtualenv 20.0.31

## Usage
1. Clone the repository and navigate to it:
`git clone https://github.com/uiot/crowd_detector.git
cd crowd_detector`

2. Create a virtual environment and activate it:
`virtualenv venv
source venv/bin/activate # Linux`

3. Install required packages:
`pip install -r requirements.txt`

4. Download YOLO's weights to the `yolo_files` folder:
`wget -O ./crowd_detector/yolo_detection/yolo_files/yolo.weights \
https://pjreddie.com/media/files/yolov4.weights`

5. Execute the main code:
`python ./crowd_detector/main.py`

## Config
Configuration can be done in the `./crowd_detector/config.yaml` file.

Fields
`reports_filename`: Must be a JSON.
