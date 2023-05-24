export const state = () => ({
    datosProfesional:{
        nombre: "",
        rut: "",
        area:"",
        cargo:'',
        contrato:'',
        coordinador:''
    },
    pagoProfesional:{
        sueldoBase:"",
        gratificaciones: "",
        descuentos:""
    },
    estProfesional:{
        inasistencias:"",
        horasTotales:"",
        horasExtra:"",
        diasLicencia:"",
        diasVacaciones:""
    },
    categoriaElegida: null,
    datoBuscadoProfesional: null,
    mostrar:false,
    idAnterior: false,
    profesionales:[
        { nombre: "Natalia Damaris Perello Contreras",
          rut:"19456957-5",
          area:"ADMINISTRACION", //Centro de trabajo
        },
        { nombre: "Mariela Leonardo Tantarico",
          rut:"20345687-7",
          area:"CUIDADOS",
        },
        { nombre: "Will Hermes Torrealba Alvarez",
          rut:"9234876-0",
          area:"CUIDADOS",
        },
        { nombre: "Angelina Elizabeth Cespedes Cortes",
          rut:"14987436-7",
          area:"KINESIOLOGIA",
        }

      ],
    pagos:[
        { rut:'19456957-5',
          sueldoBase:"1.200.000",
          gratificaciones: "50.000",
          descuentos:"45.000"
        },
        { rut:'20345687-7',
          sueldoBase:"1.903.000",
          gratificaciones: "530.000",
          descuentos:"445.000"
        },
        { rut:'9234876-0',
          sueldoBase:"123.567",
          gratificaciones: "5.220.000",
          descuentos:"435.000"
        },
        { rut:'14987436-7',
          sueldoBase:"1.900.000",
          gratificaciones: "12.350.000",
          descuentos:"45.344"
        }
    ],
    estadisticas:[
        { rut:'19456957-5',
            inasistencias:"0",
            horasTotales:"400",
            horasExtra:"35",
            diasLicencia:"7",
            diasVacaciones:"45"
        },
        { rut:'20345687-7',
            inasistencias:"3",
            horasTotales:"90",
            horasExtra:"56",
            diasLicencia:"7",
            diasVacaciones:"3"
        },
        { rut:'9234876-0',
            inasistencias:"0",
            horasTotales:"350",
            horasExtra:"78",
            diasLicencia:"0",
            diasVacaciones:"0"
        },
        { rut:'14987436-7',
            inasistencias:"1",
            horasTotales:"290",
            horasExtra:"35",
            diasLicencia:"15",
            diasVacaciones:"0"
        }
    ]


    
  })
export const getters = {

    getCategoria(state){
        return state.categoriaElegida
    },
    getDatoBuscado(state){
        return state.datoBuscadoProfesional
    },
    getMostrar(state){
        return state.mostrar
    },
    getPagos(state){
        return state.pagoProfesional
    },
    getEstadisticas(state){
        return state.estProfesional
    },
    getDatosBasicos(state){
        return state.datosProfesional
    },
    getProfesionales(state){
        return state.profesionales
    },
    getDatosProfesionales(state){
        
    
        if(state.categoriaElegida === null && state.datoBuscadoProfesional===null){
            return state.profesionales
        }

        if(state.categoriaElegida != null){
            return state.profesionales.filter(profesionales => profesionales.area === state.categoriaElegida);
        }
        if(state.datoBuscadoProfesional!=null){
            const nombres = state.profesionales.filter(profesionales => profesionales.nombre.toLowerCase().search(state.datoBuscadoProfesional.toLowerCase())!=-1);
            const ruts = state.profesionales.filter(profesionales => profesionales.rut.toLowerCase().search(state.datoBuscadoProfesional.toLowerCase())!=-1);
          
            const resultado = nombres.concat(ruts);
            
            return resultado
        }
        return null;
        
    }
}
export const mutations = {
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
    datoPorBuscar(state,dato){
        state.datoBuscadoProfesional = dato;
    },
    recuperarDatos(state,rut){
        const datosBasicos = state.profesionales.find(profesionales => profesionales.rut === rut);
        const datosEstadisitcos = state.estadisticas.find(estadisticas => estadisticas.rut === rut);
        const datosPagos = state.pagos.find(pagos => pagos.rut === rut);
        console.log(datosBasicos)

        //console.log(datosBasicos);
        state.datosProfesional.nombre = datosBasicos.nombre;
        state.datosProfesional.rut = datosBasicos.rut;
        state.datosProfesional.area = datosBasicos.area;

        console.log(state.datosProfesional);


        state.estProfesional.inasistencias = datosEstadisitcos.inasistencias;
        state.estProfesional.horasExtra = datosEstadisitcos.horasExtra;
        state.estProfesional.horasTotales = datosEstadisitcos.horasTotales;

        state.pagoProfesional.sueldoBase = datosPagos.sueldoBase;
        state.pagoProfesional.gratificaciones = datosPagos.gratificaciones;
        state.pagoProfesional.descuentos = datosPagos.descuentos;

    }
      
  }
