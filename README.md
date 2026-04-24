flowchart TD
    A[User Notification / Message] --> B[Notification Listener]
    B --> C[Preprocessing Module]
    C --> D[Tokenization (IndicBERT)]
    D --> E[AI Model (PyTorch Lite)]
    E --> F{Risk Score > 0.5?}

    F -- No --> G[Normal Response]
    G --> H[End]

    F -- Yes --> I[Trigger Alert Notification]
    I --> J[Launch Chatbot]
    J --> K{User Responds?}

    K -- Yes --> L[Provide Emotional Support]
    K -- No --> M[Escalation]

    M --> N[Trusted Contact]
    M --> O[Helpline / Web Chat]

    L --> H
