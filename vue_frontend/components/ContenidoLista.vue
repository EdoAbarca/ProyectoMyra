<script>
import ProfesionalLista from './ProfesionalLista.vue'

export default {
  data() {
        return {
          profesionales:[
            { nombre: "Natalia Damaris Perello Contreras",
              rut:"19456957-5",
              area:"ADMINISTRACION",
            },
            { nombre: "Natalia Damaris Perello Contreras",
              rut:"19456957-5",
              area:"ADMINISTRACION",
            },
            { nombre: "Natalia Damaris Perello Contreras",
              rut:"19456957-5",
              area:"ADMINISTRACION",
            },
            { nombre: "Natalia Damaris Perello Contreras",
              rut:"19456957-5",
              area:"ADMINISTRACION",
            },
            { nombre: "Natalia Damaris Perello Contreras",
              rut:"19456957-5",
              area:"ADMINISTRACION",
            },
            { nombre: "Natalia Damaris Perello Contreras",
              rut:"19456957-5",
              area:"ADMINISTRACION",
            },
            { nombre: "Natalia Damaris Perello Contreras",
              rut:"19456957-5",
              area:"ADMINISTRACION",
            },
            { nombre: "Natalia Damaris Perello Contreras",
              rut:"19456957-5",
              area:"ADMINISTRACION",
            },
            { nombre: "Natalia Damaris Perello Contreras",
              rut:"19456957-5",
              area:"ADMINISTRACION",
            },
            
            { nombre: "Mariela Leonardo Tantarico",
              rut:"20345687-7",
              area:"CUIDADOS",
            },
            { nombre: "Will Hermes Torrealba Alvarez",
              rut:"9234876-0",
              area:"FONOAUDIOLOGIA",
            },
            { nombre: "Angelina Elizabeth Cespedes  Cortes",
              rut:"14987436-7",
              area:"KINESIOLOGIA",
            },
            { nombre: "Yelitza Coromoto Ortegano Santiago",
              rut:"16789657-2",
              area:"AUXILIARES",
            }

          ]
        }
    },
  components: {
    ProfesionalLista
    },
  computed:{
  },

  }
</script>

<template>
    <div class="ContenedorLista">
        <div class="ContenedorTitulo">Titulo de la vista</div>
        <div class ="ContenidoLista">
            <ul>
                <ProfesionalLista v-for="(profesional,index) in profesionales"
                    :key="profesional.rut"
                    :nombre="profesional.nombre"
                    :rut="profesional.rut"
                    :area="profesional.area"
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