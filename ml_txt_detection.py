from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import requests
from PIL import Image

def detect(file):
    processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
    model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

    url = "https://d2gi74td4gf3sj.cloudfront.net/games/7b70ace6-bd74-4abf-b710-98978d2560f9/assets/title_image/a01-122-02.jpg"
    image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

    pixel_values = processor(image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)

    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print(generated_text)
    
    return generated_text