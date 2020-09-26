open System
(* This is a multi-line comment *)
// This is a single-line comment

let sign num =
   if num > 0 then "positive"
   elif num < 0 then "negative"
   else "zero"

let abs num =
  if num > 0 then num * 1
  elif num < 0 then num * -1
  else 0

let main() =
   Console.WriteLine("abs 5: {0}", (abs 5))
   Console.WriteLine("abs -5: {0}", (abs -5))

main()