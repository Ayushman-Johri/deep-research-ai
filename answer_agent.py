# agents/answer_agent.py

from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from agents.hf_llm import HuggingFaceLLM

# Load your Hugging Face model
llm = HuggingFaceLLM(
    api_url="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",  # Same or different model
    api_key="your api key"
)

# Answer prompt
answer_prompt = PromptTemplate(
    input_variables=["research_output"],
    template=(
        "You are an expert AI. Based on the detailed research provided below, give a final concise answer.\n\n"
        "Research Output: {research_output}\n\n"
        "Answer:"
    )
)

# Chain using RunnableSequence
answer_chain = RunnableSequence(
    steps=[answer_prompt, llm]
)

def run_answer(research_output: str) -> str:
    response = answer_chain.invoke({"research_output": research_output})
    return response
