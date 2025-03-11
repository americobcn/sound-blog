let switchCommentForm;
let cancelCommentButton;

document.addEventListener("DOMContentLoaded", () => {
  switchCommentForm = () => {
    const button = document.getElementById("comment-button");
    const commentForm = document.getElementById("comment-form");
    if (
      commentForm.style.display === "none" ||
      commentForm.style.display === ""
    ) {
      commentForm.style.display = "block";
      button.style.display = "none";
      commentForm.scrollIntoView({ behavior: "smooth", block: "end" });
    } else {
      commentForm.style.display = "none";
      button.style.display = "inline";
    }
  };

  cancelCommentButton = () => {
    const commentForm = document.getElementById("comment-form");
    const button = document.getElementById("comment-button");
    commentForm.style.display = "none";
    button.innerHTML = "Add Comment";
    button.style.display = "inline";
  };

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      cancelCommentButton();
    }
  });
});
