# Thread Uploader for Discord

## Introduction

Thread Uploader is a Python-based tool designed for Discord moderators. It automates the process of fetching, processing, and uploading the latest Discord threads to a Vector DB.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python installed on your system.
- A Discord bot with moderation privileges.
- Access to OpenAI and Pinecone services.

## Installation

Follow these steps to install Thread Uploader:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/UmstadAI/Thread-Uploader.git
   cd thread-uploader
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Unix or MacOS
   venv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Environment Variables**
   - Duplicate the `.env.example` file and rename it to `.env`.
   - Fill in the necessary details in `.env`:
     - `DISCORD_TOKEN`: Your Discord Bot Token.
     - `OPENAI_API_KEY`: Your OpenAI API Key.
     - `PINECONE_API_KEY`: Your Pinecone API Key.
     - `PINECONE_ENVIRONMENT`: Your Pinecone Environment.
     - `ISSUE_VECTOR_TYPE`: Your specified Vector Type.

2. **Activate the Virtual Environment**
   Ensure that the virtual environment is activated whenever you work with the project.

## Usage

To run the Thread Uploader, execute the following command in the project directory:

```bash
python task_runner.py
```

## Support

For support, contact berkingurcan@gmail.com

## Contributing

Contributions to the Thread Uploader project are welcome. Please adhere to the project's code of conduct in your interactions.