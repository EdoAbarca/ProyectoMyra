import axios from 'axios';
export const state = () => ({
    selectorArea: false,
    selectorCliente: false,
    selectorTurno: false,
    selectorCentro: false,
  })

  export const mutations = {
    modificarArea(state,valor){
        state.selectorArea = valor
    },
    modificarCentro(state,valor){
        state.selectorCentro = valor
    }
  }