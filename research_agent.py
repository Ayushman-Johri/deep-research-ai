# agents/research_agent.py

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from agents.hf_llm import HuggingFaceLLM

# Instantiate HuggingFaceLLM with necessary credentials
llm = HuggingFaceLLM(
    api_url="gpt2",
    api_key="your api key"
)

# Define the prompt template
prompt = PromptTemplate.from_template("""
You are a research expert AI. Research the following question deeply and provide a detailed answer:

Question: {query}

Answer:
""")

# Create the LLM chain with the prompt and LLM
llm_chain = LLMChain(llm=llm, prompt=prompt)

def run_research(query: str):
    # Use the chain to process the query and get the answer
    return llm_chain.run({"query": query})  # Using 'run' directly instead of RunnableSequence
# Correct initialization with both model_name and api_key
llm = HuggingFaceLLM(model_name="gpt2", api_key="your_api_key_here")

# Now you can call methods like _generate
result = llm._generate("machine learning")
print(result)
