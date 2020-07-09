
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:24:48 2020

@author: Marijke Prins
@author: Xavi Oorthuis
"""

import math


class DocumentFinder:

    def __init__(self, corpus):
        '''
        Creates an DocumentFinder object for a corpus.
        @param: corpus (CorpusReader) The corpus used to find the best document.
        '''
        self.corpus = corpus

    def clean_tokens(self, tokens):
        '''
        Removes the interpunction and makes the tokens lowercase.
        Return a list of tokens without interpunction and in lowercase.
        @param: tokens: (list) All the words in a document.
        '''
        badCharacters = ["!", "?", ",", ".", "\"", "(", ")", "<", ">"]
        cleaned_tokens = [word.lower()
                          for word in tokens if not word in badCharacters]
        return cleaned_tokens

    def tf(self, term, tokens):
        '''
        Determines the term frequency of a term given a list of tokens and returns it. 
        @param: term: (string) Term for which you determine the TF.
        @param: tokens (list) All the words in a document.
        '''
        t = 0
        for word in self.clean_tokens(tokens):
            if word.lower() == term.lower():
                t += 1
        N = len(tokens)
        tf = t/N
        return tf

    def idf(self, term):
        '''
        Determines the inverse document frequency based on the term, and returns it.
        @param: term: (string) Term for which you determine the IDF.
        '''
        documents = self.corpus.fileids()
        count_documents = len(documents)
        count_term = 0
        for d in documents:
            for w in self.corpus.words(d):
                if w.lower() == term.lower():
                    count_term += 1
                    break
        if count_term == 0:
            return 0
        else:
            idf = count_documents/count_term
            return math.log(idf)

    def search(self, terms, k=None, showscores=True):
        '''
        Searches through the corpus and returns the k most likely document(as a dictionary),
        based on the terms. 
        @param: terms: (list) The terms for which you what to find the best document.
        @param: k: (int) The amount of documents to be returned.
        @param: showscores: (boolean) Determines whether or not the scores are shown.
        '''
        result = dict()

        for t in terms:
            idf = self.idf(t)
            for d in self.corpus.fileids():
                x = self.tf(t, self.corpus.words(d)) * idf
                result[d] = x

        sorted_result = dict()
        teller = 0

        for w, v in sorted(result.items(), reverse=True, key=lambda x: x[1]):
            if k is None:
                sorted_result[w] = v
            elif teller < k:
                sorted_result[w] = v
                teller += 1
            else:
                break

        if showscores:
            return sorted_result.items()
        else:
            return sorted_result.keys()
