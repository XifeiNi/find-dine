import React, { Component } from 'react';
import { View, Text, Button, TextInput, Image, Picker} from 'react-native';

export default class InterestedInField extends Component {
  state = {
    interestedIn: "Both"
  }

  onChange = (value) => {
    this.setState({
      interestedIn: value
    })
    this.props.changesMade();
  }
  render() {
    return (
      <>
      <Text> Interested In </Text>
        <Picker onValueChange={(value, position) => this.onChange(value)}
                selectedValue={this.state.interestedIn}>
          <Picker.Item label="Men" value="men" />
          <Picker.Item label="Women" value="women" />
          <Picker.Item label="Both" value="both" />
        </Picker>
        </>
      );
    }
}
