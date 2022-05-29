var checkbox = document.getElementById('flexSwitchCheckDefault');
if (checkbox != null) {
    checkbox.addEventListener('change', () => {
        if (checkbox.checked) {
            document.documentElement.setAttribute('data-theme', 'dark');
            sessionStorage.setItem("theme", "dark");
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            sessionStorage.setItem("theme", "light");
        }
    });

}

window.addEventListener('load', (event) => {
    if (sessionStorage.getItem("theme") == "dark") {
        document.documentElement.setAttribute('data-theme', 'dark');
        if (document.getElementById('flexSwitchCheckDefault') != null)
            document.getElementById('flexSwitchCheckDefault').checked = true;
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        if (document.getElementById('flexSwitchCheckDefault') != null)
            document.getElementById('flexSwitchCheckDefault').checked = false;
    }
});