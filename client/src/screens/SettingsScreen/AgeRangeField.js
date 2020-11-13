import React, { Component } from 'react';
import { View, Text, Button, TextInput, Image, Picker} from 'react-native';

export default class AgeRangeField extends Component {

  ages = () => {
    var age = 18
    var list = []
    while (age < 100) {
      list.push(age)
      age = age + 1
    }
    return list
  }


  onMinValueChange = (value) => {
      this.props.onMinChange(value)
  }

  onMaxValueChange = (value) => {
    this.props.onMaxChange(value)
  }

  render() {
    return (
        <View>
        <Text> Minimum Age </Text>
        <Picker onValueChange={(value, position) => this.onMinValueChange(value)}
                selectedValue={'' + this.props.minAge}>
        {this.ages().map((index) => (
          <Picker.Item label={'' + index} value={'' + index}
        />
        ))}
        </Picker>
        <Text> Maximum Age </Text>
        <Picker onValueChange={(value, position) => this.onMaxValueChange(value)}
                selectedValue={'' + this.props.maxAge}>
        {this.ages().map((index) => (
          <Picker.Item label={'' + index} value={'' + index} />
        ))}
        </Picker>
        </View>

      );
    }
}


// age range 18 to 99
