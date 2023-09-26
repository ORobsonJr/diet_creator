<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&display=swap" rel="stylesheet">
    <style>
    nav[id="navbar-id"] {
      position: fixed;
      width: 100%;
      z-index: 9999;
    }

    .body-gap {
      padding-top: 50px
    }

  </style>
</head>
<body>
  <nav class="navbar bg-body-tertiary" id="navbar-id" style="background-color: #20C389;">
    <div class="unique-container">
      <a class="navbar-brand" href="/" style="color: white;">Diet Creator</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="body-gap"></div>
  <script>
      // Obtém a altura da barra de navegação
      var navbarHeight = document.getElementById('navbar-id').offsetHeight;

      // Ajusta o espaçamento superior do conteúdo abaixo da barra de navegação
      document.querySelector('.body-gap').style.paddingTop = navbarHeight + 'px';
  </script>
</body>
</html>