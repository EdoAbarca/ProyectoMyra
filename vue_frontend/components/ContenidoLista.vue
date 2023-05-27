<script>
import { mapState } from 'vuex'
import { mapMutations } from 'vuex'
import { mapGetters } from 'vuex'
import ProfesionalLista from './ProfesionalLista.vue'

export default {
  data() {
        return {
          datos:[]
        }
    },
  components: {
    ProfesionalLista
    },
  computed:{
    ...mapGetters('profesional',[
            'getDatosProfesionales'       
        ])
  },

  }
</script>

<template>
    <div class="ContenedorLista">
        <div class="ContenedorTitulo">Lista de Profesionales</div>
        <div class ="ContenidoLista">
            <ul>
                <ProfesionalLista v-for="(prof) in getDatosProfesionales"
                    :key="prof.rut"
                    :nombre="prof.nombre"
                    :rut="prof.rut"
                    :area="prof.area"
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
}
.ContenedorTitulo{
    overflow: hidden;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 25px;
    background-color: #669098;

    border-radius: 12.5px 12.5px 0px 0px;
    color: white;

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