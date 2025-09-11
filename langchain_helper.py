import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load API key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
llm = ChatGroq(
    temperature=0.7,
    model="llama-3.3-70b-versatile",   # or "llama3-70b-8192"
    groq_api_key=groq_api_key
)

def generate_restaurant_name_and_items(cuisine):
    # Prompt for 7–10 restaurant names
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="Generate 10 creative, unique, and catchy restaurant names for {cuisine} cuisine. "
                 "Return them as a comma separated list."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_names")

    # Get restaurant names
    restaurant_names_response = name_chain.run({'cuisine': cuisine})
    restaurant_names = [name.strip() for name in restaurant_names_response.split(",") if name.strip()]

    # Prompt template for menu items (5–7 per restaurant)
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest 7 unique and authentic menu items for the restaurant {restaurant_name}. "
                 "Return them as a comma separated list."
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    results = {}
    for restaurant_name in restaurant_names[:10]:  # max 10 restaurants
        menu_response = food_items_chain.run({'restaurant_name': restaurant_name})
        menu_items = [item.strip() for item in menu_response.split(",") if item.strip()]
        results[restaurant_name] = menu_items[:7]  # max 7 items

    return results
