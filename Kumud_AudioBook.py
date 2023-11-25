#!/usr/bin/env python
# coding: utf-8

# # Create an Audiobook from a PDF
# ## This task tests your ability to apply Text to Speech conversion and Extraction of Text from PDF files in the creation of an audiobook from a PDF file

# ### Steps
# - Extract text from PDF file
# - Clean the text
# - Convert the text into speech
# - Save the speech
# - Play the speech

# ## 1. Extract text from PDF
# - Use PyPDF2

# ### Install the library

# In[1]:


get_ipython().system(' pip install PyPDF2')


# In[1]:


get_ipython().system('pip install pyttsx3')


# ### Import the library

# In[2]:


import PyPDF2
import pyttsx3


# ### Extract the text

# In[3]:


# Path to the PDF file
pdf_path = 'Jessie the rabbit Author.pdf'  # Replace with your PDF file path


# ### Print the extracted text

# In[4]:


# Initialize the extracted text
extracted_text = ''


# ## 2. Convert the Text into Speech
# 

# In[5]:


# Open the PDF file
with open(pdf_path, 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Read and concatenate the text from each page
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        if page.extract_text():
            extracted_text += page.extract_text() + "\n"
        else:
            # Handle pages where text extraction fails
            print(f"Text extraction failed for page: {page_num}")


# In[6]:


# Check if extracted_text is empty
if not extracted_text.strip():
    raise ValueError("No text extracted from the PDF. Check if the PDF contains extractable text.")

# Initialize pyttsx3 text-to-speech engine
tts_engine = pyttsx3.init()

# Optional: Set properties for the speech
tts_engine.setProperty('rate', 150)  # Speed of speech
tts_engine.setProperty('volume', 0.9)  # Volume

# Convert the text to speech and save it as an audio file
audio_path = 'output.mp3'   # Replace with your desired path
tts_engine.save_to_file(extracted_text, audio_path)

# Commit the changes and close the engine
tts_engine.runAndWait()


# ## 3. Convert the .mp3 file into .wave
# 

# ### Install the library

# In[7]:


get_ipython().system('pip install pydub')


# In[8]:


get_ipython().system('pip install ffprobe')


# In[9]:


get_ipython().system('pip install ffmpeg')


# ### Import the library

# In[10]:


engine = pyttsx3.init()


#  ### Convert the text into Wave

# In[12]:


from pydub import AudioSegment

# Convert the text
def convert_text_to_speech(text, output_path='output1.wav'):
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Save the speech
    engine.save_to_file(text, output_path)
    
    # Run the text-to-speech engine
    engine.runAndWait()


# ### Save the audio
# 

# In[13]:


output_file_path = 'Jessie the rabbit.wav'
convert_text_to_speech(extracted_text, output_path=output_file_path)

