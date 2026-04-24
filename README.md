
# 🧠 Sanjeevani-AI (SafeBot)
**Passive Suicide Risk Detector & Mental Health Support System**

---

## 📌 Overview
Sanjeevani-AI (SafeBot) is an on-device AI-powered mental health system designed to detect suicide risk in real-time and provide immediate emotional support.

Unlike traditional systems, it:
- Works completely offline
- Supports multilingual + code-mixed languages (Tenglish, Hinglish)
- Ensures 100% user privacy
- Provides automated chatbot intervention with escalation

---

## 🚀 Features
- Real-time suicide intent detection
- AI chatbot for emotional support  
- Notification-based monitoring (no intrusive keylogging)  
- Web chatbot escalation  
- Fully on-device processing (PyTorch Lite)  
- Supports English + Indic languages  

---

## 🏗️ Project Structure
```
Sanjeevani-AI/
│
├── app/                         # Android application
│   ├── src/
│   ├── assets/
│   │   └── model.ptl           # Trained AI model (PLACE HERE)
│
├── model/
│   ├── training_code.py
│   ├── preprocessing.py
│   └── model.pt               # Original trained model
│
├── dataset/
│   ├── suicide_dataset.csv    # Training dataset (PLACE HERE)
│   └── augmented_data.csv
│
├── chatbot/
│   └── chatbot_link.txt       # Escalation chatbot URL
│
├── docs/
│   └── project_report.pdf
│
└── README.md
```

---

## 📂 Where to Keep Important Files

### Trained Model
File: `model.ptl`  
Location:
```
app/src/main/assets/model.ptl
```

### Training Dataset
File: `suicide_dataset.csv`  
Location:
```
dataset/suicide_dataset.csv
```

### Chatbot Escalation Link
Example:
```
https://supportly.web.app/chat
```

Store in:
```
chatbot/chatbot_link.txt
```

OR inside code:
```kotlin
val chatbotUrl = "https://supportly.web.app/chat"
```

---

## 🧠 Model Details
- Model: IndicBERT (Fine-tuned)
- Framework: PyTorch → TorchScript → PyTorch Lite
- Task: Binary Classification
  - 0 → Non-Suicidal
  - 1 → Suicidal
 
  #Archeitecture Flow
<img width="1855" height="2648" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/c53ecf02-1e0a-42c2-99bd-7b7c662ae97b" />

- Accuracy: ~88.8%
- F1 Score: ~0.89
- Recall (Suicidal): 0.92
- ROC-AUC: 0.96

---

## ⚙️ How It Works
1. User messages are captured via notifications  
2. Text is preprocessed and tokenized  
3. AI model predicts risk score  
4. If risk exceeds threshold:
   - Alert notification is triggered  
   - Chatbot provides emotional support  
5. If needed, user is redirected to web chatbot  

---

#Sequence Diagram
<img width="2500" height="1362" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/f5953c41-9ac8-4653-856a-9309bb532b5d" />

### 📊 Performance

## 📱 Tech Stack

### Mobile App
- Kotlin / Java  
- Android Studio  

### AI Model
- PyTorch  
- TorchScript  
- IndicBERT  

### Other
- SQLite  
- NotificationListenerService  

---

## 🔒 Privacy First
- No cloud processing  
- No external APIs  
- All processing happens on-device  
- User data never leaves the phone  

---

## 🧪 How to Run
1. Clone repository
```
git clone <your-repo-link>
```

2. Open in Android Studio  

3. Add model file:
```
model.ptl → app/src/main/assets/
```

4. Run on Android device  

---

## ⚠️ Limitations
- Possible false positives due to vocabulary limits  
- Needs better handling of code-mixed language  
- Requires dynamic vocabulary expansion  

---

## 🔮 Future Improvements
- Federated learning  
- Improved multilingual support  
- Wearable integration  
- iOS / Web versions  


## 📜 License
For academic and research use only  

---

## ❤️ Final Note
This project focuses on early suicide risk detection with privacy, empathy, and real-time support.
