import requests

class ImageFromText:

    def __init__(self, deep_ai_key):
        self.DEEPAI_URL = "https://api.deepai.org/api/impressionism-painting-generator"
        self.DEEPAI_API_KEY = deep_ai_key

    def generate_image_from_text(self, prompt, done_file_path):

        negative_prompt = "bad anatomy, bad proportions, blurry, cloned face, cropped, deformed, dehydrated, disfigured, duplicate, error, extra arms, extra fingers, extra legs, extra limbs, fused fingers, gross proportions, jpeg artifacts, long neck, low quality, lowres, malformed limbs, missing arms, missing legs, morbid, mutated hands, mutation, mutilated, out of frame, poorly drawn face, poorly drawn hands, signature, text, too many fingers, ugly, username, watermark, worst quality."
        try:
            r = requests.post(
                self.DEEPAI_URL,
                data={
                    'text': prompt,
                    "negative_prompt": negative_prompt,
                    'grid_size': 1
                },
                headers={'Api-Key': self.DEEPAI_API_KEY}
            )
            download_url = r.json()["output_url"]
            self.__download_image(download_url, done_file_path)
            return done_file_path
        
        except Exception as e:
            print("Error creating image {}".format(str(e)))


    def __download_image(self, url, file_path):

        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return True
        else:
            return False