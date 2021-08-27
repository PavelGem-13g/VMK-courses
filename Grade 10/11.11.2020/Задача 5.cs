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
            int x = int.Parse(Console.ReadLine());
            int y = int.Parse(Console.ReadLine());
            int z = int.Parse(Console.ReadLine());
            if (x<0 && y<0 && z<0)
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
