using System.Globalization;
using System.Runtime.CompilerServices;

namespace teilbarkeitsregeln
{
    class Teilbarkeitsregeln()
    {
        static void Main(string []args)
        {

            num = Console.ReadLine("Wich number to be tested? ");
            Console.WriteLine("Is divided by 1 without remainder");
            if (divide_by_2(num)) {Console.WriteLine("Is divided by 2 without remainder");}
            else {Console.WriteLine("Is not divided by 2 without remainder");}


        }

        bool divide_by_2(int num)
        {
            return (num%2)==0;
        }
    }    

}
