using System;
using Gtk;

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

    void calculate()
    {
        if (label1.Text != "0")
        {
            string[] exp = label1.Text.Split('+');
            label1.Text = (Int32.Parse(exp[0]) + Int32.Parse(exp[1])).ToString();
        }
        else
        {
            label1.Text = "0";
        }
    }
    protected void OnButtonEClicked(object sender, EventArgs e)
    {
        calculate();
    }

    protected void OnButtonClicked(object sender, EventArgs e)
    {
        if (label1.Text == "0")
        {
            label1.Text = "0";
        }
        else
        {
            label1.Text += "0";
        }
    }

    protected void OnButton1Clicked(object sender, EventArgs e)
    {
        if (label1.Text == "0")
        {
            label1.Text = "1";
        }
        else
        {
            label1.Text += "1";
        }
    }

    protected void OnButton2Clicked(object sender, EventArgs e)
    {
        if (label1.Text == "0")
        {
            label1.Text = "2";
        }
        else
        {
            label1.Text += "2";
        }
    }

    protected void OnButton3Clicked(object sender, EventArgs e)
    {
        if (label1.Text == "0")
        {
            label1.Text = "3";
        }
        else
        {
            label1.Text += "3";
        }
    }

    protected void OnButton4Clicked(object sender, EventArgs e)
    {
        if (label1.Text == "0")
        {
            label1.Text = "4";
        }
        else
        {
            label1.Text += "4";
        }
    }

    protected void OnButton5Clicked(object sender, EventArgs e)
    {
        if (label1.Text == "0")
        {
            label1.Text = "5";
        }
        else
        {
            label1.Text += "5";
        }
    }

    protected void OnButton6Clicked(object sender, EventArgs e)
    {
        if (label1.Text == "0")
        {
            label1.Text = "6";
        }
        else
        {
            label1.Text += "6";
        }
    }

    protected void OnButton7Clicked(object sender, EventArgs e)
    {
        if (label1.Text == "0")
        {
            label1.Text = "7";
        }
        else
        {
            label1.Text += "7";
        }
    }

    protected void OnButton8Clicked(object sender, EventArgs e)
    {
        if (label1.Text == "0")
        {
            label1.Text = "8";
        }
        else
        {
            label1.Text += "8";
        }
    }

    protected void OnButton9Clicked(object sender, EventArgs e)
    {
        if (label1.Text == "0")
        {
            label1.Text = "9";
        }
        else
        {
            label1.Text += "9";
        }
    }

    protected void OnButton10Clicked(object sender, EventArgs e)
    {
        if (label1.Text != "0")
        {
            label1.Text += "+";
        }
        else if (label1.Text.Contains("+"))
        {
            calculate();
            label1.Text += "+";
        }

    }

    protected void OnButton11Clicked(object sender, EventArgs e)
    {
        if (label1.Text != "0")
        { 
            label1.Text += "-"; 
        }
        else if (label1.Text.Contains("-"))
        {
            calculate();
            label1.Text += "-";
        }
    }

    protected void OnButton12Clicked(object sender, EventArgs e)
    {
        if (label1.Text != "0")
        {
            label1.Text += "*";
        }
        else if (label1.Text.Contains("*"))
        {
            calculate();
            label1.Text += "*";
        }
    }

    protected void OnButton13Clicked(object sender, EventArgs e)
    {
        if (label1.Text == "0")
        {
            label1.Text += ".";
        }
        else
        {
            label1.Text += ".";
        }
    }
}
