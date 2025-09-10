import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Load API key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
llm = ChatGroq(
    temperature=0.7,
    model="llama-3.3-70b-versatile",   # you can also use "llama3-70b-8192"
    groq_api_key=groq_api_key
)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma separated string."
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Sequential Chain
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
