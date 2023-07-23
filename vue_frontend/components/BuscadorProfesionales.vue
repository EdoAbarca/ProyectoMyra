<script>
import DropBoxCentro from './DropBoxCentro.vue'
import DropBoxArea from './DropBoxArea.vue'
import {mapMutations, mapActions, mapState} from 'vuex'


export default {
    props:['page']
    ,
    data(){
        return{
            datoBuscado:null

        }
    },
    components: {
    DropBoxCentro,
    DropBoxArea,

},
    methods:{
        ...mapState('profesional',[
            'dataProfesionales'       
        ]),
        ...mapMutations({
            setDatoPorBuscar: 'profesional/setDatoPorBuscar'
        }),

        ...mapMutations({
            setDatoPorBuscarPaci: 'paciente/setDatoPorBuscar'
        }),

        ...mapMutations({
            setDatoPorBuscarCoord: 'coordinador/setDatoPorBuscar'
        }),
        ...mapActions('profesional',[
            'fetchProfesionales',
            'buscarProfesional'       
        ]),

        ...mapActions('paciente',[
            'fetchPacientes',
            'buscarPaciente'       
        ]),

        ...mapActions('coordinador',[
            'fetchCoordinadores',
            'buscarCoordinador'       
        ]),
        
        buscarProfesionales(){
            if(this.datoBuscado ===''){
                this.setDatoPorBuscar(null);
                this.fetchProfesionales();
            }
            else{
                
                this.setDatoPorBuscar(this.datoBuscado);
                this.buscarProfesional();    
            } 

        },
        buscarPacientes(){
            if(this.datoBuscado ===''){
                this.setDatoPorBuscarPaci(null);
                this.fetchPacientes();
            }
            else{
                
                this.setDatoPorBuscarPaci(this.datoBuscado);
                this.buscarPaciente();
                console.log(this.dataPacientes)     
            } 
        },
        buscarCoordinadores(){
            if(this.datoBuscado ===''){
                this.setDatoPorBuscarCoord(null);
                this.fetchCoordinadores();
            }
            else{
                
                this.setDatoPorBuscarCoord(this.datoBuscado);
                this.buscarCoordinador();
                console.log(this.dataPacientes)     
            } 
        },
        buscar(){
            if(this.page === 'profesionales'){
                this.buscarProfesionales();
            }
            else if (this.page === 'pacientes'){
                this.buscarPacientes();
            }
            else if (this.page === 'coordinadores'){
                this.buscarCoordinadores();
            }  
        }

    }
  }
</script>

<template>
    <div class="ContenedorBuscador">
        <div class="BarraBusqueda">
            <input type="search" placeholder="Buscar un individuo" id="buscador" v-model="datoBuscado" @keyup.enter="buscar()"/>
            <div class="BotonBusqueda" @click="buscar()" ><img class="lupa" src="../static/iconolupa.svg" alt=""></div>
        </div>
        <div class="BarraFiltro" v-if="page==='profesionales'">
            <DropBoxCentro :page="page" />
            <DropBoxArea :page="page" />
            
            
        </div>
        <div class="BarraFiltro" v-if="page==='pacientes'">
            <DropBoxCentro :page="page" />
            <DropBoxArea :page="page" />
        </div>
    </div>
</template>

<style>
.ContenedorBuscador{
    position: relative;
    display: flex;
    flex-direction: column;

    width: 90%;
    height: 80px;
    font-family: Arial, Helvetica, sans-serif;
    
}
.BarraBusqueda{
    
    position: relative;
    display: flex;
    width: 100%;
    height: 60%;
    min-width: 500px;

    border-radius: 8px 8px 8px 0px;
    background-color: #D9D9D9;
    
    flex-direction: row;
    align-items: center;
    filter: drop-shadow(0px 1px 1px rgba(0, 0, 0, 0.1));
}
.BarraFiltro{
    position: relative;
    display: flex;
    width: 100%;
    height: 40%;
}
.BotonBusqueda{
    position: relative;
    display: flex;
    width: 10%;
    height:28px;

    align-items: center;
    justify-content: center;
    z-index: -200;
    cursor: pointer;


}
.BotonBusqueda::before{
    align-items: center;
    display: flex;
    position: absolute;
    content: '';
    background-color: #D9D9D9;
    width: 100px;
    height: 28px;
    right: 20px;
    z-index: -20;
    border-radius: 0px 8px 8px 8px;
    transition: all 200ms linear;
}
.BotonBusqueda:hover::before{
    background-color: #919191;

}

.BotonBusqueda::after{
    align-items: center;
    display: flex;
    position: absolute;
    content: '';
    background-color: #48abbf;
    width: 0;
    height: 28px;
    left: -20px;
    z-index: -20;
    border-radius: 0px 8px 8px 8px;
    transition: all 200ms linear;
}

.BotonBusqueda:hover::after{

    width:100%
}

.lupa{
    width: 20px;
    height: 20px;
    right: 10px;
    position: relative;
    z-index: 200;
}
#buscador{
    position: relative;
    width: 90%;
    height: 25px;
    display: flex;
    border-radius: 8px;
    margin-left: 18px;
    padding-left: 8px;
    padding-right: 2%;
    border: #D9D9D9 2px solid ;
    transition: all 200ms linear;


    background-color: white;
    color: #919191;
    
    outline: none;
}
#buscador:focus, #buscador:hover{
    background-color: white;
    height: 25px;
    border: #C4C4C4 2px solid ;
    
}
#buscador::placeholder{
    font-size: 12px;
    font-weight: 600;
    color: #D9D9D9;
    transition: all 200ms linear;
}
#buscador:hover::placeholder{
    font-size: 12px;
    font-weight: 600;
    color: gray;
}

#buscador:hover ~ .BotonBusqueda::before{
    background-color: #C4C4C4;
}
#buscador:focus ~ .BotonBusqueda::before{
    background-color: #C4C4C4;
}

</style>