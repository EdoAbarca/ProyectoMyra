<script>
 
    export default {
       name: 'Login',
       data() {
          return {
             email: null,
             password: null
          }
       },
       methods: {
         async loginHandler() {
             const data = { 'email': this.email, 'password': this.password };
             console.log(data);
             
             try{
                const response = await this.$auth.loginWith('local', data);
                //const responseBackend = await this.$axios.post('http://localhost:8000/api/signin', data);
                console.log(response);
                //console.log(responseBackend);

                this.$router.push('/');
    
             } catch(e) {
                console.log(e.message);
             }
             
          }
       }
    };
    </script>

<template>
    <v-app id="inspire">
       <v-main>
          <v-container fluid fill-height>
             <v-layout align-center justify-center>
                <v-flex xs12 sm8 md4>
                   <v-card class="elevation-12" id="cuerpoForm">
                      <v-toolbar id="bordeInicioSesion">
                         <v-toolbar-title id ="textoInicioSesion">Inicio de sesión</v-toolbar-title>
                      </v-toolbar>
                      <v-card-text>
                         <v-form action="/signin" method = "POST">
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
                         <v-btn id="boton" type = "submit" @click="loginHandler">Iniciar sesión</v-btn>
                         <v-btn id="boton"  href="/">Volver</v-btn>
                      </v-card-actions>
                   </v-card>
                </v-flex>
             </v-layout>
          </v-container>
       </v-main>
    </v-app>
 </template>


<style>
#bordeInicioSesion{
   background: #005D71;
   border-radius: 12px;
}

#textoInicioSesion{
   color: #ffffff;
}

#boton{
   background-color: #48ABBF;
   color: #ffffff;
   border-radius: 9px;
}

#cuerpoForm{
   border-radius: 12px;
}
</style>