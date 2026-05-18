# Bulk Email Sender

A Python-based utility to send personalized bulk emails to potential clients. It supports both plain text and HTML formats, making it ideal for business outreach.

## Features
- **Personalization**: Automatically injects company names into subjects and bodies.
- **Multipart Emails**: Sends both HTML and Plain Text versions for better compatibility.
- **Security**: Uses environment variables to manage sensitive credentials.
- **Logging**: Provides real-time feedback on the success or failure of sent emails.

## Prerequisites
- Python 3.x
- A Gmail account with **2-Step Verification** enabled.
- A Google **App Password** (since standard passwords are not supported for SMTP).

## Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Create a `.env` file in the root directory and add your credentials:
   ```env
   SENDER_EMAIL=your-email@gmail.com
   PASSWORD=your-app-password
   ```

## Usage
Run the script to start sending emails:
```bash
python main.py
```