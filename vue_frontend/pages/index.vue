<script>
import { mapGetters } from "vuex";
export default {
  name: "IndexPage",
  computed: {
    ...mapGetters(["isAuthenticated"]),
  },
  methods: {
    async signoutHandler() {
      try {
        //await this.$axios.post('/signout/');
        await this.$auth.logout();

        this.$router.push("/");
      } catch (e) {
        console.log(e.message);
      }
    },
  },
};
</script>

<template>
  <div class="container">
    <title>Rotativa Myra - Home</title>
    <v-row justify="center" alling="center">
      <h1 class="text-center">Pingeso</h1>
      <hr />

      <template v-if="isAuthenticated">
        <form action="/profesionales">
          <v-btn  id="boton" type="submit" value="VentanaProfesionales">
            Profesionales
          </v-btn >
        </form>

        <form action="/reporte">
          <v-btn  id="boton" type="submit" value="VentanaReporte">
            Subir reporte
          </v-btn >
        </form>

        <v-form action="/signout" method="POST">
          <v-btn  id="boton" type="submit" @click="signoutHandler"
            >Cerrar sesión</v-btn 
          ></v-form
        >
      </template>
      <template v-else>
        <form action="/register">
          <v-btn id="boton" type="submit" value="VentanaRegistro">Registrarse</v-btn >
        </form>

        <form action="/login">
          <v-btn id="boton" type="submit" value="VentanaInicioSesion">
            Iniciar sesión
          </v-btn >
        </form>
      </template>
    </v-row>

    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT"
      crossorigin="anonymous"
    />
  </div>
</template>

<style>
* {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

#boton {
  background-color: #48abbf;
  color: #ffffff;
  border-radius: 9px;
}
</style>