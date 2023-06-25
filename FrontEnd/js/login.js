document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar envío del formulario

    var emailInput = document.getElementById('email');
    var passwordInput = document.getElementById('password');

    var isValid = true;

    // Validación del email
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(emailInput.value)) {
      isValid = false;
      emailInput.classList.add('error');
    } else {
      emailInput.classList.remove('error');
    }

    // Validación de la contraseña
    if (passwordInput.value.trim() === '') {
      isValid = false;
      passwordInput.classList.add('error');
    } else {
      passwordInput.classList.remove('error');
    }

    if (isValid) {
      // Realizar alguna acción, como enviar el formulario
      console.log('Formulario válido. Enviar datos al servidor...');
    }
  });
  

  document.getElementById('toggle-menu').addEventListener('click', function() {
    var menu = document.querySelector('header .menu');
    menu.classList.toggle('active');
  });
  
  