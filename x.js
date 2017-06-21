try{var x = document.getElementById("demo").innerHTML;
document.getElementById("demo").style.visibility = "hidden";   
   }
catch(err)
{var a =err;
 
}  
if (typeof x != 'undefined')
{document.getElementById("t").innerHTML=x;
   }
