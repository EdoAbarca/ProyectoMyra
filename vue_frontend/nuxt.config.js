export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Puerto para nuxt app
  /* 
  server: {
    port:8080,
  },*/

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'vue_frontend',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    '@nuxtjs/vuetify'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    '@nuxtjs/auth'
  ],



  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    BaseURL : 'http://localhost:8000/api',
    //proxy: true,
  },
/* 
  proxy: {
    "/signup": 'http://localhost:8000/api',
    "/signin": 'http://localhost:8000/api',
    "/signout": 'http://localhost:8000/api',
    "/cargar_excel": 'http://localhost:8000/api'
  },
*/
  auth: {
    strategies: {
      local: {
        endpoints: {
          login: { url: 'http://localhost:8000/api/signin', method: 'post', propertyName: 'data.token' },
          //user: { url: 'me', method: 'get', propertyName: 'data' },
          logout: {url: 'http://localhost:8000/api/signout', method: 'post'}
        }
      }
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
