import React, { Component } from 'react';
import { View, Text, Button, TextInput } from 'react-native';
import styles from '../index';

export default class BioField extends Component {

  updateParentandCurrent = (text) => {
    this.props.updateProfileState(text);
  }

  render() {
    return (
              <View style={[{borderWidth: 3,
                            borderColor: '#4287f5',
                            borderRadius: 20}]}>
                <TextInput
                  multiline={true}
                  onChangeText={(text)=> this.updateParentandCurrent(text)}
                  value={this.props.value}
                />
              </View>
        );
    }
}
