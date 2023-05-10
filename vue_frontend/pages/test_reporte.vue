<script>
import axios from "axios"
export default {
  name: 'Test_reportePage',
  data: () => ({
    exceel:{},
  }),
  methods:{
    async uploadExcel(){
        const input = document.getElementById("reporte_excel");
        var formData = new FormData();
        formData.append("excel", input);
        console.log(formData);

        // Mandar a backend
        await axios.post('http://localhost:8000/api/cargar_excel/', formData, {headers:{'Content-Type': 'multipart/form-data'}}).then(Response => console.log(Response)).catch(err => {console.log(err)});

        
      }
  }
}
</script>


<template>

  <div class="container">
    <title> Rotativa Myra - Home</title>
    <h1 justify="center" alling="center">EXCEL</h1>
    <form method="post" enctype="multipart/form-data">
        <input id="reporte_excel" name="excel_file" type="file"/>
        <button type="submit" @change="uploadExcel()">Upload</button>
    </form>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
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