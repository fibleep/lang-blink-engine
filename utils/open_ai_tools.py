import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPEN_AI_API_KEY")


def parse_to_blink(snippet:str)->str:
    """Parse a snippet to a blink"""
    PROMPT: str = """
    Create a 'blink' for the following html, a blink is basically a json with the following structure:
    {
        "title": "Title of the blink",
        "description": "Description of the blink",
        "code": "Example code for the description",
        "difficulty: "beginner | intermediate | advanced",
    }  
    A blink is a short snippet of code that explains a concept, it should be short and concise but also addicting.
    """ 
    
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=PROMPT + snippet,
            temperature=0.6,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"]
        )
        return response.choices[0].text
    except Exception as e:
        print(e)
        return None
    
if __name__ == "__main__":
    print(OPENAI_API_KEY)