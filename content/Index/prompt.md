Contexte

  Tu vas m'aider a classer mes feuilles de cours
  scannees.

  Chemins

  - Source (scans bruts):
    C:\Users\camillemarchandbelmo\quartz-cours\content\scan
  - Destination (images classees): C:\Users\camillema
    rchandbelmo\quartz-cours\content\Images

  Etapes

  1. Avant de commencer, lis les index dans Index
     pour voir l'index existant et connaitre les
     prefixes deja utilises et leur dernier numero
  2. Regarde toutes les images dans le dossier Images
     pour voir ce qui est deja classe
  3. Regarde toutes les images dans le dossier scan
     pour voir les nouveaux fichiers a classifier
  4. Génère un index temporaire sous la forme d'un fichier .md dans /scan en indiquant la matière de chauqe image et un id temporaire
  5. Après approbation, deplace chaque fichier de scan vers Images en le renommant avec le bon code (ex: FR-1.jpg)
  6. Regenere les index de matière en scannant tout le
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