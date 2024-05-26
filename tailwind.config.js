module.exports = {
  content: ["./index.html"],
  darkMode: 'selector',
  theme: {
   fontFamily: {
    'body': ['"Poppins', 'sans-serif']
   },
    container: {
      center: true,
      padding: '12px'
    },
    extend: {
      colors: {
        primary: '#78716c',
        secondary: '#949494',
       'secondary-2': '#afafaf',
        dark: '#1c1917',
        'second-dark': '#262626'
      },
      screens: {
        '2xl': '1320px'
      }
    },
  },
  plugins: [],

}