blank = 15;
steps = 0;
iswin = 0;
ischeat = 0;
bg = 0;
window.onload = function(){
	getPuzzle();
	document.getElementById("start").onclick = function(){
		start();
		move();
	}
	document.getElementById("fix").onclick = function(){
		start();
		autofix();
	}
	document.getElementById("change").onclick = function(){
		start();
		autofix();
		change();
		start();
		autofix();
	}
}

function getPuzzle(){
	ul = document.getElementById("game");
	var node = document.createElement("ul");
	node.type = "ul";
	node.id = "ul";
	ul.appendChild(node);
	var num = 0;
    for (var i = 0; i < 4; i++) {
    	for(var j = 0; j < 4; j++){
            var li = document.getElementById("ul");
            var node = document.createElement("li");
            var xpos = (33.33 * (num % 4)) + '%';
			var ypos = (33.33 * Math.floor(num / 4)) + '%';
            node.type = "li";
            node.id = "" + num;
            node.name = "pice";
            node.value = num;
            num++;
            node.className = "pice";
            
            node.style.border = "solid 1px gray";
            if(num<16){
            	node.style.background ="url(penda.png)";
            	node.style.backgroundSize = "360px 360px";
            }
            else{
            	node.name = "blank";
            	node.className = "blank";
            	node.style.border = "solid 1px white";
            }
            node.style.backgroundPosition = xpos + '' + ypos;
            li.appendChild(node);
        }
    }

}

function start(){
	iswin = 0;
	steps = 0;
	ischeat = 0;
	document.getElementById("15").style.transform = "translate(" + -600 + "px," + 0 + "px)"; 
	document.getElementById("steps").textContent = steps;
	count = 99;
	while(count--){
		while(true){
			var randomNum1 = Math.floor(Math.random() * 16);
			ran1 = randomNum1;
			a = "" + ran1; 
			idnum = parseInt(a);
			if((idnum % 4 == 0 && (blank == idnum + 1 || blank == idnum + 4 || blank == idnum - 4))||(idnum % 4 == 3 && (blank == idnum -1||blank == idnum+4||blank == idnum - 4))||(idnum%4==1||idnum%4==2)&&(blank == idnum -1||blank == idnum+4||blank == idnum - 4||blank==idnum+1)){
				break;
			}
		}
		
		idstr = "" + idnum;
		x_right = document.getElementById(a).value % 4 ;
		x_to = blank % 4;
		y_right = parseInt(document.getElementById(a).value / 4);
		y_to = parseInt(blank / 4);
		if((idnum % 4 == 0 && (blank == idnum + 1 || blank == idnum + 4 || blank == idnum - 4))||(idnum % 4 == 3 && (blank == idnum -1||blank == idnum+4||blank == idnum - 4))||(idnum%4==1||idnum%4==2)&&(blank == idnum -1||blank == idnum+4||blank == idnum - 4||blank==idnum+1)){
			document.getElementById(idstr).style.transform = "translate(" + (x_to - x_right)*90 + "px," + (y_to - y_right)*90 + "px)"; 
			document.getElementById(a).id = "" + blank;
			blank = idnum;
		}
		
	}
	if(blank!=15){
		start();
	}
	
}

function move(){
	var x_right;
	var y_right;
	var x_now ;
	var y_now;
	if(iswin==0){
		for(var i=0;i<16;i++){
			document.getElementsByClassName("pice")[i].onclick = function(){
				idnum = parseInt(this.id);
				idstr = "" + idnum;
				x_right = this.value % 4 ;
				x_to = blank % 4;
				y_right = parseInt(this.value / 4);
				y_to = parseInt(blank / 4);
				if((idnum % 4 == 0 && (blank == idnum + 1 || blank == idnum + 4 || blank == idnum - 4))||(idnum % 4 == 3 && (blank == idnum -1||blank == idnum+4||blank == idnum - 4))||(idnum%4==1||idnum%4==2)&&(blank == idnum -1||blank == idnum+4||blank == idnum - 4||blank==idnum+1)){
					document.getElementById(idstr).style.transform = "translate(" + (x_to - x_right)*90 + "px," + (y_to - y_right)*90 + "px)"; 
					this.id = "" + blank;
					steps++;
					document.getElementById("steps").textContent = steps;
					blank = idnum;
				}
				check();
			}
			
		}
	}
}


function change(a){
	if(a=="0"){var b = 0;return b;}
	if(a=="1"){var b = 1;return b;}
	if(a=="2"){var b = 2;return b;}
	if(a=="3"){var b = 3;return b;}
	if(a=="4"){var b = 4;return b;}
	if(a=="5"){var b = 5;return b;}
	if(a=="6"){var b = 6;return b;}
	if(a=="7"){var b = 7;return b;}
	if(a=="8"){var b = 8;return b;}
	if(a=="9"){var b = 9;return b;}
	if(a=="10"){var b = 10;return b;}
	if(a=="11"){var b = 11;return b;}
	if(a=="12"){var b = 12;return b;}
	if(a=="13"){var b = 13;return b;}
	if(a=="14"){var b = 14;return b;}
	if(a=="15"){var b = 15;return b;}
}

function check(){
	flag = 1;
	for(j=0;j<16;j++){
		var k;
		(function(a){
			if(document.getElementById(a).value!=a){
				flag = 0;
			}
		})(j);
		if(flag == 0){
			break;
		}
	}
	if(flag == 1){
		if(ischeat==1){
			setTimeout(function() {alert("Don't cheat!")}, 1000);
			
		}
		else{
			setTimeout(function() {alert("You win!" + "You have walked " + steps + " steps")}, 1000);
			iswin = 1;
			return 1;
		}
		
	}
	else{
		return 0;
	}
}

function autofix(){
	
	for(j=0;j<16;j++){
		(function(a){
				document.getElementById(a).style.transform = "translate(" + 0 + "px," + 0 + "px)"; 
		})(j);
	}
	
	for(j=0;j<16;j++){
		(function(a){
				document.getElementById(a).id = "c" + document.getElementById(a).value;
		})(j);
	}

	for(j=0;j<16;j++){
		(function(a){
			b = "c" + a;
				document.getElementById(b).id = "" + a;
		})(j);
	}
	document.getElementById("15").style.transform = "translate(" + -600 + "px," + 0 + "px)"; 


	blank = 15;
	iswin = 1;
	ischeat = 1;
}

function change(){
	if(bg == 0)
	{for(j=0;j<15;j++){
			(function(a){
					document.getElementById(a).style.backgroundImage ="url(2.jpg)";
			})(j);
		}
		document.getElementById("pic").style.backgroundImage = "url(2.jpg)";
		bg = 1;
	}
	else{
		for(j=0;j<15;j++){
			(function(a){
					document.getElementById(a).style.backgroundImage ="url(penda.png)";
			})(j);
		}
		document.getElementById("pic").style.backgroundImage = "url(penda.png)";
		bg = 0;
	}
}