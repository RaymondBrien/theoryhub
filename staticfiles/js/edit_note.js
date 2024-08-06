/* jshint eversion: 11 */

const editButtons = document.getElementsByClassName("btn-edit");
const noteText = document.getElementById("id_note");
const noteForm = document.getElementById("noteForm");
const submitButton = document.getElementById("submitNoteButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");



/**
 * Initialize edit note form with note content and set action to update note via urls
 * 
 * For each button in the editButtons list, add an event listener to listen for a click event.
 */
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let fullNoteId = e.target.getAttribute("data-note_id");
        let noteId = fullNoteId.replace("note", ""); // remote 'note' from noteId for url handling
        let noteContent = document.querySelector(`#${fullNoteId}`).innerText;
        noteText.value = noteContent;
        noteForm.scrollIntoView({ behavior: 'smooth' });
        submitButton.innerText = "Update";
        noteForm.setAttribute("action", `edit_note/${noteId}/`);
    });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated note's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific note.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let fullNoteId = e.target.getAttribute("data-note_id");
      let noteId = fullNoteId.replace("note", ""); // remote 'note' from noteId for url handling
      deleteConfirm.href = `delete_note/${noteId}/`;
      deleteModal.show();
    });
  }
  
