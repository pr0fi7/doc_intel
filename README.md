# DocIntel

DocIntel is a FastAPI-based tool designed to streamline the processes of embedding, chunking, and other essential tasks in creating chatbots or NLP projects. We handle the complex aspects, allowing you to effortlessly utilize endpoints for embeddings and chunking according to your preferences. Additionally, DocIntel offers advanced text extraction capabilities, including extracting text from images embedded within documents.

## Features

- **Simplified Embedding and Chunking**: Easily process and manage text embeddings and chunking through intuitive API endpoints.
- **Advanced Text Extraction**: Extract text from various document formats, including images, to ensure comprehensive data processing.
- **Customizable Workflows**: Tailor the tool to your specific NLP project requirements, enhancing flexibility and efficiency.

## Installation

To get started with DocIntel, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/pr0fi7/doc_intel.git
   cd doc_intel

2. **Set Up the Virtual Environment**:

It's recommended to use a virtual environment to manage dependencies:

  ```bash
  python3 -m venv venv
  ```
3. Activate the Virtual Environment:

  - On Windows:
  ```bash
  venv\\Scripts\\activate
  ```
  - On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

4. Install Dependencies:

With the virtual environment activated, install the required packages:
```bash
pip install -r requirements.txt
```

5.Run the Application:

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```
The application will be accessible at http://127.0.0.1:8000.

## Usage

DocIntel provides API endpoints for embedding, chunking, and text extraction. Refer to the [API documentation](http://127.0.0.1:8000/docs) for detailed information on available endpoints and their usage.

## Contributing

Contributions to DocIntel are welcome. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Commit your changes with clear messages.
5. Push your changes to your forked repository.
6. Submit a pull request detailing your changes.

Please ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

DocIntel is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the web framework.
- [Uvicorn](https://www.uvicorn.org/) for the ASGI server.
- [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation.
