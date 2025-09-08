import ollama


def write_essay(prompt):
    prompt = ""+prompt
    response = ollama.chat(model='gemma3:1b', messages=[
        {
            'role': 'user',
            'content': prompt
        },
    ])
    
    return response['message']['content']