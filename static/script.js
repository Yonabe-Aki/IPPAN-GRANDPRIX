function show_modal_window(id){
    document.getElementById("modal_window"+String(id)).style.display="flex";
}
function close_modal_window(id){
    document.getElementById("modal_window"+String(id)).style.display="none";
}
function require_login(){
    alert("ログインしてください")
}