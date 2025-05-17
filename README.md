# 𝗧𝗮𝗹𝗸𝟮𝗔𝗪𝗦 – Where language meets the cloud 

This project is a command-line assistant that translates natural language AWS requests into AWS CLI commands using Google Gemini API (LLM).  
It executes those commands on your machine and returns the output, making AWS CLI usage easier and more conversational.

---

## 🚀 Features

- Convert plain English queries to AWS CLI commands using Google Gemini LLM  
- Execute generated AWS CLI commands automatically  
- Interactive CLI prompt for continuous input  
- Error handling for AWS CLI execution errors  

---

## 📋 Prerequisites

- Python 3.8+  
- AWS CLI installed and configured on your machine with valid credentials  
- Google Gemini API key (see below)  
- Internet connection to call Gemini API  

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/shaikMahammedarif/aws-cli-llm
cd aws-llm-helper
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Get your Google Gemini API key

```bash
Go to Google AI Studio

Navigate to the API Keys section and create a new key
```
### 5. Provide your API key

```bash
Set an environment variable GEMINI_API_KEY:

export GEMINI_API_KEY="your_api_key_here"   # On Windows: set GEMINI_API_KEY=your_api_key_here

💡 Alternatively, you can update the config.py file with your API key (not recommended for production).


```


## Deployment

To run this project

```bash
  python main.py

```
```bash
Example queries to try:

create a new s3 bucket in ap-south-1 called test-bucket-arif

list all ec2 instances in us-east-1

delete the s3 bucket named old-bucket

Type exit or quit to stop the program.

```

```bash
🏗️ How It Works (Process Overview)

1-Input: You enter a natural language request for an AWS operation (e.g., “create a new S3 bucket”).

2-LLM Processing: The request is sent to the Google Gemini API, which translates it into a valid AWS CLI command.

3-Command Execution: The generated AWS CLI command is executed locally using Python's subprocess module.

4-Output: The command’s output (success, error, or data) is displayed back in the CLI.

Repeat: It continues to prompt for new commands until you type exit or quit.



```
---

## 📋 Prerequisites
⚠️ Important Notes

- Ensure AWS CLI is properly configured with credentials and permissions before running this tool.

- Gemini API usage may incur costs — monitor your usage on Google Cloud Console.

- Commands are executed locally and may alter your AWS resources — use caution, especially with destructive operations.

- You can customize the prompt or model parameters in llm_client.py to improve command accuracy.

- For production use, never hardcode API keys — use environment variables or secure vaults.


## 🚀 About Me
Happy cloud commanding! ☁️🚀

— Shaik Mahammed Arif
```bash

Let me know when you're ready for me to generate all the actual `.py` source files — we can build the full repo next!

```

Demo : https://youtu.be/5BDRz1MXjgg?si=GNtXLJ4Lcztm3NIr
