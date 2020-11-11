using System;

namespace _11._11._2020
{
    class Program
    {
        static void Main(string[] args)
        {
            double x = double.Parse(Console.ReadLine());
            double y = double.Parse(Console.ReadLine());
            if (Math.Cos(x) <0.5 && Math.Cos(x) > 0f)
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