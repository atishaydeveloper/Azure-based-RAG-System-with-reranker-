
def chunk_text(text:str, chunk_size:int, chunk_overlap:int)->list[str]:
    chunks=[]
    start=0

    while start < len(text):
        end = start+chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start+=chunk_size-chunk_overlap
    return chunks