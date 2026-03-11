
SANJEEVANI
AI-Based Real-Time Wildlife Poaching Detection System
===============================================================

Project Domain: Artificial Intelligence / Computer Vision / IoT
Application: Wildlife Protection and Anti-Poaching Monitoring



1. PROBLEM STATEMENT
===============================================================

Wildlife poaching is a major threat to endangered species worldwide.
Forest departments often struggle to monitor vast forest areas due to:

• Limited ranger manpower
• Poor visibility in dense forests
• Delayed reporting of poaching incidents
• Lack of automated surveillance systems

Poachers typically operate with firearms and often blend with the
environment, making it difficult for traditional surveillance systems
to detect threats in real time.

The objective of this project is to design an intelligent system that
can automatically detect potential poaching activities using:

• Computer Vision
• Audio Gunshot Detection
• AI-based Threat Classification
• Automated Ranger Alert System



2. SYSTEM OVERVIEW
===============================================================

The SANJEEVANI system integrates multiple AI modules to detect and
respond to poaching events in real time.

The system pipeline:

Camera / Drone Feed
        |
        V
YOLOv8 Object Detection
(human, gun, elephant, jacket)
        |
        V
Threat Logic Engine
        |
        V
Poacher Classification
        |
  -----------------------------
  |            |              |
  V            V              V
SMS Alert   LoRa Message   Evidence Logging
                         |
                         V
                     Map Visualization



3. OBJECT DETECTION MODEL
===============================================================

Model Used:
YOLOv8s (Ultralytics)

Framework:
PyTorch

Purpose:
Detect objects related to poaching activities.

Classes detected:

0 -> gun
1 -> elephant
2 -> human
3 -> jacket

Interpretation:

human + jacket = ranger

human without jacket = poacher

human + gun = armed poacher



4. YOLO TRAINING CONFIGURATION
===============================================================

Model: yolov8s.pt

Image Size: 832
Epochs: 60
Batch Size: 16
Optimizer: AdamW
Initial Learning Rate: 0.0008

Training Augmentations:

mosaic = 1.0
mixup = 0.2
scale = 0.9
translate = 0.2
degrees = 10
shear = 2
fliplr = 0.5

Color Augmentation:

hsv_h = 0.015
hsv_s = 0.7
hsv_v = 0.4

Learning Rate Scheduler:
cos_lr = True

Backbone Freezing:
freeze = 10 layers

Early Stopping:
patience = 20

Hardware Used:

GPU: NVIDIA RTX 4060 Laptop GPU
CUDA: 12.1
PyTorch: 2.5.1+cu121



5. DATASET DETAILS
===============================================================

Dataset Images: 200+
Audio Files: 2000+

Referenced Datasets:
Images generated with AI (Dall.E)
https://www.kaggle.com/datasets/emrahaydemr/gunshot-audio-dataset
https://www.kaggle.com/datasets/javohirtoshqorgonov/noise-audio-data
https://www.kaggle.com/datasets/shijo96john/elephant-thermal-images
https://www.kaggle.com/datasets/vivmankar/asian-vs-african-elephant-image-classification


6. YOLO MODEL PERFORMANCE
===============================================================

Final Validation Metrics

Precision: 0.856
Recall: 0.855
mAP@0.5: 0.914
mAP@0.5:0.95: 0.566

Per-Class Performance:

gun
Precision: 1.00
Recall: 0.651
mAP50: 0.796
mAP50-95: 0.354

elephant
Precision: 0.851
Recall: 0.880
mAP50: 0.881
mAP50-95: 0.578

human
Precision: 0.941
Recall: 0.889
mAP50: 0.984
mAP50-95: 0.536

jacket
Precision: 0.631
Recall: 1.00
mAP50: 0.995
mAP50-95: 0.796


Training stopped early due to EarlyStopping.

Best model saved at:

runs/detect/train17/weights/best.pt



7. INFERENCE SPEED
===============================================================

Preprocess time: 0.8 ms
Inference time: 7.0 ms
Postprocess time: 1.7 ms

Average total inference time per image ≈ 9.5 ms



8. GUNSHOT DETECTION MODEL
===============================================================

Model Type:
Deep Learning Binary Classifier

Input Features:

• Log Mel Spectrogram
• MFCC
• Spectral Centroid
• Spectral Rolloff
• RMS Energy
• Zero Crossing Rate
• Delta Features

These features are stacked to create a multi-channel audio feature map.



9. GUNSHOT MODEL PERFORMANCE
===============================================================

Validation Samples: 807

Confusion Matrix:

            Predicted
            0     1
Actual 0  348    57
Actual 1    2   400

Classification Report:

Class 0 (Non-Gunshot)
Precision: 0.99
Recall: 0.86
F1-score: 0.92

Class 1 (Gunshot)
Precision: 0.88
Recall: 1.00
F1-score: 0.93

Overall Accuracy:

93%



10. THREAT CLASSIFICATION LOGIC
===============================================================

The system determines poaching events using object combinations.

Rules implemented:

human + jacket -> Ranger

human without jacket -> Poacher

human + gun -> Armed Poacher

Gunshot detected -> Critical Alert



11. SYSTEM COMPONENTS
===============================================================


central_server.py

Main system controller that coordinates all modules.


threat_logic.py

Implements AI threat classification logic.


yolo_detector.py

Runs YOLO object detection inference.


gunshot_detector.py

Detects gunshot sounds using audio classification.


proximity_utils.py

Calculates spatial distance between detected objects.


config.py

Contains system parameters and configuration.


lora_handshake.py

Handles communication between server and ranger devices.


ranger_device_sim.py

Simulates ranger device receiving alerts.


sms_alert.py

Sends SMS alerts when threats are detected.


evidence_logger.py

Stores evidence including images and detection metadata.


map_generator.py

Generates map visualization of detected events.


data.yaml

YOLO dataset configuration file.



12. SYSTEM OUTPUT
===============================================================

When a poacher event is detected the system:

1. Logs evidence
2. Sends SMS alerts to rangers
3. Sends LoRa alert packets
4. Updates event location on monitoring map



13. FUTURE IMPROVEMENTS
===============================================================

Possible future enhancements:

• Thermal camera integration
• Drone surveillance automation
• Multi-frame object tracking
• Satellite monitoring integration
• Ranger patrol prediction using AI


