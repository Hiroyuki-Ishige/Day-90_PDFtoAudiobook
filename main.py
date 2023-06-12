from gtts import gTTS
from playsound import playsound
from PyPDF2 import PdfReader

# PDF to text -------------------------------------------------
#Open PDF file
# with open("Google_wiki.pdf", mode="r") as f:
#     pdfFileobj = f.read()

#Create a pdf reader object
pdfReader = PdfReader("Google_wiki.pdf")

#Print number of pages in the pdf file
print(f'Page Number: {len(pdfReader.pages)}')

#create a page object
pageObj = pdfReader.pages[0]

#extract text from page
text = pageObj.extract_text()

#display text
print(text)

# Text to Speech---------------------------------------
audio ="speech.mp3"
language ="en"

speech = gTTS(
                text=text,
                lang=language)

speech.save(audio)
playsound(audio)



