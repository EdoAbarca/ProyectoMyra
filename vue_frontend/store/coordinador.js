//import this.$axios from 'this.$axios';
export const state = () => ({
    categoriaElegida: null,
    datoBuscadoCoord: null,
    mostrar:false,
    idAnterior: false,
    Coordinadores:[],
    dataCoordinadores:[],
    dataCoordinador:[],
  })

export const mutations = {
    setCoordinadores(state,lista){
        state.dataCoordinadores = lista;
    },
    setCoordinador(state,datoscoordinador){
        state.dataCoordinador = datoscoordinador;
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
        state.datoBuscadoCoord = dato;
    },
      
  }

  export const actions = {
    async fetchCoordinadores({ commit }) {
      const path = this.$config.coordinadorURL;
      try {
        const res = await this.$axios.get(path);
        const datos = res.data.coordinadores;
        commit('setCoordinadores', datos);
        }  
      catch (error) {
        console.log(error);
        }
    },

    async fetchCoordinador({ commit,state },id) {

        const id_coordinador = id.toString();
        const path = this.$config.coordinadorURL+ id_coordinador;
        try {
            const res = await this.$axios.get(path);
            const datos = res.data.coordinador;
            
            commit('setCoordinador', datos);
            }  
          catch (error) {
            console.log(error);
            }
      },
    
      async buscarCoordinador({ commit,state }) {

        const nombres = state.dataCoordinadores.filter(dataCoordinadores => dataCoordinadores.nombre.toLowerCase().search(state.datoBuscadoCoord.toLowerCase())!=-1);
        const ruts = state.dataCoordinadores.filter(dataCoordinadores => dataCoordinadores.rut.toLowerCase().search(state.datoBuscadoCoord.toLowerCase())!=-1);
        
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
  