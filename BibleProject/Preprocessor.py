
import re
import requests
import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from unidecode import unidecode
from dataclasses import dataclass
from typing import List, Type, Dict
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from wordcloud import WordCloud
from collections import Counter

nltk_pkgs = ["punkt", "stopwords"]

for pkg in nltk_pkgs:
    nltk.download(pkg)


@dataclass
class LenRange:
    min_len: int
    max_len: int

@dataclass
class PreprocessConfig:
    language: str
    stopwords: List[str]
    word_range: LenRange
    sent_range: LenRange
    patterns: List[re.Pattern]

class Step:
    def __init__(self, config: PreprocessConfig):
        self.config = config

    def forward(self, text:str) -> str:
        ...

class LowerStep(Step):
    def forward(self, text: str) -> str:
        return text.lower()

class WordTokenizeStep(Step):
    def forward(self, text: str) -> str:
        tokens = word_tokenize(text, language=self.config.language)
        return " ".join(tokens)

class UnidecodeStep(Step):
    def forward(self, text: str) -> str:
        return unidecode(text)

class StopwordsStep(Step):
    def forward(self, text: str) -> str:
        tokens = text.split(" ")
        filtered_tokens = filter(
            lambda token: token not in self.config.stopwords,
            tokens
            )
        return " ".join(filtered_tokens)

class LenFilterStep(Step):
    def forward(self, text: str) -> str:
        tokens = text.split(" ")
        filtered_tokens = filter(
            lambda token: (
                len(token) >= self.config.word_range.min_len and
                len(token) <= self.config.word_range.max_len
            ),
            tokens
        )
        return " ".join(filtered_tokens)

class RegexSubStep(Step):
    def forward(self, text: str) -> str:
        for pat in self.config.patterns:
            text = re.sub(pat, " ", text)
        return text

class StripStep(Step):
    def forward(self, text: str) -> str:
        return text.strip()

class SentLenStep(Step):
    def forward(self, text: str) -> str:
        tokens = text.split(" ")
        if (
            len(tokens) < self.config.sent_range.min_len or
            len(tokens) > self.config.sent_range.max_len
            ):
            text = ""
        return text

class Preprocessor:
    def __init__(
        self,
        steps: List[Type[Step]],
        config: PreprocessConfig
        ):
        self.steps = steps
        self.config = config

    def preprocess(self, text: str) -> str:
        for step_type in self.steps:
            step = step_type(self.config)
            text = step.forward(text)
        return text