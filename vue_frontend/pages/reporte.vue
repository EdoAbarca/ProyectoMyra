<script>
export default {
  head() {
    return {
      title: "Cargar reporte - Rotativa Myra",
    };
  },
  name: "Reporte",
  middleware: "auth",
  data() {
    return {
      title: null,
      date: null,
      excel: null,
    };
  },
  methods: {
    async reportHandler() {
      const data = {
        title: this.title,
        date: this.date,
        excel: this.excel,
      };
      console.log(data);
      try {
        const res = await this.$axios.post("/carga_excel", data);
        console.log(res);
      } catch (e) {
        console.log(e.message);
      }
    },
  },
};
</script>


<template>
  <v-app id="ventanaReporte">
    <v-main>
      <v-container fluid fill-height>
        <v-layout id="layoutReporte" align-center justify-center>
          <v-flex>
            <v-card class="elevation-12" id="cuerpoForm">
              <v-toolbar id="bordeReporte" :elevation="0">
                <v-toolbar-title id="textoReporte"
                  >Cargar reporte</v-toolbar-title
                >
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    name="title"
                    label="Título"
                    type="text"
                    v-model="title"
                  ></v-text-field>
                  <v-text-field
                    name="date"
                    label="Fecha de reporte"
                    type="date"
                    v-model="date"
                  ></v-text-field>
                  <v-text-field
                    id="excel"
                    name="Archivo"
                    label="Excel"
                    type="file"
                    v-model="excel"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn id="boton" @click="reportHandler">Subir</v-btn>
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
#ventanaReporte {
  opacity: 1;
}
#textoReporte {
  color: #005d71;
}

#boton {
  background-color: #48abbf;
  color: #ffffff;
  border-radius: 9px;
}
#bordeReporte {
  border-radius: 12px 12px 0 0;
}

#cuerpoForm {
  border-radius: 12px;
}
#layoutReporte {
  width: 30%;
}
</style>