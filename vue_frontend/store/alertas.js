//import axios from 'axios';
export const state = () => ({
    categoriaElegida: null,
    datoBuscado: null,
    mostrarAlerta:false,
    idAnterior: false,
    dataAlertas:[],
    dataAlerta:[], 
    copia:[],

    })


export const mutations = {
    setAlertas(state,lista){
        state.dataAlertas = lista;
        
    },
    setCopia(state,lista){
        state.copia = lista;
    },
    setAlerta(state,datosAlerta){
        state.dataAlerta = datosAlerta;
        console.log(datosAlerta)
    },
    mostrar(state,id){
        const idAnterior = state.idAnterior
        if(idAnterior != id){
            state.mostrar = true
        }
        else{
            state.mostrar = true;
            state.idAnterior = id;
        }
 
    },
    elegirCategoria(state,categoriaSeleccionada){
        state.categoriaElegida = categoriaSeleccionada;
    },
    setDatoPorBuscar(state,dato){
        state.datoBuscado = dato;
    },
      
  }

  export const actions = {
    async fetchAlertas({ commit }) {
      const path = 'http://localhost:8000/api/alerta/';
      try {
        const res = await this.$axios.get(path);
        const datos = res.data.alertas;
        commit('setCopia', datos);
        commit('setAlertas', datos);
        }  
      catch (error) {
        console.log(error);
        }
    },

    async fetchAlerta({ commit,state },id) {

        const id_Alerta = id.toString();
        const path = 'http://localhost:8000/api/alerta/' + id_Alerta;
        try {
            const res = await this.$axios.get(path);
            const datos = res.data.alerta;
            
            commit('setAlerta', datos);
            }  
          catch (error) {
            console.log(error);
            }
      },
    
      async buscarCoordinador({ commit,state }) {

        const nombres = state.dataAlertas.filter(dataAlertas => dataAlertas.nombreProfesional.toLowerCase().search(state.datoBuscadoCoord.toLowerCase())!=-1);
        const ruts = state.dataCoordinadores.filter(dataAlertas => dataAlertas.rut.toLowerCase().search(state.datoBuscadoCoord.toLowerCase())!=-1);
        
        const datos = nombres.concat(ruts);
        commit('setCoordinadores', datos);
      },

      async filtrarCentro({commit,state}) {
        if(state.categoriaElegida != null){
            const categoria = state.categoriaElegida.toString();

            const path = this.$config.filterCenterURL+ categoria;
            try {
                const res = await this.$axios.get(path);
                const datos = res.data.Coordinadores;
                
                commit('setCoordinadores', datos);
                }  
              catch (error) {
                console.log(error);
                }
        }
      },
      async filtrarArea({commit,state}) {
        if(state.categoriaElegida != null){
            const area = state.categoriaElegida.toString();

            const path = this.$config.filterPositionURL + area;
            try {
                const res = await this.$axios.get(path);
                const datos = res.data.Coordinadores;
                
                commit('setCoordinadores', datos);
                }  
              catch (error) {
                console.log(error);
                }
        }
      },
      async restaurarCoordinadores({commit}){
        commit('setCoordinadores', []);
      }
  }
  