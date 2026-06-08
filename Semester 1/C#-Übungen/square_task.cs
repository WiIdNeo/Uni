using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int[,] pic =
        {
            {0,0,1,1,0,0},
            {0,1,1,1,1,0},
            {1,1,1,1,1,1},
            {1,1,1,1,1,1},
            {0,1,1,1,1,0},
            {0,0,1,1,0,0}
        };

        var counts = new Dictionary<int, int>();

        // Wir wollen 1x1, 2x2, 3x3, 4x4 prüfen
        for (int size = 1; size <= 4; size++)
        {
            counts[size] = CountSquares(pic, size);
        }

        foreach (var kv in counts)
        {
            Console.WriteLine($"{kv.Key}x{kv.Key}-Quadrate: {kv.Value}");
        }

        int total = 0;
        foreach (var kv in counts)
            total += kv.Value;

        Console.WriteLine($"Insgesamt: {total}");
    }

    // Prüft, wie viele NxN-Quadrate aus 1 bestehen
    static int CountSquares(int[,] pic, int n)
    {
        int rows = pic.GetLength(0);
        int cols = pic.GetLength(1);
        int count = 0;

        for (int i = 0; i <= rows - n; i++)
        {
            for (int j = 0; j <= cols - n; j++)
            {
                if (IsSquare(pic, i, j, n))
                    count++;
            }
        }

        return count;
    }

    // Prüft ein einzelnes NxN-Quadrat
    static bool IsSquare(int[,] pic, int startRow, int startCol, int n)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (pic[startRow + i, startCol + j] != 1)
                    return false;
            }
        }
        return true;
    }
}
