using System;

namespace teilbarkeitsregeln
{
    // ❌ "class Main()" is invalid syntax.
    // ✔ In C#, classes never have parentheses.
    // ✔ The class name does NOT need to match the namespace or file name.
    class Program
    {
        // ✔ This is the real entry point of the program.
        static void Main(string[] args)
        {
            int num;

            // ✔ Input loop
            while (true)
            {
                Console.Write("Which number to be tested? ");

                // ✔ TryParse is the cleanest way to validate numeric input
                if (int.TryParse(Console.ReadLine(), out num))
                    break;

                Console.WriteLine("\nEnter a natural number!\n");
            }

            // ❗ You always print "divided by 2" even for 3,4,5,... → fixed below
            Console.WriteLine("Is divided by 1 without remainder\n");

            Console.WriteLine(Divide_by_2(num)
                ? "Is divided by 2 without remainder\n"
                : "Is not divided by 2 without remainder\n");

            Console.WriteLine(Divide_by_3(num)
                ? "Is divided by 3 without remainder\n"
                : "Is not divided by 3 without remainder\n");

            Console.WriteLine(Divide_by_4(num)
                ? "Is divided by 4 without remainder\n"
                : "Is not divided by 4 without remainder\n");

            Console.WriteLine(Divide_by_5(num)
                ? "Is divided by 5 without remainder\n"
                : "Is not divided by 5 without remainder\n");

            Console.WriteLine(Divide_by_6(num)
                ? "Is divided by 6 without remainder\n"
                : "Is not divided by 6 without remainder\n");

            Console.WriteLine(Divide_by_7(num)
                ? "Is divided by 7 without remainder\n"
                : "Is not divided by 7 without remainder\n");

            Console.WriteLine(Divide_by_8(num)
                ? "Is divided by 8 without remainder\n"
                : "Is not divided by 8 without remainder\n");

            Console.WriteLine(Divide_by_9(num)
                ? "Is divided by 9 without remainder\n"
                : "Is not divided by 9 without remainder\n");
        }

        static bool Divide_by_2(int num)
        {
            // ✔ Only the last digit matters for divisibility by 2
            num %= 10;
            return (num % 2) == 0;
        }

        public static bool Divide_by_3(int num)
        {
            // ❌ Your original code had syntax errors and infinite loops.
            // ✔ This version follows the "sum of digits" rule correctly.

            int sum = 0;
            string s = num.ToString();

            foreach (char digit in s)
            {
                // ❗ (int)digit gives ASCII code, not numeric value
                // ✔ Correct conversion:
                sum += digit - '0';
            }

            return sum % 3 == 0;
        }

        public static bool Divide_by_4(int num)
        {
            // ✔ Only last two digits matter
            num %= 100;
            return (num % 4) == 0;
        }

        public static bool Divide_by_5(int num)
        {
            // ✔ Simple and correct
            return num % 10 == 0 || num % 10 == 5;
        }

        public static bool Divide_by_6(int num)
        {
            // ❌ You wrote divide_by_2 instead of Divide_by_2 → case sensitive
            // ✔ Divisible by 6 = divisible by 2 AND 3
            return Divide_by_2(num) && Divide_by_3(num);
        }

        public static bool Divide_by_7(int num)
        {
            // ✔ Your algorithm is correct (school rule)
            while (Math.Abs(num) > 7)
            {
                num = num / 10 - 2 * (num % 10);
            }
            return num == 0 || num == 7;
        }

        public static bool Divide_by_8(int num)
        {
            // ✔ Your school-rule version is fine
            return ((num % 1000) % 8) == 0;
        }

        public static bool Divide_by_9(int num)
        {
            // ✔ Same logic as Divide_by_3, but modulo 9
            int sum = 0;
            string s = num.ToString();

            foreach (char digit in s)
            {
                sum += digit - '0';
            }

            return sum % 9 == 0;
        }
    }
}
