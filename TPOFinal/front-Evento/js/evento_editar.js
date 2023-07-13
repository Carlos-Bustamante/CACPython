console.log(location.search); // lee los argumentos pasados a este formulario
var id = location.search.substr(4);
console.log(id);
const { createApp } = Vue;
createApp({
  data() {
    return {
      id: 0,
      nombre: "",
      fecha: "",
      precio: 0,
      lugar: "",
      url:"https://cmontanobustamante.pythonanywhere.com/productos/"+id,
      // url:"http://localhost:5000/productos/"+id,
    //   url: "http://mcerda.pythonanywhere.com/productos/" + id,
    };
  },
  methods: {
    fetchData(url) {
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          this.id = data.id;
          this.fecha = data.fecha;
          this.nombre = data.nombre;
          this.lugar = data.lugar;
          this.precio = data.precio;
        })
        .catch((err) => {
          console.error(err);
          this.error = true;
        });
    },
    modificar() {
      let producto = {
        nombre: this.nombre,
        precio: this.precio,
        lugar: this.lugar,
        fecha: this.fecha,
      };
      var options = {
        body: JSON.stringify(producto),
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        redirect: "follow",
      };
      fetch(this.url, options)
        .then(function () {
          alert("Registro modificado");
          window.location.href = "./evento.html";
        })
        .catch((err) => {
          console.error(err);
          alert("Error al Modificar");
        });
    },
  },
  created() {
    this.fetchData(this.url);
  },
}).mount("#app");
