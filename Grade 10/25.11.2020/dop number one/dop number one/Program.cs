
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dop_number_one
{
    class Program
    {
        public static string convertOctToBin(string s) 
        {
            string result = "";
            while (s.Length > 0) 
            {
                switch (s[0]) 
                {
                    case '0':
                        result += "000";
                        break;
                    case '1':
                        result += "001";
                        break;
                    case '2':
                        result += "010";
                        break;
                    case '3':
                        result += "011";
                        break;
                    case '4':
                        result += "100";
                        break;
                    case '5':
                        result += "101";
                        break;
                    case '6':
                        result += "110";
                        break;
                    case '7':
                        result += "111";
                        break;
                }
                s = s.Substring(0, s.Length - 1);
            }
            for (int i = 0; s[0] == '0';i++) 
            {
                s = s.Substring(1, s.Length);
            }
            return result;
        }
        static void Main(string[] args)
        {
            string s = Console.ReadLine();
            Console.WriteLine(convertOctToBin(s));
            Console.ReadKey();
        }
    }
}
