# Language Identifier
Fun nltk-based language identifier. Will probabilistically determine if an input word is English or Spanish. 
Could be updated with other language models if available corpus.

In order to run, testes.txt and texten.txt need to be downloaded (as they are the corpora the language models are based on)

To add in new language models, first obtain a corpus written in that language and use the function create_LM() to create another language model

The output of the function should be the model that returns the greatest probability for the input word.

Project based on work done in my Language Processing 2 class at The University of Copenhagen
English and Spanish corpora obtained from Project Gutenburg.
