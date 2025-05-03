from unstructured.partition.pdf import partition_pdf
# from unstructured.documents import PDF

PATH_TO_FILE = "data/pdfs/demo-pdf.pdf"

# elements = partition_pdf(PATH_TO_FILE, strategy="hi_res")
elements = partition_pdf(PATH_TO_FILE)

print(f"Number of elements: {len(elements)}")
for i, element in enumerate(elements):
    print(f"Element {i}:")
    print(f"  - Type: {type(element)}")
    print(f"  - Text: {element.text[:100]}")  # Print first 100 characters of text
    print(f"  - Metadata: {element.metadata}")
    print()