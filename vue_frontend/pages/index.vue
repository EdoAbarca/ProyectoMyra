<template>

  <div class="container">
    <title> Rotativa Myra - Home</title>
    <v-row justify="center" alling="center">
      <h1 class="text-center">Pingeso</h1>
      <hr />

      <form action="/profesionales">
        <button type="submit" value="VentanaProfesionales">
          Profesionales
        </button>
      </form>

      <form action="/test_reporte">
        <button type="submit" value="VentanaReporte">
          Prueba subida reporte
        </button>
      </form>
    </v-row>

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
}
</script>

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