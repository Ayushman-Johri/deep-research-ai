# # main.py

# from agents.research_agent import run_research
# from agents.answer_agent import run_answer

# def main():
#     query = input("Enter your research query: ")

#     print("\n🔎 Researching...")
#     research_output = run_research(query)
#     print("\n--- Research Output ---\n")
#     print(research_output)

#     print("\n🧠 Generating Final Answer...")
#     final_answer = run_answer(research_output)
#     print("\n--- Final Answer ---\n")
#     print(final_answer)

# if __name__ == "__main__":
#     main()
# main.py
from agents.hf_llm import HuggingFaceLLM

# Initialize the HuggingFaceLLM instance
llm = HuggingFaceLLM(model_name="gpt2", api_key="your api key")

# Now you can call methods like _generate
result = llm._generate("Write a brief explanation of Quantum Computing.")
print(result)

