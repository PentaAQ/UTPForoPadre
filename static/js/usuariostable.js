function confirmDelete(userName, deleteUrl) {
    document.getElementById("userName").textContent = userName;
    document.getElementById("deleteLink").href = deleteUrl;
    document.getElementById("deleteModal").classList.remove("hidden");
  }

function closeDeleteModal() {
    document.getElementById("deleteModal").classList.add("hidden");
  }

function confirmDesactivar(userN, desactivarUrl) {
    document.getElementById("userN").textContent = userN;
    document.getElementById("desactivarLink").href = desactivarUrl;
    document.getElementById("desactivarUModal").classList.remove("hidden");
  }
function closeDesactivarUModal() {
    document.getElementById("desactivarUModal").classList.add("hidden");
  }


  document
    .getElementById("deleteModal")
    .addEventListener("click", function (e) {
      if (e.target === this) {
        closeDeleteModal();
      }
    });

  document
    .getElementById("searchUserInput")
    .addEventListener("input", function (e) {
      const searchTerm = e.target.value.toLowerCase();
      const rows = document.querySelectorAll("tbody tr");

      rows.forEach((row) => {
        const text = row.textContent.toLowerCase();
        if (text.includes(searchTerm)) {
          row.style.display = "";
        } else {
          row.style.display = "none";
        }
      });
    });

  document
    .querySelector('thead input[type="checkbox"]')
    .addEventListener("change", function (e) {
      const checkboxes = document.querySelectorAll(
        'tbody input[type="checkbox"]'
      );
      checkboxes.forEach((checkbox) => {
        checkbox.checked = e.target.checked;
      });
    });

  const roleFilter = document.getElementById("roleFilter");
  const statusFilter = document.getElementById("statusFilter");
  const searchInput = document.getElementById("searchUserInput");
  const rows = document.querySelectorAll("tbody tr");

  function filterRows() {
    const term = searchInput.value.toLowerCase();
    const role = roleFilter.value;
    const status = statusFilter.value;

    rows.forEach((row) => {
      const text = row.textContent.toLowerCase();
      const rowRole = row.dataset.role;
      const rowStatus = row.dataset.status;

      const matchesText = text.includes(term);
      const matchesRole = role === "all" || rowRole === role;
      const matchesStatus = status === "all" || rowStatus === status;

      row.style.display =
        matchesText && matchesRole && matchesStatus ? "" : "none";
    });
  }

  
  searchInput.addEventListener("input", filterRows);
  roleFilter.addEventListener("change", filterRows);
  statusFilter.addEventListener("change", filterRows);
