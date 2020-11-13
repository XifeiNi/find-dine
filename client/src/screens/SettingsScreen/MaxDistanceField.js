import React, { Component } from 'react';
import { View, Text, Button, TextInput, Image, Picker} from 'react-native';

export default class MaxDistanceField extends Component {

  onChange = (value) => {
    this.props.onChange(value)
  }
  distances = () => {
    var distance = 1
    var distanceList = []
    while (distance < 100) {
      distanceList.push(distance)
      distance = distance + 1
    }
    return distanceList
  }

  render() {
    return (
        <>
        <Text>Maximum Distance</Text>
        <Picker onValueChange={(value, position) => this.onChange(value)}
                selectedValue={'' + this.props.value}>
        {this.distances().map((index) => (
          <Picker.Item label={'' + index} value={'' + index}
        />
        ))}
        </Picker>
        </>
      );
    }
}


// reproduced with permission https://stackoverflow.com/questions/32946793/react-native-textinput-that-only-accepts-numeric-characters
