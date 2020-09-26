using System;

namespace MathParser {
    public class TokenParser {


        public static void ParseTokens() {
            string input = "";
            while (input != "q") {
                input = Console.ReadLine();
                if (String.IsNullOrEmpty(input) || input == "q") { continue;}

                var tmp = Token.ReadString(input);
                foreach (var token in tmp) {
                    Console.Write(token.ToString());
                }
                Console.WriteLine();
            }
        }
    }
}