import os
import openai

class MaterializeText:

    def __init__(self, open_ai_key):
        os.environ["OPEN_AI_KEY"] = open_ai_key
        openai.api_key = os.getenv("OPEN_AI_KEY")


    def materialize(self, full_text, max_tokens=350):

        prompt = """
Rule1: Describe in MAXIMUM 350 chars how an impressionist art image would be from the {provided_text}

{provided_text}
{text}
    """
        prompt = prompt.replace("{text}", full_text)

        try:
            response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt,
                    temperature=0.3,
                    max_tokens=max_tokens,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                )
            response = response.choices[0].text
            return response
        except Exception as e:
            print("Error generating the text representation {}".format(str(e)))
