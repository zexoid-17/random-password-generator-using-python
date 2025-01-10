import random
import string
import gradio as gr

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return "Error: No character types selected. Please choose at least one character type."

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, password_length, use_uppercase, use_lowercase, use_digits, use_symbols):
    try:
        passwords = [
            generate_password(password_length, use_uppercase, use_lowercase, use_digits, use_symbols)
            for _ in range(num_passwords)
        ]
        return "\n".join(passwords)
    except Exception as e:
        return str(e)

# Gradio Interface
def gradio_interface(num_passwords, password_length, use_uppercase, use_lowercase, use_digits, use_symbols):
    return generate_multiple_passwords(
        num_passwords, password_length, use_uppercase, use_lowercase, use_digits, use_symbols
    )

iface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Number(label="Number of Passwords", value=1),
        gr.Number(label="Password Length", value=8),
        gr.Checkbox(label="Include Uppercase Letters", value=True),
        gr.Checkbox(label="Include Lowercase Letters", value=True),
        gr.Checkbox(label="Include Digits", value=True),
        gr.Checkbox(label="Include Symbols", value=False),
    ],
    outputs="text",
    title="Password Generator",
    description="Generate secure passwords with customizable options.",
)

if __name__ == "__main__":
    iface.launch()

