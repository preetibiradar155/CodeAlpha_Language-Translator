from deep_translator import GoogleTranslator
import gradio as gr

def translate_text(text, dest):
    if not text.strip():
        return "Please enter text"
    return GoogleTranslator(source='auto', target=dest).translate(text)

langs = {
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

with gr.Blocks() as app:
    gr.Markdown("# 🌐 Language Translator - CodeAlpha Task 1")
    inp = gr.Textbox(label="Enter English Text", placeholder="Hello how are you")
    out = gr.Textbox(label="Translated Text")
    choice = gr.Dropdown(choices=list(langs.keys()), value="Hindi", label="Select Language")
    btn = gr.Button("Translate", variant="primary")
    btn.click(fn=lambda t,l: translate_text(t, langs[l]), inputs=[inp, choice], outputs=out)

app.launch()