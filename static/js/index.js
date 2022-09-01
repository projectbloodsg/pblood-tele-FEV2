window.post = function(url, data) {
  return fetch(url, {method: "POST", headers: {'Content-Type': 'application/json'}, body: JSON.stringify(data)});
} //function to post 

function start_editing(elem,count){
  edit = "edit-" + count;
  paragraph = document.getElementById(edit);
  paragraph.parentNode.style.pointerEvents = "none";
  paragraph.contentEditable = true;
  paragraph.style.backgroundColor = "#dddbdb";
  end_editing_button_id = "end-editing-" + count;
  end_editing_button = document.getElementById(end_editing_button_id);
  end_editing_button.hidden = false;
}

function end_editing(elem,count,message_id){
  edit = "edit-" + count;
  paragraph = document.getElementById(edit);
  paragraph.parentNode.style.pointerEvents = "";
  paragraph.contentEditable = false;
  paragraph.style.backgroundColor = "#ffe44d";
  console.log(paragraph.textContent);
  path = "/" + message_id;
  post(path, {'type': 'edit_message', 'message': paragraph.textContent}); //posts edited message back to the python app
  end_editing_button_id = "end-editing-" + count;
  end_editing_button = document.getElementById(end_editing_button_id);
  end_editing_button.hidden = true;
}

function start_child_message(){
  message = document.getElementById('create-child-message');
  if (message.hidden == true){
    message.hidden = false;
  }
  else if (message.hidden == false){
    message.hidden = true;
  }
}

function submit_child_message(parent_id){
  message = document.getElementById('freeform');
  /*console.log(message.value)*/
  path = "/" + parent_id;
  console.log(path)
  console.log({'type': 'new_child_message', 'message': message.value, 'parent_id' : parent_id})
  post(path, {'type': 'new_child_message', 'message': message.value, 'parent_id' : parent_id}); //posts new child message back to the python app
  start_child_message()
}

function delete_message_confirm(count,message_id){
  col_wrapper_number = "col wrapper " + count;
  col_wrapper = document.getElementById(col_wrapper_number);
  path = "/" + message_id;
  if (confirm("Are you sure you want to delete this child message?")) {
    post(path, {'type': 'delete_message', 'id': message_id});
    col_wrapper.hidden = true;
  }
  
}




