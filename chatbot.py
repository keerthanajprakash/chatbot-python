import openai
import gradio as gr

# Set up your OpenAI API key
openai.api_key = ""

# Function to call the ChatGPT API
def chatbot(input_text):
    # Send the input to the ChatGPT API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful health chatbot. Provide general health advice based on user queries."},
            {"role": "user", "content": input_text}
        ]
    )
    # Extract the response text from the API response
    answer = response['choices'][0]['message']['content']
    return answer

# Gradio Interface
def gradio_interface(user_input):
    return chatbot(user_input)

# Creating a Gradio interface
iface = gr.Interface(
    fn=gradio_interface,
    inputs="text",
    outputs="text",
    title="Health Chatbot",
    description="Ask me anything about general health advice or symptoms. Note: This is for informational purposes only and not a substitute for professional medical advice."
)

# Launch the Gradio app
iface.launch()
