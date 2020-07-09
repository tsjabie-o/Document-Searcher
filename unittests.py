"""
File for unittests
@author: Xavi Oorthuis
"""
import unittest
import docsearch
import nltk
import tfidf
import math

docfinder = tfidf.DocumentFinder(nltk.corpus.gutenberg)


class TestDocsearch(unittest.TestCase):

    def test_InitializeCorpus(self):
        self.assertEqual(docsearch.InitializeCorpus(
            "brown"), nltk.corpus.brown)
        self.assertEqual(docsearch.InitializeCorpus(
            "gutenberg"), nltk.corpus.gutenberg)
        self.assertEqual(docsearch.InitializeCorpus(
            "treebank"), nltk.corpus.treebank)
        self.assertNotEqual(docsearch.InitializeCorpus(
            "brown"), nltk.corpus.treebank)


class TestTFIDF(unittest.TestCase):

    def test_clean_tokens(self):
        # Normal case
        words = ["Dit", "IS", ",", "een", "test", "."]
        expected = ["dit", "is", "een", "test"]
        self.assertEqual(docfinder.clean_tokens(words), expected)

        # Just bad characters
        words = ["!", ",", "."]
        expected = []
        self.assertEqual(docfinder.clean_tokens(words), expected)

        # Bad characters with a word
        words = ["!dit", "is", "test,"]
        expected = ["!dit", "is", "test,"]
        self.assertEqual(docfinder.clean_tokens(words), expected)

    def test_tf(self):
        # Normal case
        term = "test"
        tokens = ["token1", "token2", "token3", "test"]
        expected = 0.25
        self.assertEqual(docfinder.tf(term, tokens), expected)

        # No matches
        tokens = ["token1", "token2", "token3", "token4"]
        expected = 0
        self.assertEqual(docfinder.tf(term, tokens), expected)

    def test_idf(self):
        # Word in every document
        term = "and"
        expected = 0
        self.assertEqual(docfinder.idf(term), expected)

        # Word in no document
        term = "hnfewruihewifgheri"
        expected = 0
        self.assertEqual(docfinder.idf(term), expected)

        # Normal case
        term = "something"
        self.assertTrue(docfinder.idf(term) <= 1 and docfinder.idf(term) >= 0)

    def test_search(self):
        # Check whether order is right
        term = ["emma"]
        self.assertEqual([doc for doc in docfinder.search(term)]
                         [0][0], "austen-emma.txt")

        # Check if k parameter works correctly
        self.assertEqual(len([doc for doc in docfinder.search(term, k=1)]), 1)


if __name__ == "__main__":
    unittest.main()
