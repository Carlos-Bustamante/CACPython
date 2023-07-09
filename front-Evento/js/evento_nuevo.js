function guardar(){
    let n = document.getElementById('nombre').value;
    let p = document.getElementById('precio').value;
    let s = document.getElementById('fecha').value;
    let i = document.getElementById('lugar').value;

    let producto = {
        nombre: n,
        precio: p,
        fecha: f,
        lugar: l
    };

    let url = 'http://127.0.0.1:5000/productos'
    let options = {
        body: JSON.stringify(producto),
        method: 'POST',
        headers: {'Content-Type': 'application/json'}
    }

    fetch(url, options)
    .then(function(){
        alert("Producto agregado exitosamente");
        window.location.href = './evento.html'
    })
    .catch(error => {
        alert('No pudo agregarse el producto');
        console.error(error);
    })
}