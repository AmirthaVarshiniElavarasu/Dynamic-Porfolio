const path = require('path');

module.exports = {
  pages: {
    index: {
      entry: './src/main.js',
      template: 'public/index.html',
      filename: 'index.html'
    }
  },
  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname,'./')
      }
    }
  }
};
