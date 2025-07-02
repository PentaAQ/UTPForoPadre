document.addEventListener("DOMContentLoaded", function () {
  const toggleButtons = document.querySelectorAll('button[type="button"]');
  toggleButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const input = this.parentElement.previousElementSibling;
      if (input.type === "password") {
        input.type = "text";
        this.innerHTML = '<span class="text-lg">🙈</span>';
      } else {
        input.type = "password";
        this.innerHTML = '<span class="text-lg">👁️</span>';
      }
    });
  });
});
