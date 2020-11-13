import React, { Component } from 'react';
import { View, Text, Button, TextInput, Image, Picker} from 'react-native';

export default class InterestedInField extends Component {

  onChange = (value) => {
    this.props.onChange(value);
  }

  render() {
    return (
      <>
      <Text> Interested In {this.props.interestedIn}
 </Text>
        <Picker onValueChange={(value, position) => this.onChange(value)}
                selectedValue={this.props.value}>
          <Picker.Item label="Women" value="women" />
          <Picker.Item label="Men" value="men" />
          <Picker.Item label="Both" value="both" />
        </Picker>
        </>
      );
    }
}
