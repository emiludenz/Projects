using System;

class Triangle{
	static public void Main(String[] args){
		int num = 3;
		//Console.WriteLine(args[0]);
		
		if (args.Length >= 1){
			try{
				num = Int16.Parse(args[0]);
				} 
			catch(System.FormatException){}
		}
		
		for(int i = 0; i < num;i++){
			Console.Write(@" /\ ");
		}
		Console.WriteLine();
		for(int i = 0; i < num;i++){
			Console.Write(@"/__\");
		}
		Console.WriteLine();
	}
}