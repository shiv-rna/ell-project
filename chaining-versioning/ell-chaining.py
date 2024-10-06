import ell
from dotenv import load_dotenv
from typing import List
import random 

# Load environment variables from a .env file
load_dotenv()

ell.init(store='./logdir', autocommit=True, verbose=True)

topics = [
    "Digital Detox",
    "Mindful Productivity",
    "Emotional Intelligence",
    "Sleep Optimization",
    "Habit Formation",
    "Stress Management",
    "Cultivating Creativity"
]

"""
Role 1: Episode Concept Generator
Input: General topic or theme
Output: Specific episode concept

Role 2: Episode Outline Creator
Input: Episode concept
Output: A detailed episode outline

Role 3: Outline Evaluator and Selector
Input: List of episode outlines
Output: Best outline with evaluation report

Role 4: Script Writer
Input: Best episode outline
Output: List of full episode scripts

Role 5: Script Editor and Selector
Input: List of full episode scripts
Output: Best script with improvements

Role 6: Episode Description Writer
Input: Best full episode script
Output: Catchy episode description

Role 7: Cover Art Prompt Creator
Input: Episode concept and description
Output: Detailed image prompt for AI image generator

Role 8: Music Prompt Creator for Suno.ai
Input: Episode concept and description
Output: Opening and ending credit music prompts
"""

@ell.simple(model="gpt-4o", temperature=1.0)
def generate_episode_concept(topic : str):
    """You are an expert podcast concept creator. Generate engaging and insightful episode idea that align with the podcast's theme of science, psychology, sociology, mindfulness, current technology, and personal growth."""
    return f"Create a compelling episode concept for 'Neural Kaleidoscope' based on the theme: {topic}. The concept should be innovative and offer practical insights for personal development. Respond with a brief creative title and a one-sentence description."

@ell.simple(model="gpt-4o", temperature=1.0)
def generate_episode_outline(concept : str):
    """You are a skilled podcast content strategist. Create engaging and informative outlines for episodes based on science, psychology, sociology, mindfulness, technology, and personal growth."""
    return f"Develop a detailed outline card for the podcast'Neural Kaleidoscope' episode with the following concept: {concept}. An outline should include an introduction, 3-4 main brilliant thought-provocating talking bullet points, and a conclusion. Each point should offer practical advice or insights for listeners."
    
@ell.simple(model="gpt-4o", temperature=0.3)
def evaluate_episode_outline(outlines : List[str]):
    """You are an expert content evaluator specializing in podcast outlines. Assess outlines for novelty, innovativeness, uniqueness, accuracy of statistics, and relevance to current human behavior and interests."""
    return f"Evaluate each of these outlines for a 'Neural Kaleidoscope' episode from the following list: {'\nOUTLINE: \n'.join(outlines)}. Score each outline on a scale of 1-10 for novelty, innovativeness, uniqueness, accuracy, and relevance. Provide a single line justification for each score. Then, select the best outline based on your evaluation. Output should contain: full length of the BEST OUTLINE and it's scorecard"
    
@ell.simple(model="gpt-4o", temperature=1.0)
def generate_episode_script_draft(best_outline : str):
    """You are an expert podcast script writer specializing in though-provoking, philosophical, scientific-insights, psychology, sociology, mindfulness, technology, motivational and personal-growth content. Write engaging, conversational scripts that are both informative and inspiring with if needed then pinch of storytelling. Also devices unique parallels between our relationship with technology & current habits, while providing new eye-opening perspective"""
    return f"Write a full podcast script draft for the 'Neural Kaleidoscope' episode based on this outline: {best_outline}. Each script should be conversational between two persons, include metaphors or analogies to explain complex concepts, and provide actionable tips for listeners. Aim for a 10-15 minute episode length for each script."    

@ell.simple(model="gpt-4o", temperature=0.2)
def evaluate_episode_script_draft(script_drafts : List[str]):
    """You are an experienced podcast editor with a keen eye for engaging content. Your task is to analyze multiple scripts, identify the best parts, and select the most compelling script."""
    return f"Review these scripts for a 'Neural Kaleidoscope' episode: {'\nSCRIPT DRAFT\n'.join(script_drafts)}. Identify the strongest elements in each script. Then, select the best overall script and suggest any improvements or additions based on the strong points from other scripts. Output should contain in following sequence: full length BEST SCRIPT DRAFT, along with Review Notes, Improvements, Strong points from other scripts"
    
@ell.simple(model="gpt-4o", temperature=1.0)
def generate_episode_description(final_script : str):
    """You are a creative copywriter specializing in podcast marketing. Create catchy, engaging descriptions that entice listeners to tune in."""
    return f"Write an enticing episode description for 'Neural Kaleidoscope' based on this script: {script}. The description should be attention-grabbing, hint at the value listeners will gain, and include emojis for visual appeal. Limit the description to 3-4 sentences."
    
@ell.simple(model="gpt-4o", temperature=1.0)
def generate_episode_cover_art(concept: str):
    """You are a visionary artist specializing in creating prompts for AI image generators. Your task is to create mind-blowing, unique image prompts for podcast cover art that captures the essence of each episode."""
    return f"Create a detailed and creative image prompt for an AI image generator to produce cover art for this 'Neural Kaleidoscope' episode. Concept: {concept}. The image should be visually striking, relevant to the episode's theme, and suitable for a podcast episode cover. Include specific details about style, colors, elements, and composition."
    
@ell.simple(model="gpt-4o", temperature=1.0)
def generate_episode_theme_song(concept: str):
    """You are a music director specializing in creating song-prompts for AI music generators, specifically for podcast opening and ending credits. Create prompts that capture the essence of the episode while being suitable for background music"""
    return f"Create two distinct music prompts for Suno.ai for the 'Neural Kaleidoscope' episode based on the following concept: {concept} 1) An opening credit theme that sets the mood. 2) An ending credit theme that provides closure, bit of positivity, sort of enlightenment . Include specific musical elements like instruments, tempo, mood, and style. Avoid abstract descriptions; focus on concrete musical information."


@ell.simple(model="gpt-4o", temperature=0.5)
def generate_episode(topic : str):
    """You are an expert podcast script finalizer. Your task is to take the best script selected by the editor and incorporate their suggested improvements to create the final, polished script."""
    concept = generate_episode_concept(topic)
    outlines = generate_episode_outline(concept, api_params=(dict(n=3)))
    best_outline = evaluate_episode_outline(outlines)
    script_drafts = generate_episode_script_draft(best_outline, api_params=(dict(n=2)))
    script_draft_review = evaluate_episode_script_draft(script_drafts)
    return f"Compile the final script for the 'Neural Kaleidoscope' episode based on this best script draft and the editor's review: {script_draft_review}. Incorporate the suggested improvements and ensure the script flows seamlessly in entertaining & engaging manner."

 
episode = generate_episode(topics[2])
