using System;

namespace _11._11._2020
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = int.Parse(Console.ReadLine());
            int y = int.Parse(Console.ReadLine());
            if (x%2 == y%2)
            {
                Console.WriteLine("ДА");
            }
            else
            {
                Console.WriteLine("Нет");
            }
        }
    }
}