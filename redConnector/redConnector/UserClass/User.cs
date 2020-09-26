using System.Collections.Generic;

namespace redConnector.UserClass {
    public class User {
        public string UserName;
        public List<Comment> Comments;
        public List<SubReddits> ActiveInSubReddits;
        public List<SubReddits> ModInSubReddits;

        public User(string userName) {
            UserName = userName;
            Comments = new List<Comment>();
            ActiveInSubReddits = new List<SubReddits>();
            ModInSubReddits = new List<SubReddits>();
        }

        public void AddComment(Comment comment) {
            foreach (var c in Comments) { if (comment.Date == c.Date) { return; } }
            Comments.Add(comment);
        }
        
        
        
        
    }
}