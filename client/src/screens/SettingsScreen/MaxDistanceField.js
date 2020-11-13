import React, { Component } from 'react';
import { View, Text, Button, TextInput, Image, Picker} from 'react-native';

export default class MaxDistanceField extends Component {
  state = {
    distance: "50"
  }
  onChanged = (text) => {
    if (/^\d+$/.test(text)) {
      this.setState({
        distance: text
      });
    }
    this.props.changesMade();
  }
  render() {
    return (
        <>
        <Text>Maximum Distance</Text>
        <TextInput
          keyboardType='numeric'
          value={this.state.distance}
          onChangeText={(text)=>this.onChanged(text)}
          maxLength={3}/>
          </>
      );
    }
}


// reproduced with permission https://stackoverflow.com/questions/32946793/react-native-textinput-that-only-accepts-numeric-characters
