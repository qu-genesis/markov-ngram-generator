# import required modules
import nltk
import random

# installing corpus
corpus = nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())

# build the counter function for the nth gram #
def gram_counter(sentence, n, corpus):
    counter = {}
    if n == 1:
        for i in range(len(corpus)):
            if corpus[i] not in counter:
                counter[corpus[i]] = 1
            else:
                counter[corpus[i]] += 1
                pass
            pass
    else:
        for i in range(len(corpus) - n + 1):
            if sentence[-n + 1 :] == corpus[i : i + n - 1]:
                if corpus[i + n - 1] not in counter:
                    counter[corpus[i + n - 1]] = 1
                else:
                    counter[corpus[i + n - 1]] += 1
                    pass
                pass
    return counter


# in the case that there are unknown tokens, len(counter) == 0


# build the function that chooses the most probable word
def choose(counter, deterministic):
    if deterministic:
        choice = max(counter, key=counter.get)
    else:
        dist = [prob / sum(counter.values()) for prob in counter.values()]
        choice = random.choices(list(counter.keys()), dist)[0]
    return choice


# build the finish sentence algorithm
def finish_sentence(sentence, n, corpus, deterministic=False):
    # continue generating new words if the last word is not in .?!
    while (sentence[-1] not in [".", "?", "!"]) & (len(sentence) < 10):
        cur_counter = gram_counter(sentence, n, corpus)
        # reduce n if counter is empty
        if len(cur_counter) == 0:
            i = n
            while (i > 0) & (len(cur_counter) == 0):
                i -= 1
                cur_counter = gram_counter(sentence, i, corpus)
                pass
            pass
        token = choose(cur_counter, deterministic=deterministic)
        sentence.append(token)
    return sentence


if __name__ == "__main__":
    random.seed(1122)
    print(
        finish_sentence(["i", "have", "always", "been"], 4, corpus, deterministic=False)
    )
    print(
        finish_sentence(
            ["they", "were", "proud"],
            3,
            corpus,
            deterministic=True,
        )
    )
    random.seed(9999)
    print(
        finish_sentence(
            ["it", "was", "a", "bright", "cold", "day"], 5, corpus, deterministic=False
        )
    )
