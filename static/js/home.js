  document.addEventListener('DOMContentLoaded', function() {
    const input    = document.getElementById('searchInput');
    const select   = document.getElementById('categoryFilter');
    const articles = Array.from(document.querySelectorAll('main article'));

    function filterArticles() {
      const term     = input.value.trim().toLowerCase();
      const category = select.value;

      articles.forEach(article => {
        const title   = article.querySelector('h2')?.textContent.toLowerCase() || '';
        const content = article.querySelector('p')?.textContent.toLowerCase() || '';
        const cat     = article.getAttribute('data-category');

        const matchesText = term === '' 
          || title.includes(term) 
          || content.includes(term);

        const matchesCategory = category === 'Todas las categorías' 
          || cat === category;
        article.style.display = (matchesText && matchesCategory) 
          ? '' 
          : 'none';
      });
    }
    input.addEventListener('input', filterArticles);
    select.addEventListener('change', filterArticles);
  });