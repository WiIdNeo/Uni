using System;
using System.Collections.Generic;

namespace Lernprojekt
{
    class Program
    {
        static void Main(string[] args)
        {
            // Kommentiere aus, was du testen möchtest:

            //VariablenDemo();
            //FunktionenDemo();
            //ParameterDemo();
            //ParameterRefDemo();
            //KlassenDemo();
            //VererbungsDemo();
            //TypUmwandlungDemo();
            //StringDemo();
            //EinUndAusgabeDemo();
            //ForSchleifeDemo();
            //WhileSchleifeDemo();
            //DoWhileSchleifeDemo();
            //SwitchDemo();
            //TryCatchDemo();
            //TimeDemo();
            //RandomDemo();
            //ListeDemo();
        }

        // ---------------------------------------------------------
        // 2. Variablen
        // ---------------------------------------------------------
        static void VariablenDemo()
        {
            int ganzzahl = 10;
            double kommazahl = 3.14;
            bool istWahr = true;
            char buchstabe = 'A';
            string text = "Hallo";

            ganzzahl = ganzzahl + 5;

            Console.WriteLine("Ganzzahl: " + ganzzahl);
            Console.WriteLine("Kommazahl: " + kommazahl);
            Console.WriteLine("Ist wahr: " + istWahr);
            Console.WriteLine("Buchstabe: " + buchstabe);
            Console.WriteLine("Text: " + text);
        }

        // ---------------------------------------------------------
        // 3. Funktionen
        // ---------------------------------------------------------
        static void BegruesseBenutzer()
        {
            Console.WriteLine("Hallo, ich bin eine Funktion!");
        }

        static int Addiere(int a, int b)
        {
            return a + b;
        }

        static string ErzeugeBegrüßung(string name)
        {
            return $"Hallo {name}!";
        }

        static void FunktionenDemo()
        {
            BegruesseBenutzer();

            int ergebnis = Addiere(5, 7);
            Console.WriteLine("5 + 7 = " + ergebnis);

            string begruessung = ErzeugeBegrüßung("Colin");
            Console.WriteLine(begruessung);
        }

        // ---------------------------------------------------------
        // 4. Übergabeparameter
        // ---------------------------------------------------------
        static void ErhoeheUmEins(int zahl)
        {
            zahl = zahl + 1;
            Console.WriteLine("In der Funktion: " + zahl);
        }

        static void ParameterDemo()
        {
            int x = 10;
            ErhoeheUmEins(x);
            Console.WriteLine("Nach Funktionsaufruf: " + x);
        }

        static void ErhoeheUmEinsRef(ref int zahl)
        {
            zahl = zahl + 1;
        }

        static void ParameterRefDemo()
        {
            int x = 10;
            ErhoeheUmEinsRef(ref x);
            Console.WriteLine("Mit ref: " + x);
        }

        // ---------------------------------------------------------
        // 5. Klassen
        // ---------------------------------------------------------
        static void KlassenDemo()
        {
            Auto meinAuto = new Auto("BMW", 2015);
            meinAuto.Beschreibe();

            Auto deinAuto = new Auto("Audi", 2020);
            deinAuto.Beschreibe();
        }

        // ---------------------------------------------------------
        // 6. Vererbung
        // ---------------------------------------------------------
        static void VererbungsDemo()
        {
            Hund hund = new Hund("Bello");
            hund.Atmen();
            hund.Bellen();
        }

        // ---------------------------------------------------------
        // 7. Typumwandlung
        // ---------------------------------------------------------
        static void TypUmwandlungDemo()
        {
            int zahl = 42;
            double alsDouble = zahl;

            double pi = 3.14;
            int piAlsInt = (int)pi;

            string textZahl = "123";
            int parsedZahl = int.Parse(textZahl);

            string unsicher = "abc";
            bool erfolgreich = int.TryParse(unsicher, out int result);

            if (erfolgreich)
                Console.WriteLine("Umgewandelte Zahl: " + result);
            else
                Console.WriteLine("Konnte nicht in int umwandeln.");

            Console.WriteLine("alsDouble: " + alsDouble);
            Console.WriteLine("piAlsInt: " + piAlsInt);
            Console.WriteLine("parsedZahl: " + parsedZahl);
        }

        // ---------------------------------------------------------
        // 8. Strings
        // ---------------------------------------------------------
        static void StringDemo()
        {
            string name = "Colin";
            int alter = 30;

            string s1 = "Hallo " + name + ", du bist " + alter + " Jahre alt.";
            string s2 = $"Hallo {name}, du bist {alter} Jahre alt.";
            string s3 = string.Format("Hallo {0}, du bist {1} Jahre alt.", name, alter);

            Console.WriteLine(s1);
            Console.WriteLine(s2);
            Console.WriteLine(s3);
        }

