
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace test
{
    public class Program
    {
        
        static double Calculate(int r, int h){
            return r * r * Math.PI * h / 3;
        }

        
        public static void Main(string[] args)
        {
        	int r,h;
            while(true){

                Console.WriteLine("Radius: ");
                string input =  Console.ReadLine();
                if (input.ToLower().Contains('y')){
                	break;
                }else{
                	r = int.Parse(input);
                }
                Console.WriteLine("Height: ");
                input =  Console.ReadLine();
                if (input.ToLower().Contains('y')){
                	break;
                }else{
                	h = int.Parse(input);
                }
                double res = Calculate(r,h);
                Console.WriteLine("Result: "+res.ToString());
            }
        }
    }
}