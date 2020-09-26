using System;
using HtmlAgilityPack;

namespace redConnector {
    internal class Program {
        public static void Main()
        {
            // calling method
            ExtractHref("https://np.reddit.com/r/scandinavia/");
        }

        static void ExtractHref(string URL)
        {
            // declaring & loading dom
            HtmlWeb web = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc = web.Load(URL);
            
            // extracting all posts 
            // id="siteTable" contains all posts on one site
            foreach (HtmlNode link in doc.DocumentNode.SelectNodes("//id/siteTable"))
            {
                Console.WriteLine(link.InnerHtml);
            }
        }
    }
}