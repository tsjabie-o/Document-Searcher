# Document search

This program takes  terms and searches for the most relevant document in a corpus.

-----------

It uses three corpuses from the Natural Language Toolkit (NLTK) module for python.
The program uses an tf-idf algorithm to determine the most relevant document. All linguistic logic is done in *tfidf.py*.
It prints out a list of the most relevant documents along with their relevancy score. The user can specify a limit to the amount of documents shown and also which corpus to look for documents in. Applying the linguistic logic and also interaction with the user is done in *docsearch.py*.

It also uses the unittest module for python. All testing code can be found in *unittests.py*

-----------

Essentialy just Google