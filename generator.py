import logging
from transformers import pipeline, set_seed

logging.getLogger('transformers').setLevel(logging.ERROR)

generator = pipeline('text-generation', model='gpt2')
set_seed(42)


def generate_sequence(input_str: str, temperature: float) -> str:
    response = generator(
        input_str,
        max_length=len(input_str.split(' ')) + 30,
        num_return_sequences=1,
        do_sample=True,
        return_full_text=False,
        temperature=temperature
    )

    return response[0]['generated_text']
