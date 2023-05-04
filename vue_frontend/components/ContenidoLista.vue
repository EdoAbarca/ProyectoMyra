<script>
import ProfesionalLista from './ProfesionalLista.vue'

export default {
  data() {
        return {
          profesionalElegido:{
            NombreProfesional: "",
            RutProfesional: "",
            AreaProfesional:""
          },

          profesionales:[
            { Nombre: "Natalia Damaris Perello Contreras",
              Rut:"19456957-5",
              Area:"ADMINISTRACION",
            },
            { Nombre: "Mariela Leonardo Tantarico",
              Rut:"20345687-7",
              Area:"CUIDADOS",
            },
            { Nombre: "Will Hermes Torrealba Alvarez",
              Rut:"9234876-0",
              Area:"FONOAUDIOLOGIA",
            },
            { Nombre: "Angelina Elizabeth Cespedes  Cortes",
              Rut:"14987436-7",
              Area:"KINESIOLOGIA",
            },
            { Nombre: "Yelitza Coromoto Ortegano Santiago",
              Rut:"16789657-2",
              Area:"AUXILIARES",
            }

          ]
        }
    },
  components: {
    ProfesionalLista
    },
  computed:{
    eleccionProfesional(nombre,rut,area){
      this.NombreProfesional= nombre;
      this.RutProfesional= rut;
      this.AreaProfesional = area;
    }

  },
  methods:{

  },
  emits:{
    
  }
  }
</script>

<template>
    <div class="ContenedorLista">
        <div class="ContenedorTitulo">Titulo de la vista</div>
        <div class ="ContenidoLista">
            <ul>
                <ProfesionalLista v-for="(profesional,index) in profesionales"
                    :key="profesional.Rut"
                    :nombre="profesional.Nombre"
                    :rut="profesional.Rut"
                    :area="profesional.Area"

                />
            </ul>   
        </div>

    </div>
</template>

<style>
.ContenedorLista{
    position: relative;
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 82%;
    top: 0;
    
    
}
.ContenedorTitulo{
    overflow: hidden;
    position: relative;
    width: 100%;
    height: 25px;
    background-color: #669098;
    margin-top: 8px;
    padding-top: 10px;

    border-radius: 12.5px 12.5px 0px 0px;
    color: white;

    text-align: center;
    vertical-align: middle;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 15px;
    font-weight: 600;
}
.ContenidoLista{
    position: relative;
    height: 100%;
    overflow-y: scroll;

    filter: drop-shadow(0px 1px 1px rgba(0, 0, 0, 0.1));

}
</style>