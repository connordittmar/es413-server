const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'console')
  },
  module: {
    loaders: [
      { test: /\.js$/,
          exclude: /node_modules/,
          loader: "babel-loader" },
      { test: /\.(png|svg|jpg|gif)$/,
      use: [
          'file-loader'
      ]}
        ]
  }
};
