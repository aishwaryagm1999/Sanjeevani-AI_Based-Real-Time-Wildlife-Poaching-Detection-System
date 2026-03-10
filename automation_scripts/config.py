# config.py

PROJECT_ROOT = r"C:\Users\Aishwarya\Downloads\POACHING_PROJECT"

YOLO_MODEL_PATH = PROJECT_ROOT + r"\yolo_poaching_v1.pt"
GUNSHOT_MODEL_PATH = PROJECT_ROOT + r"\gunshot_model_v3.h5"
MEAN_PATH = PROJECT_ROOT + r"\train_mean.npy"
STD_PATH = PROJECT_ROOT + r"\train_std.npy"

DAILY_PASSCODE = "9382"  # Change daily

LORA_SECRET_KEY = "RANGER_SECRET_2025"

PROXIMITY_RSSI_THRESHOLD = -70  # adjust based on testing

SERVER_PORT = 5000