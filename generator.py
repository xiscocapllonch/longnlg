import logging
from transformers import pipeline, set_seed

logging.getLogger('transformers').setLevel(logging.ERROR)

# Set device param if there are GPU
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


def get_next_input(outputs: list, max_input_size: int):
    return ' '.join(''.join(outputs).split()[-max_input_size:])


def generate_text(
        input_str: str, sequences_nbr: int,
        max_input_size: int = 50, temperature: float = 1.0
) -> list:
    outputs = []

    for s in range(sequences_nbr):
        next_input = get_next_input(outputs or [input_str], max_input_size)
        output = generate_sequence(next_input, temperature)
        outputs.append(output)

    return outputs
