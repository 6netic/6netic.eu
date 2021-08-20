
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


function zone(id1, id2, id3) {

  // Retrieving 'Commentaires' field content
  let comments = document.getElementById(id1).textContent;

  // Again selecting 'Commentaires' field
  let zoneRectangle = document.getElementById(id1);
  zoneRectangle.textContent = '';

  let txtArea = document.createElement('textArea');
  txtArea.textContent = comments;
  zoneRectangle.appendChild(txtArea);

  let saveBtn = document.createElement("button");
  saveBtn.style.position = "relative";
  saveBtn.style.backgroundColor = "#4CAF50";
  saveBtn.style.border = "none";
  saveBtn.style.color = "white";
  saveBtn.style.textAlign = "center";
  saveBtn.style.width = "50%";
  saveBtn.textContent = "Enregistrer";
  saveBtn.style.marginTop = "3%";
  zoneRectangle.appendChild(saveBtn);

  // 'Modify' button disappears
  let boutField = document.getElementById(id2);
  boutField.style.display = "none";

  saveBtn.onclick = function() {
    // Saving the note using AJAX with POST method
    let output = encodeURIComponent(txtArea.value);
    let number = id3
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "saveComment", true);
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.send('note=' + output + '&number=' + number);

    // Retrieving notes added
    zoneRectangle.textContent = txtArea.value;
    boutField.style.display = "block";
  }
}
