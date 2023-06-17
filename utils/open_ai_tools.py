import openai
import os
from dotenv import load_dotenv
import tiktoken

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPEN_AI_API_KEY")


def truncate_text(long_text: str, max_tokens: int) -> str:
    """Truncate long text to a specified number of tokens"""
    tokenizer = tiktoken.get_encoding("p50k_base")  # Works with davinci
    tokens = tokenizer.encode(long_text)

    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]
        truncated_text = tokenizer.decode(tokens)
        return truncated_text
    else:
        return long_text


def parse_to_blink(snippet: str) -> str:
    """Parse a snippet to a blink"""
    PROMPT: str = """
    You speak only in json.
    Create a 'blink' for the following html, a blink is basically a json with the following structure:
    A blink is a short snippet of code that explains a concept, it should be short, concise and informative.
    {
        "title": "Title of the blink",
        "description": "Description of the blink",
        "code": "Example code for the description, if you cant think of anything or it doesnt make sense then leave this empty",
        "difficulty: "beginner | intermediate | advanced",
    }  Use the following html as a reference:
    """
    truncated_snippet = truncate_text(
        snippet, 1200
    )  # Allow some tokens for the completion

    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=PROMPT + truncated_snippet,
            temperature=0.3,
            max_tokens=600,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return response
    except Exception as e:
        print(e)
        return "Error"


if __name__ == "__main__":
    print(OPENAI_API_KEY)
