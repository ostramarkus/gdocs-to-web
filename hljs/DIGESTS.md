## Subresource Integrity

If you are loading Highlight.js via CDN you may wish to use [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) to guarantee that you are using a legimitate build of the library.

To do this you simply need to add the `integrity` attribute for each JavaScript file you download via CDN. These digests are used by the browser to confirm the files downloaded have not been modified.

```html
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js"
  integrity="sha384-5xdYoZ0Lt6Jw8GFfRP91J0jaOVUq7DGI1J5wIyNi0D+eHVdfUwHR4gW6kPsw489E"></script>
<!-- including any other grammars you might need to load -->
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/languages/go.min.js"
  integrity="sha384-HdearVH8cyfzwBIQOjL/6dSEmZxQ5rJRezN7spps8E7iu+R6utS8c2ab0AgBNFfH"></script>
```

The full list of digests for every file can be found below.

### Digests

```
sha384-Cmq5lORXzyHraasLNqmfchH07JRXyEmjDF+j6tSggoXjYHwtgX/ySW6kkRytM5uu /es/languages/python.js
sha384-ZV5sgX70bBgLkDR5Mtox5UsbJedBc39hRKPdvTw6miK4lSkE/wv94cLY2iyZb/sB /es/languages/python.min.js
sha384-9jy7CI5TLYs91VYlZ4S0czQFpDsMzc9jakiJ5RqCFZugGpdPglP94JPAyEhMBwJp /es/languages/python-repl.js
sha384-CO+NiDedness48VlHW0FCIw9rQt8szFZ0IOXYiQo3LEAHLytXxM5NlKnmNYBUACQ /es/languages/python-repl.min.js
sha384-ueSSFZFqg7cVD0dpEqIk9EefJiJUYan0PH6I8u/p+bNLLx7dMs4J2keMaFXqCN8P /languages/python.js
sha384-eXRt+aAa2ig1yFVDQCLis8k9s/1dikTcigj+/R07yNdIxc8BAG/b1uHDyEW3of17 /languages/python.min.js
sha384-Zr5t2YaLU0giGFY/MuBA8UrK47JGpd9DuryiosYFRSQ6EJfTIF9mt8IJp/4/hpOU /languages/python-repl.js
sha384-n3iFvvEGhuJlnYpLj6JaCg7WiOhd8kQfKTZBDnpJwFZ0puRMhoq9JWtKDRw5Snyq /languages/python-repl.min.js
sha384-qPnLN43X7KBBVeEG0mhUAQ9+Gk+Sao1ka5c5BDx/9pteM7xa+E7DOZ8/+S+YUIVk /highlight.js
sha384-41MR3R6W6JwSIqs3pfq9hksjLHnVYr7T7cUJ0dboJPvhZD6j0p5oAGCzfPRkF6WZ /highlight.min.js
```

