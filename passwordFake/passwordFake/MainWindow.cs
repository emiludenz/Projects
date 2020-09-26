using System;
using Gtk;
using System.Linq;

public partial class MainWindow : Gtk.Window
{
    string secret = "kodeord";
    string secInput;
    public MainWindow() : base(Gtk.WindowType.Toplevel)
    {
        Build();
    }

    protected void OnDeleteEvent(object sender, DeleteEventArgs a)
    {
        Application.Quit();
        a.RetVal = true;
    }
    protected void OnEntry1Changed(object sender, EventArgs e)
    {
        if (entry1.Text.Length - 1 >= 0) { 
            secInput += entry1.Text[entry1.Text.Length-1];
            }
        entry1.Text = String.Concat(Enumerable.Repeat("*", entry1.Text.Length));
    }

    protected void OnButton1Clicked(object sender, EventArgs e)
    {
        secInput = secInput.Replace("*", "");
        if (secret == secInput)
        {
            label1.Text = "Enter!";
        }
        else
        {
            label1.Text = "Wrong";
        }

    }
}

