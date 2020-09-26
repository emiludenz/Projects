using System;
using System.Collections.Generic;

namespace MathParser {
    public class Token {
        public char Kind;
        public double Value;
        
        /// <summary>
        /// Reads a char and returns the corresponding token 
        /// </summary>
        /// <param name="x">The char to read</param>
        /// <returns>A Token</returns>
        public static Token ReadToken(char x) {
            Token retToken = new Token();
            switch (x) {
                case '+':
                case '-':
                case '*':
                case '/':
                case '^':
                    retToken.Kind = x;
                    break;
                default:
                    retToken.Kind = '8';
                    retToken.Value = double.Parse(x.ToString());
                    break;
                    
            }

            return retToken;
        }

        /// <summary>
        /// Read a string and returns a list of tokens
        /// </summary>
        /// <returns></returns>
        public static List<Token> ReadString(string stream) {
            List<Token> rTokens = new List<Token>();
            foreach (char c in stream) {
                Token t = Token.ReadToken(c);
                rTokens.Add(t);
            }
            return rTokens;
        }

        /// <summary>
        /// 
        /// </summary>
        /// <returns></returns>
        public override string ToString() {
            return (Kind =='8') 
                ? Value.ToString() 
                : Kind.ToString();
        }
    }
}