PlumeX website
==============

- [Site web](https://plumexlyon.github.io/)
- [Dépôt](https://github.com/plumexlyon/)


**Installation et dépendances**

- Python 3
- Pelican:
  ```bash
  python -m pip install pelican pelican_bib pybtex ghp_import
  ```

Lorsqu'on modifie le code source du site, il faut pousser dans la branche
Pelican, i.e.
```bash
git add nouveau.rst
git commit -m "Nouveau fichier"
git push origin pelican
```

Le déploiement dans la branche "Pages" se fait via le Makefile.

Déploiement en local
====================

```bash
make html
make serve
```

Déploiement sur Github Pages
============================

```bash
make publish
make github
```

Documentation
=============

- [ReStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Pelican](https://docs.getpelican.com/en/stable/)


