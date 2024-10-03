function showLoader() {
    var loader = document.getElementById("loader");
    loader.classList.add("active"); // Exibe o loader


    setTimeout(function() {
        loader.classList.remove("active");
    }, 30000);
}
