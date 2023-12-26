# Thread Uploader for Discord

## Introduction

Thread Uploader is a Python-based tool designed for MINA Protocol Discord moderators. It automates the process of fetching, processing, and uploading the latest Discord threads in the zkapps-developers and zkapps-questions channels to a zkApp Umstad Vector DB.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python installed on your system.
- A Discord bot with read message history moderation privileges.
- Access to OpenAI and Pinecone services.

## Installation

Follow these steps to install Thread Uploader:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/UmstadAI/Thread-Uploader.git
   cd Thread-Uploader
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

## GPT Model
You can also use gpt-4-1106-preview model depends on tha API consistency. Sometimes it stuck. When it is stable, using gpt4 would be better to process.

So, you can change the model in the processor.py:

```python
response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={"type": "json_object"},
        temperature=0.8,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": str(contents)},
        ],
    )
```

## Usage

To run the Thread Uploader, execute the following command in the project directory:

```bash
python task_runner.py
```

## Support

For support, contact berkingurcan@gmail.com

## Contributing

Contributions to the Thread Uploader project are welcome. Please adhere to the project's code of conduct in your interactions.