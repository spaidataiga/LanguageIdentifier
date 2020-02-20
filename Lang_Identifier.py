import nltk

def biletter(words):
	"""Creates two-letter sequences within words. Used to create probability distribution
	for language models below"""
    bi_letters = []
    for word in words:
        if len(word) < 2:
            continue
        else:
            for i in range(len(word)-1):
                bi_letters.append( word[i] + word[i+1] )
    return bi_letters

def create_LM(path):
	"""Allows generation of other language models. Makes a probability distribution
	based on sequences of 2 letters in inputted corpus.
	Input parameter "path" should be the path to the input corpus
	Outputs a probability distribution for the language of that corpus. """ 
    f=open(path,encoding="utf-8")
    raw =f.read()
    words = nltk.word_tokenize(raw)
    words = nltk.Text(words)
    bis = biletter(words)
    bi_freq = nltk.ConditionalFreqDist((bigram[0].lower(), bigram[1].lower()) for bigram in bis)
    bi_probs = nltk.ConditionalProbDist(bi_freq, nltk.MLEProbDist)
    return bi_probs

def eng_or_es(word):
	"""Will determine if the probability of this word being English or Spanish is
	greater and will return the according value.

	This section requires some updating if more language models are introduced."""
    word = word.lower()
    en_prob = 1
    es_prob = 1
    for i in range(len(word)-1):
        en_prob *= en_probs[word[i]].prob(word[i+1])
        es_prob *= es_probs[word[i]].prob(word[i+1])
    if en_prob < es_prob:
        return "Spanish"
    elif es_prob < en_prob:
        return "English"
    else:
        return "Unidentified"

print("Welcome! Please wait while we load the language models.")

# To introduce other language models, create_LM with a path to a corpus in that language
es_probs = create_LM('textes.txt')
en_probs = create_LM('texten.txt')


# The input game.
print("To exit, write 'End'")
txt = ""
while (txt != "End"):
	txt = input("\n Please enter a word // Escribir una palabra \n>> ")
	if txt == "End":
		print("Goodbye!")
		break
	if (eng_or_es(txt) == "English"):
		print("That's an English word!")
	elif (eng_or_es(txt) == "Spanish"):
		print("¡Esa es una palabra española!")
	else:
		print("Sorry! We can't understand that word.")