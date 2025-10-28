// Hitta alla <pre><code>-block
document.querySelectorAll('pre').forEach(pre => {
    let copySymbol = '🗐' 
  // Skapa en knapp
  const button = document.createElement('button');
  button.textContent = copySymbol;
  button.className = 'copy-btn';
  pre.appendChild(button);

  // Lägg till klickhändelse
  button.addEventListener('click', async () => {
    const code = pre.querySelector('code').innerText;

    try {
      await navigator.clipboard.writeText(code);
      setTimeout(() => button.textContent = copySymbol, 2000);
    } catch (err) {
      console.error('Kunde inte kopiera text: ', err);
      button.textContent = 'Fel!';
    }
  });
});

// Highlight links

document.querySelectorAll('.section-link a').forEach(sectionLink => {
  sectionLink.addEventListener('click', async () => {
    let articlesList = sectionLink.nextElementSibling;
    if (articlesList.classList.contains('open')) {
      articlesList.classList.remove('open');
    } else {
      articlesList.classList.add('open');
    }
    
  });
  
  sectionLink.addEventListener('mouseleave', async () => {
    let articlesList = sectionLink.querySelector('ul');
  });
});

// Scrollspy

const sections = document.querySelectorAll("main section");
const navLinks = document.querySelectorAll("#toc a");

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      const id = entry.target.getAttribute("id");
      const link = document.querySelector('#toc a[href="#' + id + '"]');
      if (entry.isIntersecting) {
        navLinks.forEach((l) => l.classList.remove("active"));
        link.classList.add("active");
      }
    });
  },
  {
    root: null,              // observerar i viewporten
    threshold: 0,            // trigga så fort något syns
    rootMargin: "-50% 0px -50% 0px" // mitten av sidan (övre halvan)
  }
);

sections.forEach((section) => observer.observe(section));