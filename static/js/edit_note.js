const editButtons = document.getElementsByClassName("btn-edit");
const noteText = document.getElementById("id_body");
const noteForm = document.getElementById("noteForm");
const submitButton = document.getElementById("submitNoteButton");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let noteId = e.target.getAttribute("data-note_id");
        console.log(noteId);
        let noteContent = document.querySelector(`#note${noteId} .note-content`).innerText.trim();
        noteText.value = noteContent;
        submitButton.innerText = "Update";
        noteForm.setAttribute("action", `edit_note/${noteId}`);
    });
}
