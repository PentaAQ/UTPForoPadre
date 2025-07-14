function confirmDelete(categoryName, deleteUrl) {
  document.getElementById('categoryName').textContent = categoryName;
  document.getElementById('deleteLink').href = deleteUrl;
  document.getElementById('deleteModal').classList.remove('hidden');
}

function closeDeleteModal() {
  document.getElementById('deleteModal').classList.add('hidden');
}

document.getElementById('deleteModal').addEventListener('click', function(e) {
  if (e.target === this) {
    closeDeleteModal();
  }
});

document.getElementById('gridView').addEventListener('click', function() {
  document.getElementById('gridContainer').classList.remove('hidden');
  document.getElementById('listContainer').classList.add('hidden');
  this.classList.add('bg-white', 'text-gray-700', 'shadow-sm');
  this.classList.remove('text-gray-500');
  document.getElementById('listView').classList.remove('bg-white', 'text-gray-700', 'shadow-sm');
  document.getElementById('listView').classList.add('text-gray-500');
});

document.getElementById('listView').addEventListener('click', function() {
  document.getElementById('listContainer').classList.remove('hidden');
  document.getElementById('gridContainer').classList.add('hidden');
  this.classList.add('bg-white', 'text-gray-700', 'shadow-sm');
  this.classList.remove('text-gray-500');
  document.getElementById('gridView').classList.remove('bg-white', 'text-gray-700', 'shadow-sm');
  document.getElementById('gridView').classList.add('text-gray-500');
});

document.querySelector('input[placeholder*="Buscar"]').addEventListener('input', function(e) {
  const searchTerm = e.target.value.toLowerCase();
  
  const gridCards = document.querySelectorAll('#gridContainer > div');
  gridCards.forEach(card => {
    const text = card.textContent.toLowerCase();
    if (text.includes(searchTerm)) {
      card.style.display = '';
    } else {
      card.style.display = 'none';
    }
  });
  
  const listRows = document.querySelectorAll('#listContainer tbody tr');
  listRows.forEach(row => {
    const text = row.textContent.toLowerCase();
    if (text.includes(searchTerm)) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
});