import axios from 'axios';
export const state = () => ({
    categoriaElegida: null,
    datoBuscadoPaciente: null,
    mostrarPac:false,
    idAnterior: false,
    historialAtencion:[],
    dataPacientes:[],
    dataPaciente:[],
    pagosProfesional:[],
    
  })
export const getters = {

    getCategoria(state){
        return state.categoriaElegida
    },
    getDatoBuscado(state){
        return state.datoBuscadoPaciente
    },
    getmostrarPac(state){
        return state.mostrarPac
    },
    getDatosBasicos(state){
        return state.datosPaciente
    },
    getHistorial(state){
        return state.profesionalesActivos
    }
}
export const mutations = {
    setPacientes(state,lista){
        
        state.dataPacientes = lista;
        console.log(state.dataPacientes);
    },
    setPaciente(state,datosPaciente){
        state.dataPaciente = datosPaciente;
        state.historialAtencion = datosPaciente.asistencias
        console.log( state.dataPaciente)
    },
    mostrar(state,id){
        const idAnterior = state.idAnterior
        if(idAnterior != id){
            state.mostrarPac = true
        }
        else{
            state.mostrarPac = true;
            state.idAnterior = id;
        }

        console.log(state.mostrarPac)
 
    },
    elegirCategoria(state,categoriaSeleccionada){
        state.categoriaElegida = categoriaSeleccionada;
    },
    setDatoPorBuscar(state,dato){
        state.datoBuscadoPaciente = dato;
    },
      
  }

  export const actions = {
    async fetchPacientes({ commit,state }) {
      const path = 'http://127.0.0.1:8000/api/paciente/';
      try {
        const res = await axios.get(path);
        const datos = res.data.pacientes;
        commit('setPacientes', datos);
        }  
      catch (error) {
        console.log(error);
        }

    },

    async fetchPaciente({ commit,state },id) {

        const id_profesional = id.toString();
        const path = 'http://127.0.0.1:8000/api/paciente/'+ id_profesional;
        try {
            const res = await axios.get(path);
            const datos = res.data.paciente;
            
            commit('setPaciente', datos);
            }  
          catch (error) {
            console.log(error);
            }

        
      },
    
      async buscarPaciente({ commit,state }) {

        const nombres = state.dataPacientes.filter(dataPacientes => dataPacientes.nombre.toLowerCase().search(state.datoBuscadoPaciente.toLowerCase())!=-1);
        //const ruts = state.dataPacientes.filter(dataPacientes => dataPacientes.rut.toLowerCase().search(state.datoBuscadoPaciente.toLowerCase())!=-1);
        
        const datos = nombres
        commit('setPacientes', datos);
      },

      async filtrarCliente({commit,state}) {
        if(state.categoriaElegida != null){
            const categoria = state.categoriaElegida.toString();

            const path = 'http://127.0.0.1:8000/api/filter-client-type/'+ categoria;
            try {
                const res = await axios.get(path);
                const datos = res.data.pacientes;
                
                commit('setPacientes', datos);
                }  
              catch (error) {
                console.log(error);
                }
        }
      },
      async filtrarTurnos({commit,state}) {
        if(state.categoriaElegida != null){
            const area = state.categoriaElegida.toString();

            const path = 'http://127.0.0.1:8000/api/filter-turn-type/'+ area;
            try {
                const res = await axios.get(path);
                const datos = res.data.pacientes;
                
                commit('setPacientes', datos);
                }  
              catch (error) {
                console.log(error);
                }
        }
      },
      async restaurarPacientes({commit}){
        commit('setPacientes', []);
      }
  }