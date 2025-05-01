from mrjob.job import MRJob

class WordFrequencyCounter(MRJob):

    def mapper(self, _, line):
        """Splits lines into words and emits (word, 1)"""
        for word in line.split():
            yield word.lower(), 1  # Convert to lowercase for uniformity

    def reducer(self, word, counts):
        """Sums up counts for each word"""
        yield word, sum(counts)

if __name__ == "__main__":
    # Running the MRJob using command-line emulation in Jupyter
    import sys
    sys.argv.append("input.txt")  # Specify the input file
    WordFrequencyCounter.run()