        // ---------------------------------------------------------
        // 9. Ein- und Ausgabe
        // ---------------------------------------------------------
        static void EinUndAusgabeDemo()
        {
            Console.WriteLine("Wie heißt du?");
            string name = Console.ReadLine();

            Console.WriteLine($"Hallo {name}!");

            Console.WriteLine("Gib eine Zahl ein:");
            string eingabe = Console.ReadLine();

            bool ok = int.TryParse(eingabe, out int zahl);

            if (ok)
                Console.WriteLine($"Du hast {zahl} eingegeben.");
            else
                Console.WriteLine("Ungültige Zahl.");
        }

        // ---------------------------------------------------------
        // 10. Schleifen
        // ---------------------------------------------------------
        static void ForSchleifeDemo()
        {
            for (int i = 0; i < 5; i++)
                Console.WriteLine("Durchlauf: " + i);
        }

        static void WhileSchleifeDemo()
        {
            int count = 0;
            while (count < 5)
            {
                Console.WriteLine("Count: " + count);
                count++;
            }
        }

        static void DoWhileSchleifeDemo()
        {
            int zahl;
            do
            {
                Console.WriteLine("Gib eine Zahl > 10 ein:");
                int.TryParse(Console.ReadLine(), out zahl);
            } while (zahl <= 10);

            Console.WriteLine("Danke!");
        }

        // ---------------------------------------------------------
        // 11. Switch-Case
        // ---------------------------------------------------------
        static void SwitchDemo()
        {
            Console.WriteLine("Gib eine Note (1-5) ein:");
            int.TryParse(Console.ReadLine(), out int note);

            switch (note)
            {
                case 1: Console.WriteLine("Sehr gut"); break;
                case 2: Console.WriteLine("Gut"); break;
                case 3: Console.WriteLine("Befriedigend"); break;
                case 4: Console.WriteLine("Ausreichend"); break;
                case 5: Console.WriteLine("Mangelhaft"); break;
                default: Console.WriteLine("Ungültig"); break;
            }
        }

        // ---------------------------------------------------------
        // 12. Try-Catch
        // ---------------------------------------------------------
        static void TryCatchDemo()
        {
            Console.WriteLine("Gib eine Zahl ein:");
            string eingabe = Console.ReadLine();

            try
            {
                int zahl = int.Parse(eingabe);
                Console.WriteLine("Zahl * 2 = " + (zahl * 2));
            }
            catch (FormatException)
            {
                Console.WriteLine("Keine gültige Zahl.");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Fehler: " + ex.Message);
            }
            finally
            {
                Console.WriteLine("Fertig.");
            }
        }

        // ---------------------------------------------------------
        // 13. Zeit
        // ---------------------------------------------------------
        static void TimeDemo()
        {
            DateTime jetzt = DateTime.Now;
            Console.WriteLine("Jetzt: " + jetzt);

            DateTime heute = DateTime.Today;
            Console.WriteLine("Heute: " + heute.ToShortDateString());

            DateTime geburtstag = new DateTime(1990, 5, 20);
            TimeSpan diff = jetzt - geburtstag;

            Console.WriteLine("Tage seit Geburtstag: " + diff.Days);
        }

        // ---------------------------------------------------------
        // 14. Random
        // ---------------------------------------------------------
        static void RandomDemo()
        {
            Random random = new Random();

            int zufallInt = random.Next(0, 10);
            double zufallDouble = random.NextDouble();

            Console.WriteLine("Zufallszahl (0-9): " + zufallInt);
            Console.WriteLine("Zufallsdouble (0-1): " + zufallDouble);
        }

        // ---------------------------------------------------------
        // 15. Listen
        // ---------------------------------------------------------
        static void ListeDemo()
        {
            List<int> zahlen = new List<int>();
            zahlen.Add(1);
            zahlen.Add(2);
            zahlen.Add(3);

            foreach (int z in zahlen)
                Console.WriteLine("Listenelement: " + z);
        }
    }

    // ---------------------------------------------------------
    // Klassen für die Demos
    // ---------------------------------------------------------

    class Auto
    {
        public string Marke;
        public int Baujahr;

        public Auto(string marke, int baujahr)
        {
            Marke = marke;
            Baujahr = baujahr;
        }

        public void Beschreibe()
        {
            Console.WriteLine($"Auto: {Marke}, Baujahr {Baujahr}");
        }
    }

    class Tier
    {
        public string Name;

        public Tier(string name)
        {
            Name = name;
        }

        public void Atmen()
        {
            Console.WriteLine($"{Name} atmet.");
        }
    }

    class Hund : Tier
    {
        public Hund(string name) : base(name) { }

        public void Bellen()
        {
            Console.WriteLine($"{Name} bellt: Wuff!");
        }
    }
}