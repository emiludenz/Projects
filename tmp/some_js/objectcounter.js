function spam(myobj){
	let count  	= 0;
	let numbers = 0;
	let att 	= 0;
	let high	= new Array();

	for (const elm in myobj){
		// number of objects
		att = att + 1;
		// count 
		if (typeof(myobj[elm]) == 'number'){
	    	count += myobj[elm];
	    	numbers += 1;
	    	high.push(myobj[elm])
		}
	}
	let h = high.sort(function(a,b){return b-a;}).slice(0,3)
	let median = count/numbers;
	return {Median:median, numAtt:att, highest:h};
}

let mobj = {name:"Emil", age:30, brothers:1, highest:35, lowest:4, mid:25, k:21, some_numbers:{a:100, b:90, c:7}};
let yobj = {name:"Jasmin", age:20, brothers:2, highest:50, lowest:2, mid:21, k:4, some_numbers:{a:100, b:90, c:7}}
console.log(spam(mobj))
console.log(spam(yobj))


	// highest 3
	/*
	let h = high.sort(
		function(a,b){
			if (a < b){return 1;} 
			else if (a==b){return 0;} 
			else {return -1;}
		}).slice(0,3)
	*/
	
	//let h = high.sort(function(a,b){return a-b;}).slice(high.length-3,high.length)