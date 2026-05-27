import pymupdf
from langchain.agents import create_agent
import os
from dotenv import load_dotenv
load_dotenv()
def extract_pdf_text(file_name):
    doc = pymupdf.open("File_Repo/"+file_name)
    extracted_text = []
    for page in doc:
        # print(page.get_text())
        extracted_text.append(page.get_text())
    return "\n".join(extracted_text)

file_name = "Demo_Pilot_sample_document_002.pdf"
pdf_content = extract_pdf_text(file_name)
agent = create_agent(
    model = "openai:gpt-5.4",
    tools = [],
    system_prompt = "Your an helpful assistant for extract the require information from the given pdf content. This is an extracted content form the pdf: " + pdf_content
    )

result = agent.invoke(
    {
        "messages":[{"role": "user", "content": "please get the pilot name form the pdf"}]
    }
)
print(result)

    

