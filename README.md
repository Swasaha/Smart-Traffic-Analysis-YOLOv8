
# **Smart Traffic Analysis Using YOLOv8**  

## **Overview**  
This project leverages **YOLOv8** for real-time vehicle detection and tracking, integrating the **Google Gemini API** to extract vehicle attributes. The system provides insights into traffic patterns, congestion levels, and vehicle classification, enabling efficient urban planning and intelligent transportation management.

## **Features**  
- 🚗 **Real-time vehicle detection and tracking** using **YOLOv8**  
- 📊 **Traffic flow visualization** with dynamic graphs  
- 🔍 **Vehicle attribute extraction** via **Google Gemini API**  
- 🛣 **Smart insights for urban traffic management**  

## **Installation**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Swasaha/Smart-Traffic-Analysis-YOLOv8.git
cd Smart-Traffic-Analysis-YOLOv8
```

### **2️⃣ Install Dependencies**  
Ensure you have Python **3.8+** installed, then run:  
```bash
pip install -r requirements.txt
```

### **3️⃣ Download YOLOv8 Model**  
Download the YOLOv8 weights:  
```bash
wget https://github.com/ultralytics/yolov8/releases/download/v8/yolov8n.pt
```

## **Usage**  

### **Run Traffic Analysis**  
Execute the script to start real-time traffic analysis:  
```bash
python traffic_analysis.py
```

### **Customize Parameters**  
Modify configurations in **config.py** to adjust detection settings.

## **Project Structure**  
```
📂 Smart-Traffic-Analysis-YOLOv8  
 ├── 📜 README.md  
 ├── 📜 requirements.txt  
 ├── 📜 traffic_analysis.py  
 ├── 📜 config.py  
 ├── 📂 models/  
 ├── 📂 data/  
 ├── 📂 utils/  
```

 
