print("hello")
from translate import Translator
greetings = ["hello","goodmorning"]
trans = Translator(to_lang="telugu")
for g in greetings:
    print(trans.translate(g));