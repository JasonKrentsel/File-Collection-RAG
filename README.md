# File-Collection-RAG

## Overview

This project is a basic proof of concept for a Retrieval-Augmented Generation (RAG) system. It is designed to manage a collection of files stored in a single directory, generating detailed summaries and vector embeddings using the Google Gemini API.

## Features

-   **File Management**: Add and delete files from a local database.
-   **Summarization**: Automatically generates detailed summaries of various file types using Google Gemini.
-   **Vector Embeddings**: Creates vector embeddings for efficient retrieval and similarity search.
-   **Search**: Search for files based on user query.

## Getting Started

### Prerequisites

-   Python 3.x
-   Google API key (for accessing Google Gemini)

### Setup

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure your Google API key:
    - Open `config.py.example` and set your API key:
        ```python
        GOOGLE_API_KEY = 'your_api_key_here'
        ```
    - Rename the file to `config.py`.

### Usage

1. Run the main application:

    ```bash
    python main.py
    ```

2. After running the application once, you can add files to the `Files` directory. The system will automatically generate summaries and embeddings for the files added.

3. To check for changes in the files and update the database, the application will prompt you accordingly when ran again.

## File Structure

-   `main.py`: The main entry point for the application.
-   `Source/`: Contains the source code for summarization and embedding utilities.
-   `Files/`: Directory where files are stored for processing, generated after the first run of main.py.
-   `config.py.example`: Example configuration file for setting the Google API key. Rename to config.py after setting the key.
-   `README.md`: Project documentation.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

-   Google Gemini API for summarization and embedding capabilities.
-   Open-source community for various libraries and tools used in this project.
