using System;
using System.IO;
using System.Collections.Generic;
namespace them_racists
{
    public class users
    {
        List<string> uNames = new List<string>();
        public users()
        {
            string[] txt = File.ReadAllLines(@"users.txt");
            string name;
            for (int i=0;i < txt.Length; i++){
                name = txt[i].Substring(28);
                uNames.Add(name);
            }
        }
        List<string> GetUsers()
        {
            return uNames;
        }
    }
}
