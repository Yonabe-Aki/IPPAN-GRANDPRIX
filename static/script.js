function require_login(){
    alert("ログインしてください")
}

var speed;
var fadeOut;
var count;
var acceleration;

function test2(){
    speed = 1;
    acceleration = 1.2;
}

function fadeOut(){
    speed = speed * acceleration
    if (document.getElementById("flash-message") != null){
        var target = document.getElementById('flash-message');
        var cssStyleDeclaration = getComputedStyle(target, null ) ;
        var top = cssStyleDeclaration.getPropertyValue( "top" ) ;
        target.style.top = parseInt(top) - parseInt(speed) +"px";   
        if(parseInt(top) <= -300){
            clearInterval(timer1);
            target.remove();
        }
    }
}


timer1 = setInterval(fadeOut,50);

setTimeout(test2,3000);


