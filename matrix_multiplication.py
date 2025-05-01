from mrjob.job import MRJob

class MatrixMultiplication(MRJob):

    def mapper(self, _, line):
        # Parse the input (Matrix, Row, Column, Value)
        matrix, i, j, value = line.split()
        i, j, value = int(i), int(j), int(value)

        # Matrix dimensions (assumed known, change as needed)
        num_rows_A = 2  # Rows in A
        num_cols_B = 2  # Columns in B

        if matrix == "A":
            for k in range(num_cols_B):  
                yield (i, k), ("A", j, value)
        
        elif matrix == "B":
            for k in range(num_rows_A):  
                yield (k, j), ("B", i, value)

    def reducer(self, key, values):
        from collections import defaultdict

        A_values = defaultdict(int)
        B_values = defaultdict(int)

        for mat, index, value in values:
            if mat == "A":
                A_values[index] = value
            else:
                B_values[index] = value

        # Compute dot product
        result = sum(A_values[k] * B_values[k] for k in A_values if k in B_values)

        yield key, result

if __name__ == "__main__":
    MatrixMultiplication.run()
