using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _11._11._2020
{
    class Program
    {
        static void Main(string[] args)
        {
            int k = int.Parse(Console.ReadLine());
            if (k.ToString()[0] == k.ToString()[1] && k.ToString()[0] == k.ToString()[3])
            {
                Console.WriteLine("Да");
            }
            else 
            {
                Console.WriteLine("Нет");
            }
        }
    }
}
