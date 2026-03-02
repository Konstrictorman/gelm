import re
import nltk
import pandas as pd
from unidecode import unidecode
from nltk.tokenize import WordPunctTokenizer

word_tokenizer = WordPunctTokenizer()

def preprocess(texto: str):
    texto = unidecode(texto)
    lower_text = texto.lower()
    tokens = word_tokenizer.tokenize(lower_text)
    tokenized_text = " ".join(tokens)
    punkt_removed_text = re.sub(r"[^a-z\s]", "", tokenized_text)
    no_dup_spaces_text = re.sub(r"\s+", " ", punkt_removed_text)
    return no_dup_spaces_text.strip()  #strip elimina espacios al comienzo y al final

def uniGrama(texto: str):
    _tokens = word_tokenizer.tokenize(texto)
    n_tokens = len(_tokens)
    print('n tokens: ', len(_tokens))
    vocab = set(_tokens)
    n_vocab = len(vocab)
    print('n vocab: ', n_vocab)
    print(_tokens[:1000])

    d_count = {word: 0 for word in vocab}
    for token in _tokens:
        d_count[token] += 1
    # print(d_count)
    d_probs = {token: count / n_tokens for token, count in d_count.items()}
    probs_series = pd.Series(d_probs)
    print(probs_series.sort_values(ascending=False).head(5))  # Imprime los 5 mayores
    print(probs_series.sort_values(ascending=False).tail(5))  # Imprime los 5 menores
    print(probs_series.idxmax())  # Imprime el mayor

    print(sum(d_probs.values()))  # Valida que la sumatoria de las probabilidades sea igual a 1

with open('Bible.txt', 'r', encoding='utf8') as f:
    try:
        corpus = f.read()
        clean_text = preprocess(corpus)
        uniGrama(clean_text)

    except Exception as e:
        print(e)

