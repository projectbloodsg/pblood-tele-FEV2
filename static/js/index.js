
function start_editing(elem,count){
  edit = "edit-" + count;
  console.log(edit)
  paragraph = document.getElementById(edit);
  paragraph.parentNode.style.pointerEvents = "none";
  paragraph.contentEditable = true;
  paragraph.style.backgroundColor = "#dddbdb";
}

function end_editing(elem,count){
  edit = "edit-" + count;
  console.log(edit)
  paragraph = document.getElementById(edit);
  paragraph.parentNode.style.pointerEvents = "";
  paragraph.contentEditable = false;
  paragraph.style.backgroundColor = "#ffe44d";
}




