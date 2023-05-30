<script>
import { mapGetters } from "vuex";
export default {
  name: "IndexPage",
  computed: {
    ...mapGetters(["isAuthenticated"]),
  },
  mounted: function () {
    localStorage.setItem('user', null);
    this.$router.push("/home");
  },
  methods: {
  },
};
</script>

<template>
  <div class="ContenedorIndex">
    <title>Rotativa Myra - Home</title>

    <h1 class="text-center">Pingeso</h1>
    <hr />

    <form action="/home">
      <v-btn id="boton" type="submit" value="VentanaHome">Home</v-btn>
    </form>

    <form action="/register">
      <v-btn id="boton" type="submit" value="VentanaRegistro"
        >Registrarse</v-btn
      >
    </form>

    <form action="/login">
      <v-btn id="boton" type="submit" value="VentanaInicioSesion"
        >Iniciar sesión</v-btn
      >
    </form>

    <form action="/profesionales">
      <v-btn id="boton" type="submit" value="VentanaProfesionales"
        >Profesionales</v-btn
      >
    </form>

    <form action="/reporte">
      <v-btn id="boton" type="submit" value="VentanaReporte"
        >Subir reporte</v-btn
      >
    </form>

    <v-form action="/signout" method="POST">
      <v-btn id="boton" type="submit"
        >Cerrar sesión</v-btn
      >
    </v-form>

    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT"
      crossorigin="anonymous"
    />
  </div>
</template>

<style>
.ContenedorIndex {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

#boton {
  background-color: #48abbf;
  color: #ffffff;
  border-radius: 9px;
  margin-top: 3%;
}
</style>