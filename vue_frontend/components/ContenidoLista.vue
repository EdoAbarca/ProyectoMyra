<script>
import { mapState, mapActions, mapMutations, mapGetters } from 'vuex'
import ProfesionalLista from './ProfesionalLista.vue'
import PacienteLista from './PacienteLista.vue'
import axios from 'axios'

import CoordinadorLista from './CoordinadorLista.vue'
export default {
  name: 'ListaDeContenidos',
  props:['page'],
  data() {
        return {
          datos:[]
        }
    },
  components: {
    ProfesionalLista,
    PacienteLista,
    CoordinadorLista
},
  computed:{

    ...mapState('profesional',[
            'dataProfesionales'       
        ]),
    ...mapState('paciente',[
            'dataPacientes'       
        ]),
    ...mapState('coordinador',[
            'dataCoordinadores'       
        ]),
    ...mapActions('profesional',[
            'fetchProfesionales',
            'restaurarProfesionales'       
        ]), 
    ...mapActions('paciente',[
            'fetchPacientes',      
        ]),
    ...mapActions('coordinador',[
            'fetchCoordinadores',      
        ]),     
  },
  mounted(){
    if(this.page === 'profesionales'){
      this.fetchProfesionales;
    }
    else if (this.page === 'pacientes'){
      this.fetchPacientes;
    }
    else if(this.page === 'coordinadores'){
      this.fetchCoordinadores;
    }
    else{
      this.restaurarProfesionales;
    }
  }
}
</script>

<template>
    <div class="ContenedorLista">
        <div class="ContenedorTitulo" v-if="this.page === 'profesionales'">
          <h1 id="tituloCentro">Centro</h1>
          <h1 id="tituloArea">Área</h1>
          <h1 id="tituloNombreProfesional">Profesional</h1>
          <h1 id="tituloRutProfesional">Rut</h1> 
        </div>
        <div class="ContenedorTitulo" v-if="this.page === 'pacientes'">
          <h1 id="tituloCentro">Cliente</h1>
          <h1 id="tituloArea">Turno</h1>
          <h1 id="tituloNombreProfesional">Paciente</h1>
          <h1 id="tituloRutProfesional">Rut</h1> 
        </div>

        <div class="ContenedorTitulo" v-if="this.page === 'coordinadores'">
          <h1 id="tituloCentro">Centro</h1>
          <h1 id="tituloArea"></h1>
          <h1 id="tituloNombreProfesional">Coordinador</h1>
          <h1 id="tituloRutProfesional">Rut</h1> 
        </div>

        <div class ="ContenidoLista">
            <ul v-if="this.page === 'profesionales'">
                <ProfesionalLista v-for="(prof) in dataProfesionales"
                    :key="prof.id"
                    :nombre="prof.nombre"
                    :rut="prof.rut"
                    :area="prof.idArea_id"
                    :centro="prof.idCentro_id"
                    :id="prof.id"
                />
            </ul>
            
            <ul v-if="this.page === 'pacientes'">
                <PacienteLista v-for="(paciente) in dataPacientes"
                    :key="paciente.id"
                    :nombre="paciente.nombre"
                    :rut="paciente.rut"
                    :cliente="paciente.idCliente_id"
                    :turno="paciente.idTipoTurno_id"
                    :id="paciente.id"
                />
            </ul>


            <ul v-if="this.page === 'coordinadores'">
                <CoordinadorLista v-for="(coord) in dataCoordinadores"
                    :key="coord.id"
                    :nombre="coord.nombre"
                    :rut="coord.rut"
                    :centro="coord.idCentro_id"
                    :id="coord.id"
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
    margin-top: 1%;
    width: 100%;
    height: 82%;
    top: 0;
    background-color: white;
    border-radius: 12.5px;
    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.15));
    z-index: 1;
}
.ContenedorTitulo{

    position: relative;
    display: flex;
    align-items: center;
    width: 100%;
    height: 25px;
    background-color: #669098;

    border-radius: 12.5px 12.5px 0px 0px;
    color: white;

    
}
.ContenidoLista{
    margin-left: 1%;
    position: relative;
    height: 100%;
    overflow-y: scroll;

    filter: drop-shadow(0px 1px 1px rgba(0, 0, 0, 0.1));

}
#tituloCentro,#tituloArea{
  display: flex;
  position: relative;
  width: 16%;
  min-width: 110px;
  justify-content: center;

  font-family: Arial, Helvetica, sans-serif;
  font-size: 13px;
  font-weight: 600;
  margin-left: 1%;
}
#tituloNombreProfesional{
  width: 45%;
  text-align: left;
  margin-left: 3%;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 13px;
  font-weight: 600;
}
#tituloRutProfesional{
  width: 20%;
  text-align: left;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 13px;
  font-weight: 600;
  padding-left: 1%;
}
</style>