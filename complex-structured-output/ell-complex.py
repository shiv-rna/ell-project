import ell
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from ell import Message
from typing import List

load_dotenv()

# Structured Output 
class MovieReview(BaseModel):
    title: str = Field(description="The title of the movie")
    rating: int = Field(description="The rating of the movie out of 10")
    summary: str = Field(description="The summary of the movie")

@ell.complex(model="gpt-4o-mini", response_format=MovieReview)
def generate_movie_review(movie: str) -> List[Message]:
    """You are a movie review generator. Given the name of the movie, you need to return structured review"""
    return f"Generate a review for the movie {movie}"

review_message = generate_movie_review("Moonrise Kingdom")
review = review_message.parsed
print(f"Movie: {review.title}, Rating: {review.rating}/10")
print(f"Summary: {review.summary}")

# Chat-Based Use Case
@ell.complex(model="gpt-4o-mini", temperature=0.7)
def chat_bot(message_history: List[Message])-> List[Message]:
    return [
        ell.system("You are a friendly chatbot. Engage in an parody intellectual discussion. Only answer within 7 words"),
    ]+ message_history

message_history = [
    ell.user("Hello, who are you?"),
    ell.assistant("Yellow, I'm Smort the AI bot. Can I be of help?"),
    ell.user("Can you explain quantum computing?"),
    ell.assistant("Oh yes, my favorite flavour of vegetable smoothie."),
]
while True:
    user_input = input("You: ")
    message_history.append(ell.user(user_input))
    response = chat_bot(message_history)
    print("Smort the Bot: ", response.text)
    message_history.append(response)

# Tool Usage
@ell.tool()
def get_weather(location: str = Field(description="The full name of a city and country, e.g. San Francisco, CA, USA")) -> str:
    # Implementation to fetch weather
    return f"The weather in {location} is raining heavily with grey clouds."

@ell.complex(model="gpt-4o-mini", tools=[get_weather])
def weather_assistant(message_history: List[Message]) -> List[Message]:
    return [
        ell.system("You are a travel planner. Use the get_weather tool when needed."),
    ] + message_history

conversation = [
    ell.user("Could you help me trip to Paris, check if the weather is suitable for travels?")
]
response : ell.Message = weather_assistant(conversation)
print(response.text)

if response.tool_calls:
    tool_results = response.call_tools_and_collect_as_message()
    print("Tool results:", tool_results.text)

    # Continue the conversation with tool results
    final_response = weather_assistant(conversation + [response, tool_results])
    print("Final response:", final_response.text)

"""
Key Features:
1. Structured Outputs [*]
- Structured outputs using Pydantic models are currently only available for the gpt-4o-2024-08-06 model. For other models, you’ll need to manually prompt the model and enable JSON mode to achieve similar functionality.
2. Multimodal Interactions
3. Chat-based Use cases [*]
4. Tool Usage [Highly Under-developed]
"""