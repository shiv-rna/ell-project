import ell
from typing import List

ell.init(verbose=True)


@ell.simple(model="gpt-4o-mini", temperature=1.0)
def generate_story_ideas(about : str):
    """You are an expert story ideator. Only answer in a single sentence."""
    return f"Generate a story idea about {about}."

@ell.simple(model="gpt-4o-mini", temperature=1.0)
def write_a_draft_of_a_story(idea : str):
    """You are an adept story writer. The story should only be 3 paragraphs."""
    return f"Write a story about {idea}."

@ell.simple(model="gpt-4o", temperature=0.1)
def choose_the_best_draft(drafts : List[str]):
    """You are an expert fiction editor."""
    return f"Choose the best draft from the following list: {'\n'.join(drafts)}."

@ell.simple(model="gpt-4-turbo", temperature=0.2)
def write_a_really_good_story(about : str):
    """You are an expert novelist that writes in the style of Hemmingway. You write in lowercase."""
    # Note: You can pass in api_params to control the language model call
    # in the case n = 4 tells OpenAI to generate a batch of 4 outputs.
    ideas = generate_story_ideas(about, api_params=(dict(n=4)))

    drafts = [write_a_draft_of_a_story(idea) for idea in ideas]

    best_draft = choose_the_best_draft(drafts)


    return f"Make a final revision of this story in your voice: {best_draft}."

story = write_a_really_good_story("a dog")

"""
This approach leverages test-time compute techniques, specifically Best-of-N (BoN) sampling. By generating multiple ideas and drafts, then selecting the best one, we increase the chances of producing a high-quality output. This strategy allows us to really leverage the most out of language models in several ways:

Diversity: By generating multiple ideas and drafts, we explore a broader space of possible outputs.

Quality Control: The selection step helps filter out lower-quality outputs.

Specialization: Each step is handled by a specialized LMP, allowing for more focused and effective prompts.

Iterative Improvement: The final revision step allows for further refinement of the chosen draft.

This compositional approach to prompt engineering enables us to break down complex tasks into smaller, more manageable steps. It also allows us to apply different strategies (like varying temperature or using different models) at each stage of the process, giving us fine-grained control over the output generation.
"""


"""
Observation:

 when draft is selected by the choose_the_best_draft  and it's output is passed on to the write write_a_really_good_story . It doesn't really pass the content of the best draft only the review of it .
 
"""