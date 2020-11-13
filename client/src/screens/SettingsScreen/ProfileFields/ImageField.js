import React, { Component } from 'react';
import { View, Text, Button, TextInput, Image } from 'react-native';
import styles from '../index';

export default class ImageField extends Component {

  // show current image(s)
  // press to change image
  // save option

  render() {
    return (
        <Image style={imageStyle} source={require('./steak.jpg')} />
      );
    }
}



const imageStyle = [
  {
    maxWidth: 325,
    maxHeight: 325,
    marginBottom: 10,
    overflow: 'hidden',
    borderRadius: 10
  }
]
