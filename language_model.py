from nltk import ngrams


class LM:
    def __init__(self, n):
        self.n = n

    def ingest(self, data):
        pass

    def get_prob(self, inpt):
        """

        Parameters
        ----------
        inptt: tuple
            Tuple should of length n where the first n-1
            items are y, with the nth item x, where
            p(x|y)

        Returns
        -------
        float
            n-gram probability.

        """
