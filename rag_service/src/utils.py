from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text_into_chunks(text: str, 
                           max_len: int = 1024, 
                           overlap_len: int = 42):
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_len,
        chunk_overlap=overlap_len,
        length_function=len,
        is_separator_regex=False,
    )

    chunks = [chunk.page_content for chunk in text_splitter.create_documents([text])]
    return chunks