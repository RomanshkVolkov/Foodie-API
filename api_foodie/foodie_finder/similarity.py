from .utils import preprocess, format


def jaccard_similarity(s1, s2, n=3):
    s1_ngrams = set([s1[i:i+n] for i in range(len(s1)-n+1)])
    s2_ngrams = set([s2[i:i+n] for i in range(len(s2)-n+1)])

    intersection = s1_ngrams.intersection(s2_ngrams)
    union = s1_ngrams.union(s2_ngrams)

    return len(intersection) / len(union)


def find_closest_title(search_text, titles):
    closest_title = None
    highest_similarity = float("-inf")
    n_gram_size = len(search_text.split())

    for title in titles:
        curr_similarity = jaccard_similarity(preprocess(
            search_text), preprocess(title), n_gram_size)

        if curr_similarity > highest_similarity:
            highest_similarity = curr_similarity
            closest_title = title
            print(closest_title + " similarity: " + str(highest_similarity))

    print(closest_title)
    return closest_title
