/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/base.html',

    //html files
    './users/templates/**/*.html',
    './rooms/templates/**/*.html',
    './bookings/templates/**/*.html',


  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

