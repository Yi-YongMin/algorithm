const ladder="|   |   |   |   |\n|   |   |   |   |\n|   |   |   |   |\n|   |   |   |   |\n|   |   |   |   |\n";
var ans=ladder;
const option=["   ","---","\\-\\","/-/"]
function reset(){
    ans=ladder;
}
function randomFill(){
    for(var i=0;i<5;i++){
        for(var j=0;j<4;j++){
            var plus=option[Math.floor(Math.random()*10)%4];
            //var first=ans.substring(4*j+18*i,4*j+18*i+1); 아....
            var first=ans.substring(0,4*j+18*i+1);
            var second=ans.substring(4*j+18*i+4);
            //console.log(plus);
            ans=first+plus+second;
            //console.log(ans);
            //console.log("j값은 : "+j+"\n"+"앞줄 : \n"+first+"\n");
            //console.log(second);
            //console.log(ans);
        }
    }
}
function analyze(){
    for(var i=0;i<5;i++){
        for(var j=0;j<3;j++) {
            var first=ans.substring(4*j+18*i+1,4*j+18*i+4);
            var second=ans.substring(4*j+18*i+5,4*j+18*i+8);
            if(first==="---"&&first===second) return false;
            else if(first==="\\-\\"&&second==="/-/") return false;
            else if(first==="/-/"&&second==="\\-\\") return false;
        }
    }
    return true;
}
function display(){
    console.log(ans)
}

reset();
randomFill();
display();
console.log(analyze())
