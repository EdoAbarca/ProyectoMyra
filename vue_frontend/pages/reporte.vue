<script>

/* 
export default {
  name: 'Test_reportePage',
  data: () => ({
    exceel:{},
  }),
  methods:{
    async reportHandler(){
        const input = document.getElementById("reporte_excel");
        var formData = new FormData();
        formData.append("excel", input);
        console.log(formData);

        // Mandar a backend
        await axios.post('http://localhost:8000/api/cargar_excel/', formData, {headers:{'Content-Type': 'multipart/form-data'}}).then(Response => console.log(Response)).catch(err => {console.log(err)});

        
      }
  }
}*/
import axios from "axios"
export default {
   name: 'Reporte',
   data() {
      return {
         title: null,
         date: null,
         excel: null,
      }
   },
   methods: {
      async reportHandler() {
         const data = {
            'title': this.title,
            'date': this.date,
            'excel': this.excel
         };
         console.log(data);
         try {
             const res = await this.$axios.post('/carga_excel', data);
             console.log(res);
         }
         catch(e) {
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
                     <v-toolbar id="bordeReporte">
                        <v-toolbar-title id="textoReporte">Cargar reporte</v-toolbar-title>
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
                        <v-btn id="boton"  href="/">Volver</v-btn>
                     </v-card-actions>
                  </v-card>
               </v-flex>
            </v-layout>
         </v-container>
      </v-main>
   </v-app>
</template>
<!--
  <div class="container">
    <title> Rotativa Myra - Home</title>
    <h1 justify="center" alling="center">EXCEL</h1>
    <form method="post" enctype="multipart/form-data">
        <input id="reporte_excel" name="excel_file" type="file"/>
        <button type="submit" @change="uploadExcel()">Upload</button>
    </form>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  </div> -->



<style>
#textoReporte{
   color: #ffffff;
}

#boton{
   background-color: #48ABBF;
   color: #ffffff;
   border-radius: 9px;
}
#bordeReporte{
   background: #005D71;
   border-radius: 12px;
}

#cuerpoForm{
   border-radius: 12px;
}
</style>