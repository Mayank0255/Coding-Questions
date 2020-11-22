function vowelsAndConsonants(s) {
    var i;
    for(i=0;i<s.length;i++){
        if(s.substring(i,i+1)=="a" || s.substring(i,i+1)=="e" || s.substring(i,i+1)=="i" || s.substring(i,i+1)=="o" || s.substring(i,i+1)=="u"){
            console.log(s.substring(i,i+1));
        }
    }
    for(i=0;i<s.length;i++){
        if(s.substring(i,i+1)!="a" && s.substring(i,i+1)!="e" && s.substring(i,i+1)!="i" && s.substring(i,i+1)!="o" && s.substring(i,i+1)!="u"){
            console.log(s.substring(i,i+1));
        }
    }

}
