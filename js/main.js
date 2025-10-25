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