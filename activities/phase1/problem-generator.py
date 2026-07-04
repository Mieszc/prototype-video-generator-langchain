from dotenv import load_dotenv
from typing import Dict, Any
from dataclasses import dataclass
from pydantic import BaseModel
from langchain.agents import AgentState, create_agent
from langchain.messages import HumanMessage


load_dotenv()

@dataclass
class InputData:
    def __init__(self, product_name: str, target_audience: str, product_description: str) -> None:
        self.product_name = product_name
        self.product_description = product_description
        self.target_audience = target_audience

class OutputSchema(BaseModel):
    """Schema for outputting the pgenerated problems. Format the response data list from plain text to a dictionary where the number is the key and text value is the value"""

    output: Dict[int, Any]

input = InputData("70mai Air Purifier Pro", "Daily commuters, Parents with kids / families, Allergy sufferers, People with sensitive lungs", "70mai Air Purifier Pro For the sake of your health The operation of combustion engines results in the production of pollutants. While driving a car, tires and brake pads also wear down. These microscopic particles pose a real threat to our health. If you multiply all these factors by the number of vehicles on the roads, you can say with full confidence that the risk increases with every kilometer traveled. Therefore, purifying the air in the car as well as at home is a sensible step. Nowadays, we spend a lot of time in the car—just consider how much time we devote each day to commuting to work. The 70mai Air Purifier Pro car air purifier will help reduce exposure to harmful, health-negative factors. This purifier is a great option for allergy sufferers, as well as for people who care about their own health and the health of their loved ones and want to improve the air quality in their car or in rooms where they spend longer periods of time. Key features of the 70mai Air Purifier Pro The 70mai purifier is a device designed as a car air purifier, but it can also be successfully used as a desk or room purifier. Its efficient brushless motor offers a high fan speed, quiet operation, and a long service life. This car air purifier can achieve a CADR (Clean Air Delivery Rate) of 52 m³/h. The purifier is equipped with a high-quality Cubic Optoelectronics dust sensor, which continuously monitors changes in pollution levels in the car and adjusts its operation accordingly. The device is also characterized by low power consumption. Efficient and effective filter The 70mai Air Purifier Pro air purifier is equipped with a high-efficiency filter that thoroughly cleans the air flowing through it in your car. The main element of the filter is filter paper, which effectively captures particles found in dust and smoke, as well as the well-known PM2.5 particles and pollen. The filter is replaceable. You can choose between the AC02-1 filter and the AC02-2 filter, which additionally captures formaldehyde. Deduct 5 new problems for the provided product that follow all of these rules.")

#@tool
#def format_output(response_main: str) -> Dict[str, Any]:
   # """Format the response data list from plain text to a dictionary where the number is the key and text value is the value"""
   # response = response_formatter.invoke

problem_generator_agent = create_agent(
    model="gpt-5-mini",
    response_format=OutputSchema,
    system_prompt="""You are an expert brand strategist and creative director specializing in problems that the e-commerce products solve for the users. Your task is to analyze the user's product, product description and target auudience for this product and output a list of 5 specific problems that the audience is most likely to have that this product will solve.  

    **Strict Rules for Problem Analysis:**  

    1. **Realistic and measurable:** Each output must describe a single, clear problem that a text-to-text AI can realistically understrand and elaborate on with creative production. Avoid overly complex problems with no way to identify(measure) the successful outcome.  

    2. **Problem -- Product -- Solution Arc:** the probelm must bew solvable with the use of product. Avoid situation when the deducted probelm is realistic but not solvable by the product.   

    3. **Format:** Output ONLY a numbered list of the 5 problems. Then use the ‘with_structured_output’ provided output schema and input the list into a dictionary where each point number is the key and the text value is the value."**
    """
)

config = {"configurable": {"thread_id": "1"}}

response = problem_generator_agent.invoke(
    {"messages": [HumanMessage(content=f"Details of the product to analyze(Product Name: {input.product_name}, Target Audience: {input.target_audience}, Product Description: {input.product_description})")]},
    config
)

print(response["messages"][-1].content)