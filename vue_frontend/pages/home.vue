<template>
  <div class="container">
    <title> Pingeso </title>
    <v-row justify="center" alling="center">
      <h1 class="text-center">Proyecto Rotativa Myra 2023</h1>
      <hr />
      <form action="/profesionales">
        <button type="submit" value="Profesionales">
          Ver profesionales
        </button>
      </form>
      <form action="/pacientes">
        <button type="submit" value="Pacientes">
          Ver pacientes
        </button>
      </form>
      <form action="/coordinadores">
        <button type="submit" value="Coordinadores">
          Ver coordinadores
        </button>
      </form>
      <form action="/alertas">
        <button type="submit" value="Alertas">
          Ver alertas
        </button>
      </form>
      <form action="/login">
        <button type="submit" value="Inicio sesion">
          Iniciar sesion <!--Dejar esto en navbar-->
        </button>
      </form>
      <form action="/signup">
        <button type="submit" value="Registro">
          Registrarse <!--Dejar esto en navbar-->
        </button>
      </form>
    </v-row>

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>
