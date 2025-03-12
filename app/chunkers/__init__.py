from .chunker import Chunker
from .fixed_chunker import FixedSizeChunker
from .semantic_fake_chunker import SemanticFakeChunker
from .semantic_chunker import SemanticChunker

def get_chunker(chunker_type: str):
    match chunker_type:
        case "fixed":
            return FixedSizeChunker
        case "fake_semantic":
            return SemanticFakeChunker  
        case 'semantic':
            return SemanticChunker
        case _:
            raise ValueError(f"Unsupported chunker type: {chunker_type}")