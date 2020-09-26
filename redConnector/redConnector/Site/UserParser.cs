using System.Collections.Generic;
using redConnector.UserClass;

namespace redConnector.Site {
    public class UserParser {
        public string Url;
        public List<Comment> Comments;
        public UserParser(string url) {
            Url = url;
            Comments = new List<Comment>();
        }
    }
}