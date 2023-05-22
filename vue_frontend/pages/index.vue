<script>
import { mapGetters } from 'vuex'
export default {
  name: "IndexPage",
  computed: {
    ...mapGetters(['isAuthenticated'])
  },
  methods: {

    async signoutHandler() {
      try {

        //await this.$axios.post('/signout/');
        await this.$auth.logout();

        this.$router.push('/');
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
        <NuxtLink to="/profesionales">Profesionales</NuxtLink>

        <NuxtLink to="/reporte">Cargar reporte</NuxtLink>

        <v-form action="/signout" method="POST">
          <v-btn id="boton" type="submit" @click="signoutHandler"
            >Cerrar sesión</v-btn
          ></v-form
        >
      </template>
      <template v-else>
        <NuxtLink to="/signup">Registrarse</NuxtLink>

        <NuxtLink to="/login">Iniciar sesión</NuxtLink></template
      >
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
  color: #2c3e50;
  margin-top: 40px;
}
</style>