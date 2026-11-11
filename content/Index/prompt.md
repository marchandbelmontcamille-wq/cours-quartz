Contexte

  Tu vas m'aider a classer mes feuilles de cours
  scannees.

  Chemins

  - Source (scans bruts):
    C:\Users\camillemarchandbelmo\cours-quartz\content\sc
  - Destination (images classees): C:\Users\camillema
    rchandbelmo\cours-quartz\content\images

  Etapes

  1. Avant de commencer, lis les index dans /content/Index
     pour voir l'index existant et connaitre les
     prefixes deja utilises et leur dernier numero
  2. Regarde toutes les images dans le dossier Images
     pour voir ce qui est deja classe
  3. Regarde toutes les images dans le dossier sc
     pour voir les nouveaux fichiers a classifier
  4. Utilise Tesseract pour voir le contenu des images
  5. crée un mini site web tenant en un fichier index.html qui attribue à chaque fichier un id temporaire (FR-**; MA-**; etc)et les classe par matière
  6. après que j'ai aprouvé, transfère tous les documents en les renommant avec le bon id
  7. Regenere les index de matière en scannant tout le
     dossier Images

  Format de l'index

  L'index est organise par matiere. Pour chaque
  matiere, un index puis chaque fichier avec son
  code en gras et un embed Obsidian:

  ## Francais

  - **FR-1**
    ![[FR-1.jpg]]
  - **FR-2**
    ![[FR-2.jpg]]

  ## Anglais

  - **AN-1**
    ![[AN-1.png]]

  ## Mathematiques

  - **MA-1**
    ![[MA-1.pdf]]
  - **MA-2**
    ![[MA-2.pdf]]

  Regles

  - Si un prefixe est nouveau (pas encore dans
    l'index), demande-moi quel nom de matiere lui
    associer
  - Trie les numeros par ordre croissant dans chaque
    matiere
  - Ne touche pas aux fichiers deja dans Images