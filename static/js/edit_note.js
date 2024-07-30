const editButtons = document.getElementsByClassName("btn-edit");
const noteText = document.getElementById("id_note");
const noteForm = document.getElementById("noteForm");
const submitButton = document.getElementById("submitNoteButton");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let fullNoteId = e.target.getAttribute("data-note_id");
        let noteId = fullNoteId.replace("note", ""); // remote 'note' from noteId for url handling
        console.log(noteId);
        let noteContent = document.querySelector(`#${fullNoteId}`).innerText;
        noteText.value = noteContent;
        console.log(noteContent);
        submitButton.innerText = "Update";
        noteForm.setAttribute("action", `edit_note/${noteId}/`);
    });
}
