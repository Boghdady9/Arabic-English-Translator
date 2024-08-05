from transformers import pipeline
import gradio as gr


# Load translation pipelines
translator_en_to_ar = pipeline("text2text-generation", model="BoghdadyJR/en-ar-model")
translator_ar_to_en = pipeline("text2text-generation", model="BoghdadyJR/ar-en-model")

def translate(text, direction):
    if direction == "en_to_ar":
        return translator_en_to_ar(text)[0]['generated_text']
    else:  # direction == "ar_to_en"
        return translator_ar_to_en(text)[0]['generated_text']


def translate_text(text, direction):
    return translate(text, direction)

# Define Gradio interface with a switch button
iface = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter text here..."),
        gr.Radio(choices=["en_to_ar", "ar_to_en"], label="Translation Direction", value="en_to_ar")
    ],
    outputs="text",
    title="Translation"
)

# Launch the interface
iface.launch()

