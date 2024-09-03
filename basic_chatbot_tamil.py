from transformers import pipeline, Conversation
from googletrans import Translator

# Load the pre-trained model for conversational tasks
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Initialize the translator
translator = Translator()

def chat_with_bot():
    print("Chatbot: Hello! I'm your friendly chatbot. Ask me anything!")

    # Create a conversation object to maintain context
    conversation = Conversation()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: போய்விடுங்கள்! நல்ல நாளாக வாழ்க!")
            break

        # Append user input to the conversation
        conversation.add_user_input(user_input)

        # Generate a response
        response = chatbot(conversation)

        # Translate the response to Tamil
        tamil_response = translator.translate(response.generated_responses[-1], dest='ta').text

        # Print the chatbot's response in Tamil
        print("Chatbot:", tamil_response)

# Run the chatbot
chat_with_bot()
