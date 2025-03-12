from worker import celery_app as app

from chunkers import get_chunker
from models.chunk_request import ChunkRequest

@app.task(name="chunk_text")
def chunk_text(text: str, chunk_type: str, chunk_size: int):
    try:
        # Fetch the appropriate chunker class (ensure it does not return functions)
        ChunkerClass = get_chunker(chunk_type)
        
        # Initialize the chunker
        chunker = ChunkerClass(chunk_size)

        # Perform chunking operation (make sure this is synchronous)
        chunks = chunker.chunk(text)
        # print(f"Chunks of text: {chunks}")
        # Ensure chunks is serializable (should be a list or dict)
        if isinstance(chunks, list):  # Ensure chunks is a list
            return chunks
        else:
            raise ValueError("Chunking result must be a serializable list")

    except Exception as e:
        print(f"Failed to chunk the text: {e}")
        return None
