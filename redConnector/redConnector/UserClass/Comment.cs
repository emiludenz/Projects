using System;

namespace redConnector.UserClass {
    public class Comment {
        public string Text;
        public DateTime Date;
        public User User;
        public SubReddits Place;

        public Comment(string text, User user, DateTime dateTime, SubReddits place) {
            Text = text;
            User = user;
            Date = dateTime;
            Place = place;
        }
        
        
        public override string ToString() {
            return Text;
        }
        
        
    }
}