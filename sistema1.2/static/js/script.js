document.addEventListener('DOMContentLoaded', function() {
    // Funcionalidad del menú lateral
    const openMenuBtn = document.getElementById('openMenu');
    const closeMenuBtn = document.getElementById('closeMenu');
    const sideMenu = document.getElementById('sideMenu');

    openMenuBtn.addEventListener('click', function() {
        sideMenu.classList.add('open');
    });

    closeMenuBtn.addEventListener('click', function() {
        sideMenu.classList.remove('open');
    });

    // Funcionalidad del menú desplegable del usuario
    const userIcon = document.getElementById('userIcon');
    const userDropdown = document.getElementById('userDropdown');

    userIcon.addEventListener('click', function(event) {
        event.stopPropagation();
        userDropdown.classList.toggle('show');
    });

    window.addEventListener('click', function(event) {
        if (!userIcon.contains(event.target)) {
            userDropdown.classList.remove('show');
        }
    });

    sessionStorage.setItem("usuarioAutenticado", "true");
        
});