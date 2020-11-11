using System;

namespace _11._11._2020
{
    class Program
    {
        static void Main(string[] args)
        {
            double x = double.Parse(Console.ReadLine());
            double y = double.Parse(Console.ReadLine());
            if ((x * x + y * y > 25) && (x < 5 && x > 0) && (y < 5 && y > 0))
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