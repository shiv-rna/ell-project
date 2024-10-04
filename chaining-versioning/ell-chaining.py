import ell
from typing import List

ell.init(verbose=True)

@ell.simple(model="gpt-4o", temperature=1.0)
def generate_podcast_ideas(about : str):
    """You are an expert podcast episode idea generator. Only with the title of podcast and one single line description"""
    return f"Generate a podcast episode idea about {about}"

@ell.simple(model="gpt-4o", temperature=1.0)
def write_a_draft_of_a_podcast(idea : str):
    """You are an adept podcast draft writer. You are well known for giving out provocative, relatable & engaging podcast drafts based on idea given to you. The draft should only consists of 3 paragraphs."""
    return f"Write a podcast draft about {idea}"

@ell.simple(model="gpt-4o", temperature=0.1)
def choose_best_draft(drafts : List[str]):
    """You are an expert podcast editor."""
    return f"Choose the best podcast draft from the following list based on how innovative, engaging and accurately relatable it is to the audience: {'\n'.join(drafts)}."

@ell.simple(model="gpt-4o", temperature=0.2)
def write_a_really_good_podcast_transcript


