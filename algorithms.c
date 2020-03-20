#include "algorithms.h" 

void resetMatrix(int **matrix, int rows, int cols)
{
    int *rowsZero = malloc(rows * sizeof(int));
    int *colsZero = malloc(cols * sizeof(int));

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (matrix[i][j] == 0)
            {
                rowsZero[i] = 1;
                colsZero[j] = 1;
            }
        }
    }

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (rowsZero[i] == 1 || colsZero[j] == 1)
            {
                matrix[i][j] = 0;
            }
        }
    }

    free(rowsZero);
    free(colsZero);
}