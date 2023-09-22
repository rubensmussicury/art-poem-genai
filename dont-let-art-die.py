from classes.MaterializeText import MaterializeText
from classes.ImageFromText import ImageFromText
from classes.ImageDecorator import ImageDecorator

def runner():

    # What's the poem you want to materialize as an image?
    # In this example I'm using Sonnet 18 – by William Shakespeare
    my_poem = """
Shall I compare thee to a summer’s day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer’s lease hath all too short a date;
Sometime too hot the eye of heaven shines,
And often is his gold complexion dimm'd;
And every fair from fair sometime declines,
By chance or nature’s changing course untrimm'd;
But thy eternal summer shall not fade,
Nor lose possession of that fair thou ow’st;
Nor shall death brag thou wander’st in his shade,
When in eternal lines to time thou grow’st:
So long as men can breathe or eyes can see,
So long lives this, and this gives life to thee.
"""

    # For Open AI key – https://platform.openai.com/account/api-keys
    # A representation of the original poem as an image, will be returned by this method using ChatGPT.
    # E.g.:
    # An Impressionist art image from this text would capture fleeting moments 
    # of nature's beauty. Soft strokes of color convey changing seasons (...)
    chatgpt_key = "YOUR-OPENAI-KEY"
    materialize_text = MaterializeText(chatgpt_key)
    text_as_image_representation = materialize_text.materialize(my_poem)
    
    # For Deep AI Key - https://deepai.org/
    # Use it to generate an impressionist image style from above text using ChatGPT.
    deepai_key = "YOUR-DEEPAI-KEY"
    image_from_text = ImageFromText(deepai_key)
    gen_img_name = "generated/poem_img_representation_sonnet18.jpeg"
    image_from_text.generate_image_from_text(
        text_as_image_representation, 
        gen_img_name
    )

    # In this step, the Author is placed at the bottom of the image, and the Poem Title is positioned in the center.
    dec_img_name = "generated/decorated_image_sonnet18.jpeg"
    image_decorator = ImageDecorator()
    image_decorator.decorate_image(input_img=gen_img_name, 
                                   output_img=dec_img_name,
                                   text_bottom="William Shakespeare",
                                   text_center="Sonnet 18")


if __name__ == "__main__":
    runner()