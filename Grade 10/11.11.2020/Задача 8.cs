using System;

namespace _11._11._2020
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = int.Parse(Console.ReadLine());
            int y = int.Parse(Console.ReadLine());
            int z = int.Parse(Console.ReadLine());
            int k = 0;
            if (x == y)
            {
                k++;
            }
            if (y == z)
            {
                k++;
            }
            if (z == x)
            {
                k++;
            }
            if (k == 1)
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