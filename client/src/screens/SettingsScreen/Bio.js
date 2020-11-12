import React, { Component } from 'react';
import { View, Text, Button, TextInput } from 'react-native';
import styles from './index';

export default class Bio extends Component {
  state = {
    value: "Hello"
  }

  updateParentandCurrent = (text) => {
    this.setState({value: text});
    this.props.updateProfileState();
  }

  render() {
    return (<TextInput
              onChangeText={(text)=> this.updateParentandCurrent(text)}
              value={this.state.value}/>
        );
    }
}
