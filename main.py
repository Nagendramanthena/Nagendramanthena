print("hello")
from translate import Translator
greetings = ["hello","goodmorning","how are you"]
trans = Translator(to_lang="telugu")
for g in greetings:
    print(trans.translate(g));