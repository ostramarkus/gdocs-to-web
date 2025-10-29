// Nav-toggle
document.getElementById('menu-toggle').addEventListener('click', async () => {
  let navAside = document.getElementById('nav-container');
  if (navAside.classList.contains('nav-open')) {
    document.getElementById('nav-container').classList.remove('nav-open');
  } else {
    document.getElementById('nav-container').classList.add('nav-open');
  }
})

document.querySelectorAll('#toc a').forEach(link => {
  link.addEventListener('click', async => {
    let navAside = document.getElementById('nav-container');  
    if (navAside.classList.contains('nav-open')) {
      document.getElementById('nav-container').classList.remove('nav-open');
    }
  })
})

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

document.querySelectorAll('.section-link > a').forEach(sectionLink => {
  sectionLink.addEventListener('click', async () => {
    if (sectionLink.classList.contains('section-open')) {
      sectionLink.classList.remove('section-open');
    } else {
      sectionLink.classList.add('section-open');
    }

    // Get ul-tag that is sibling to a-tag
    let articlesList = sectionLink.nextElementSibling;

    // Toggle ul-tagg classname 'open'
    if (articlesList.classList.contains('articles-open')) {
      articlesList.classList.remove('articles-open');
    } else {
      // Close all dropdowns
      document.querySelectorAll('.section-link ul').forEach(dropDown => {
        dropDown.classList.remove('articles-open')
      })
      articlesList.classList.add('articles-open');
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