import ell
from dotenv import load_dotenv
from typing import List
import random 

# Load environment variables from a .env file
load_dotenv()

ell.init(store='./logdir', autocommit=True, verbose=True)

topics = [
"Cognitive Ergonomics",
"Time Perception Hacking",
"Digital Consciousness Transfer",
"Biomimicry for Personal Growth",
"Quantum Psychology",
"Neurodiversity as a Superpower",
"Sensory Augmentation",
"Memory Architectures",
"Chronobiology of Creativity",
"Algorithmic Living",
"Emotional Contagion in Digital Spaces",
"Cognitive Foraging",
"Metacognitive Mapping",
"Neuroplasticity Rituals",
"Psychotechnology",
"Manufactured Serendipity",
"Cognitive Bandwidth Optimization",
"Digital Telepathy Ethics",
"Mnemonic Architectures",
"Temporal Arbitrage",
"Synthetic Happiness Engineering",
"Attention Economics",
"Reality Tunneling",
"Cognitive Entropy",
"Networked Intelligence",
"Empathy Amplification",
"Decision Fatigue Immunization",
"Cognitive Antifragility",
"Information Metabolism",
"Perception Augmentation",
"Mind-Machine Symbiosis",
"Digital Immortality Dilemmas",
"Biorhythmic Optimization",
"Cognitive Load Balancing",
"Consciousness Bandwidth",
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
    """You are an expert podcast concept creator for 'Neural Kaleidoscope', a show exploring the intersections of science, psychology, sociology, mindfulness, current technology, and personal growth. Generate engaging and thought-provoking episode ideas that challenge listeners' perspectives and offer practical insights for personal development. The podcast format features two hosts engaging in insightful dialogue, without guest interviews."""
    return f"""Create a compelling episode concept for 'Neural Kaleidoscope' based on the theme: {topic}. The concept should be innovative, slightly provocative, and offer practical insights for personal growth. Respond using the following format: 
        Title: [A creative, attention-grabbing title], 
        Description: [A single sentence that encapsulates the episode's core idea and its potential impact on listeners' lives]"""

@ell.simple(model="gpt-4o", temperature=1.0)
def generate_episode_outline(concept : str):
    """You are a podcast content strategist specializing in concise, thought-provoking content. Your task isto brainstorm research ideas and distill complex topics into sharp, engaging bullet points for the podcast'Neural Kaleidoscope', focusing on science, psychology, sociology, mindfulness, technology, and personalgrowth. Your work becomes the basis on which script is drafted"""
    return f"""Given the concept: {concept}, create a flash card-style outline for a short (< 15 min) 'NeuralKaleidoscope' episode.
       Rewrite the title and description in a single line, making it more compelling if needed.
       Generate exactly 5 bullet points that are:
       Highly thought-provoking
       Perspective-changing
       Concise yet impactful
       Based on research or established theories (no expert interviews)
       Practical or insightful for listeners
       Mind-bending analogies & interesting parallels drawn
    Exclude introductions, conclusions, and time allocations. Focus solely on the core ideas that will drive the episode's content."""
    
@ell.simple(model="gpt-4o", temperature=0.3)
def evaluate_episode_outline(outlines : List[str]):
    """You are an expert content evaluator specializing in podcast outlines. Assess outlines for their potential to engage and inform listeners of 'Neural Kaleidoscope', a podcast focusing on science, psychology, sociology, mindfulness, technology, and personal growth."""
    return f"""Evaluate each of these outlines for a 'Neural Kaleidoscope' episode: {'\nOUTLINE: \n'.join(outlines)}
    Score each outline on a scale of 1-10 for the following criteria:
        Thought-provoking nature
        Practical value for listeners
        Scientific grounding
        Originality of perspective
        Potential for listener engagement
    Select the best outline based on your evaluation.
    Output Format:
        BEST OUTLINE: [Full text of the highest-scoring outline]
        SCORES:
        Thought-provoking nature: [Score]
        Practical value for listeners: [Score]
        Scientific grounding: [Score]
        Originality of perspective: [Score]
        Potential for listener engagement: [Score]
        TOTAL SCORE: [Sum of all scores]
        OTHER OUTLINES:
        [One-line reason for not selecting each other outline]"""
    
@ell.simple(model="gpt-4o", temperature=1.0)
def generate_episode_script_draft(best_outline : str):
    """You are an expert podcast script writer specializing in thought-provoking, philosophical, scientific-insights, psychology, sociology, mindfulness, technology, motivational and personal-growth content. Create engaging, article-style scripts that are both informative and inspiring, with a touch of storytelling when appropriate. Draw unique parallels between our relationship with technology and current habits, while providing new eye-opening perspectives. Use only factual information and real-world examples from verifiable sources."""
    return f"""Write a full podcast script draft for the 'Neural Kaleidoscope' episode based on this outline:
    {best_outline}
    Guidelines:
    Present the content in an article-style format, without host names or dialogue indicators.
    Use a sort of conversational tone that engages the listener directly.
    Incorporate metaphors or analogies to explain complex concepts, but ensure they are based on real-world phenomena or scientific principles.
    Provide actionable tips for listeners.
    Draw parallels between technology, human behavior, and personal growth.
    If using examples or case studies, only refer to well-known figures or documented research. Do not create fictional characters or scenarios.
    Aim for a 15-20 minute episode length (approximately 2000-2500 words).
    Do not include any audio cues, music breaks, or sound effect notes.
    Cite sources for any specific claims or statistics mentioned.
    Structure the script to flow naturally through the points in the outline, expanding on each with depth and insight.
    Output Format:
    [Title]
    [Full article-style script without any audio cues or host names]
    [List of sources cited]"""    

@ell.simple(model="gpt-4o", temperature=0.2)
def evaluate_episode_script_draft(script_drafts : List[str]):
    """You are an expert podcast script evaluator with extensive experience in content analysis and improvement. Your role is to critically analyze multiple script drafts, select the most effective one, and provide comprehensive feedback for enhancement. You have a deep understanding of what makes content engaging, informative, and impactful for listeners."""
    return f"""Thoroughly review these script drafts for the 'Neural Kaleidoscope' episode:
        {'\n=== SCRIPT DRAFT ===\n'.join(script_drafts)}
        Output Format:
        1. BEST SCRIPT
        [Provide an exact, unmodified copy of the best script]
        2. EVALUATION REPORT should not be more than 6 concise sentences.
        A. Review Notes
        
        B. Recommended Improvements
        Content Enhancements
        Specific suggestions for deepening insights
        Ideas for more engaging examples or metaphors
        Potential areas to expand upon
        Structure Refinements
        Flow improvements
        Pacing adjustments
        Transition enhancements

        C. Strong Elements from Other Scripts
        List compelling points, metaphors, or explanations from other drafts that could be incorporated
        Explain how these elements could be integrated into the best script

        D. Content Optimization
        Identify any low-value sections that could be removed or condensed
        Suggest replacements for removed content if necessary

        Guidelines:
        Maintain the original voice and style of the best script
        Focus on actionable, specific feedback
        Consider the target audience and episode goals when making suggestions
        Ensure all recommendations align with the 'Neural Kaleidoscope' podcast style"""
    
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
    """You are an expert podcast script finalizer. Your task is to take the best script selected by the editor and incorporate their suggested improvements to create the final, polished article style script."""
    concept = generate_episode_concept(topic)
    outlines = generate_episode_outline(concept, api_params=(dict(n=3)))
    best_outline = evaluate_episode_outline(outlines)
    script_drafts = generate_episode_script_draft(best_outline, api_params=(dict(n=2)))
    script_draft_review = evaluate_episode_script_draft(script_drafts)
    return f"Compile the final article for the 'Neural Kaleidoscope' episode based on this best script and the editor's review: {script_draft_review}. Incorporate the suggested improvements and ensure the script flows seamlessly in entertaining & engaging manner."
 
episode = generate_episode(topics[1])
