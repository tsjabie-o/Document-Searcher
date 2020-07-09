"""
Docsearch module
@author: Xavi Oorthuis
@author: Sheetal Ramdas
"""

import argparse
import sys
import nltk
from tfidf import DocumentFinder


def InputHandler():
    """
    The function that handles commandline input. Uses argparser to specify and collect arguments. Returns the arguments.
    """
    parser = argparse.ArgumentParser(
        description="Retrieve relevant documents in a specified corpus for specified terms")
    parser.add_argument(
        '-c',
        type=str,
        help="The corpus to retrieve documents from",
        default="gutenberg",
        choices=["gutenberg", "brown", "treebank"]
    )
    parser.add_argument(
        '-k',
        type=int,
        help="The maximum amount of documents to show",
        default=None
    )
    parser.add_argument(
        "terms",
        type=str,
        nargs='+',
        help="The terms to retrieve relevant documents for"
    )

    args = parser.parse_args()
    corpus = args.c
    limit = args.k
    terms = args.terms

    return(corpus, limit, terms)


def InitializeCorpus(corpusname):
    """
    Function that returns the desired CorpusReader object.
    @param corpusname: (string) Name of the corpus to return CorpusReader object for.
    """
    # Kunnen eventueel nog andere corpora bij maar je hoeft er maar drie
    if corpusname == "gutenberg":
        return nltk.corpus.gutenberg
    elif corpusname == "brown":
        return nltk.corpus.brown
    else:
        return nltk.corpus.treebank


def Start():
    corpus, limit, terms = InputHandler()
    corpus_reader = InitializeCorpus(corpus)
    document_finder = DocumentFinder(corpus_reader)
    search_results = document_finder.search(terms, k=limit)
    result_with_postive_score = [
        result for result in search_results if result[1] > 0]
    if len(result_with_postive_score) == 0:
        print("No matches found")
    else:
        for result in result_with_postive_score:
            filename, score = result
            firstwords = " ".join(corpus_reader.words(filename)[:50])
            print("Filename: {}\nScore: {}\nFirst 50 words in document:\n\"{} ...\"\n".format(
                filename, score, firstwords))


if __name__ == "__main__":
    Start()
