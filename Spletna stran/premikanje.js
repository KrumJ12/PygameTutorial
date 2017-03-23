function preveri(){
	for (var index in hashtable) {
		var p=hashtable[index];
	    if( p[0]==p[1]){
		document.getElementById(p[1]).className += " pravilnoMesto";
	} else {
		document.getElementById(p[1]).className += " napacnoMesto";
	};
	
	} 
}

function preveriZasedene(){
	zasedeni=[];
	for (var index in hashtable) {
		zasedeni.push(hashtable[index][0]);
	}
}



document.addEventListener("dragstart", function(event) {
    // The dataTransfer.setData() method sets the data type and the value of the dragged data
    event.dataTransfer.setData("Text", event.target.id);
	odhod=event.target.id;

});

/* Events fired on the drop target */

// By default, data/elements cannot be dropped in other elements. To allow a drop, we must prevent the default handling of the element
document.addEventListener("dragover", function(event) {
	q=zasedeni.indexOf(event.target.id);
    if (q < 0) {
	event.preventDefault();
	}
});


/* On drop - Prevent the browser default handling of the data (default is open as link on drop)
   Reset the color of the output text and DIV's border color
   Get the dragged data with the dataTransfer.getData() method
   The dragged data is the id of the dragged element ("drag1")
   Append the dragged element into the drop element
*/
document.addEventListener("drop", function(event) {
    event.preventDefault();
    q=zasedeni.indexOf(event.target.id);
    if ( event.target.className == "droptarget" && q < 0) {
        var data = event.dataTransfer.getData("Text");
        event.target.appendChild(document.getElementById(data));
	prihod=event.target.id;
	hashtable[odhod][0]=prihod;
	preveriZasedene();
    }
});

var q=1;
var zasedeni=[];
var prihod="";
var odhod="";
var hashtable={};

/* 
Za vsako sliko si zapomnimo par droptargetov (kjeJe,kjeBiMoralaBiti)
Na začetku ("prazno", idUstreznegaDroptargeta)
*/
hashtable["1"]=["prazno","d1"];
hashtable["2"]=["prazno","d2"];
hashtable["3"]=["prazno","d3"];
hashtable["4"]=["prazno","d4"];
hashtable["5"]=["prazno","d5"];
hashtable["6"]=["prazno","d6"];
hashtable["7"]=["prazno","d7"];
hashtable["8"]=["prazno","d8"];
hashtable["9"]=["prazno","d9"];
hashtable["10"]=["prazno","d10"];
hashtable["11"]=["prazno","d11"];
hashtable["12"]=["prazno","d12"];
hashtable["13"]=["prazno","d13"];


