from pycocoevalcap.cider.cider import Cider
df_mode = 'corpus'
scorers = [
    (Cider(df_mode), "CIDEr"),
]

gts = {0: ['the man is playing a guitar', 'a man is playing a guitar'], 1: ['a woman is slicing cucumbers', 'the woman is slicing cucumbers', 'a woman is cutting cucumbers']}
res = {0: ['man is playing guitar'], 1: ['a woman is going out ']}

for scorer, method in scorers:
    score, scores = scorer.compute_score(gts, res)
    if type(method) == list:
        for sc, scs, m in zip(score, scores, method):
            print(sc, m)
    else:
        print(score, method)