<script>
import { mapGetters } from "vuex";
export default {
  name: "Login",
  middleware: "guest",
  head() {
    return {
      title: "Iniciar sesión - Rotativa Myra",
    };
  },
  data() {
    return {
      email: "",
      password: "",
    };
  },
  computed: {
    ...mapGetters({ isAuthenticated: "isAuthenticated" }),
  },
  mounted: function () {
    if (this.isAuthenticated) {
      this.$router.push("/home");
    }
  },
  methods: {
    async loginHandler() {
      const data = { email: this.email, password: this.password };
      console.log(data);
      try {
        this.$auth.loginWith("local", {
          data: { email: this.email, password: this.password },
        });
        //this.$router.push("/home");
      } catch (e) {
        console.log("Error:", e.message);
      }
    },
  },
};
</script>

<template>
  <v-app id="inspire">
    <v-main>
      <v-container fluid fill-height>
        <v-layout id="layoutLogin" align-center justify-center>
          <v-flex>
            <v-card class="elevation-12" id="cuerpoForm">
              <v-toolbar id="bordeInicioSesion">
                <v-toolbar-title id="textoInicioSesion"
                  >Inicio de sesión</v-toolbar-title
                >
              </v-toolbar>
              <v-card-text>
                <v-form method="POST">
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
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn id="boton" type="submit" @click="loginHandler"
                  >Iniciar sesión</v-btn
                >
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
#bordeInicioSesion {
  background: #005d71;
  border-radius: 12px;
}

#textoInicioSesion {
  color: #ffffff;
}

#boton {
  background-color: #48abbf;
  color: #ffffff;
  border-radius: 9px;
}

#cuerpoForm {
  border-radius: 12px;
}
#layoutLogin {
  width: 30%;
}
</style>