<script>
export default {
  name: "Signup",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      repeatPassword: "",
    };
  },
  methods: {
    async registerHandler() {
      const data = {
        username: this.username,
        email: this.email,
        password: this.password,
        repeatPassword: this.repeatPassword,
      };
      console.log(data);
      try {
        const res = await this.$axios.post("/register", {
          username: this.username,
          email: this.email,
          password: this.password,
          repeatPassword: this.repeatPassword,
        });
        console.log(res);
        const data = res.data;
        console.log(data);
        //localStorage.setItem('user', data);
        this.$router.push("/login");
      } catch (e) {
        console.log("Error", e.message);
      }
    },
  },
};
</script>

<template>
  <v-app id="registro">
    <v-main>
      <v-container fluid fill-height>
        <v-layout id="layout" align-center justify-center>
          <v-flex id="cflex">
            <v-card class="elevation-12" id="cuerpoForm">
              <v-toolbar id="bordeRegistro">
                <v-toolbar-title id="textoRegistro"
                  >Registro de usuario
                </v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form method="POST">
                  <v-text-field
                    name="username"
                    label="Usuario"
                    type="text"
                    v-model="username"
                  ></v-text-field>
                  <v-text-field
                    name="email"
                    label="Correo electrónico"
                    type="text"
                    v-model="email"
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    name="password"
                    label="Contraseña"
                    type="password"
                    v-model="password"
                  ></v-text-field>
                  <v-text-field
                    id="repeatPassword"
                    name="repeatPassword"
                    label="Repetir contraseña"
                    type="password"
                    v-model="repeatPassword"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn id="boton" @click="registerHandler">Registrarse</v-btn>
                <v-btn id="boton" href="/home">Volver</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>



<style>
#textoRegistro {
  color: #ffffff;
}

#boton {
  background-color: #48abbf;
  color: #ffffff;
  border-radius: 9px;
}
#bordeRegistro {
  background: #005d71;
  border-radius: 12px;
}

#cuerpoForm {
  border-radius: 12px;
  width: 100%;
}
#layout {
  width: 45%;
}
</style>