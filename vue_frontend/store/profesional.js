export const state = () => ({
    profesionalElegido:{
        nombre: "",
        rut: "",
        area:"",
        estado: false
    }
    
  })
export const getters = {
    getNombre(state) {
      return state.profesionalElegido.nombre
    },
    getRut(state) {
        return state.profesionalElegido.rut
    },
    getArea(state) {
        return state.profesionalElegido.area
    }
}
export const mutations = {
    elegir (state,profesional) {
      
        state.profesionalElegido.rut = profesional[0],
        state.profesionalElegido.nombre = profesional[1],
        state.profesionalElegido.area = profesional[2],
        state.profesionalElegido.estado = true,
        console.log(state.profesionalElegido.estado)

    }
      
  }
