module.exports = {
  content: ["./**/*.html"],
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
        secondary: '#787878',
       'secondary-2': '#afafaf',
        dark: '#1c1917',
        'second-dark': '#262626'
      },
      screens: {
        '2xl': '1320px'
      }
    },
  },
  plugins: [require('/data/data/com.termux/files/home/node_modules/flowbite/plugin')],

}