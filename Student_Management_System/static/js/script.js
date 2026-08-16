// ===============================
// Student Management System
// JavaScript
// ===============================

console.log("student Management System Loaded");

//Delete Confirmation

function confirmDelete(){

    return confirm("Are you sure want to delete this student?");

}

// search Validation

function validateSearch(){

    let keywordInput = document.querySelector("input[name='keyword']");
    let keyword = keywordInput ? keywordInput.value : "";

    if (keyword.trim() === ""){

        alert("Please enter a search keyword.");

        return false;
    }

    return true;

}

//Success Message

function showMessage(message){

    alert(message);
}