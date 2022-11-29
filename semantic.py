import spacy

nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# series of words we want t compare with one another
tokens = nlp("ship package boat deliver car")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))



# comparing sentences
sentence_to_compare = "why is my cat on the car"

sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"
    ]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " ", similarity)
