from transformers import pipeline
import gradio as gr

from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

chatbot = pipeline("conversational", model="facebook/blenderbot-3B")


while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = chatbot(user_input)
    print("Bot:", response[0]['generated_text'])

# Define the chatbot function
def vanilla_chatbot(message, history):
    # The history from Gradio's ChatInterface is a list of lists: [[user_msg, bot_msg], ...]
    # Convert it to the format expected by the conversational pipeline
    conversation_history = []
    for human, assistant in history:
        conversation_history.append({"role": "user", "content": human})
        conversation_history.append({"role": "assistant", "content": assistant})
    conversation_history.append({"role": "user", "content": message})


    # Generate a response using the chatbot
    response = chatbot(conversation_history)
    # Extract the generated text from the response
    generated_text = response[-1]['content']

    # Return the user message and the generated response as a tuple for Gradio
    return generated_text

# Create a Gradio interface
demo_chatbot = gr.ChatInterface(
    vanilla_chatbot,
    title="Mashdemy Chatbot",
    description="Enter text to start chatting."
)

# Launch the demo
demo_chatbot.launch(share = True, debug=True)
