using System;
using Gtk;
using System.Globalization;
using System.Collections.Generic;
public partial class MainWindow : Gtk.Window
{
    public MainWindow() : base(Gtk.WindowType.Toplevel)
    {

#pragma warning disable RECS0021 // Warns about calls to virtual member functions occuring in the constructor
        Build();
#pragma warning restore RECS0021 // Warns about calls to virtual member functions occuring in the constructor
        getItems();
    }

    void getItems()
    {
        List<string> days = new List<string>(new string[]
            {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"});
        for (int i = 0; i < days.Count; i++){combobox1.InsertText(i, days[i]);}
    }

    protected void OnDeleteEvent(object sender, DeleteEventArgs a)
    {
        Application.Quit();
        a.RetVal = true;
    }

    protected void OnButton1Clicked(object sender, EventArgs e)
    {


        if (radiobutton1.Active) {
            TextInfo textInfo = new CultureInfo("en-US", false).TextInfo;
            label1.Text = textInfo.ToTitleCase(entry1.Text);
        }
        else if (radiobutton2.Active)
        {
            label1.Text = (entry1.Text).ToLower();
        }
        else if (radiobutton3.Active)
        {
            label1.Text = (entry1.Text).ToUpper();
        }


    }


    protected void OnCombobox1Changed(object sender, EventArgs e)
    {
        label4.Text = combobox1.ActiveText;
    }
}
