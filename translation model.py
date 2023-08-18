# -*- coding: utf-8 -*-


"""

!pip install transformers
!pip install gradio

# Import necessary libraries
from transformers import pipeline

# Initialize a translation pipeline
translator = pipeline("translation_en_to_de", model="t5-base")

# Translate English text to German
translation = translator("I love programming")[0]['translation_text']
print(translation) # Output: Ich liebe Programmieren.

# Import necessary libraries
import gradio as gr
from transformers import pipeline

# Initialize a translation pipeline
translator = pipeline("translation_en_to_de", model="t5-base")

def translate(text):
    # Translate English text to German
    translation = translator(text)[0]['translation_text']
    return translation

iface = gr.Interface(fn=translate,
                     inputs=gr.inputs.Textbox(lines=2, placeholder='Text to translate...'),
                     outputs="text")

iface.launch()

