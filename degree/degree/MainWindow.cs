using System;
using Gtk;
using System.Text;

public partial class MainWindow : Gtk.Window
{
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
        //°F = °C × 1,8 + 32
        float far = float.Parse(entry1.Text) * 1.8f + 32f;
        label4.Text = string.Format("{0}",far);
    }

    protected void OnEntry2Changed(object sender, EventArgs e)
    {
        //°C = (°F – 32) / 1,8
        float cel = (float.Parse(entry1.Text) - 32f) / 1.8f;
        label3.Text = string.Format("{0}", cel);
    }
}
