import React, { Component } from 'react';
import { View, Text, Button, TextInput, Image, Picker} from 'react-native';

export default class AgeRangeField extends Component {

  state = {
    minAge: 18,
    maxAge: 99
  }

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
    if (value > this.state.maxAge) {
      this.setState({maxAge: value})
    }
    this.setState({minAge: value})
  }

  onMaxValueChange = (value) => {
    if (value < this.state.minAge) {
      this.setState({minAge: value})
    }
    this.setState({maxAge: value})
  }

  render() {
    return (
        <View>
        <Text> Minimum Age </Text>
        <Picker onValueChange={(value, position) => this.onMinValueChange(value)}
                selectedValue={this.state.minAge}>
        {this.ages().map((index) => (
          <Picker.Item label={''+index} value={''+index}
        />
        ))}
        </Picker>
        <Text> Maximum Age </Text>
        <Picker onValueChange={(value, position) => this.onMaxValueChange(value)}
                selectedValue={this.state.maxAge}>
        {this.ages().map((index) => (
          <Picker.Item label={''+index} value={''+index} />
        ))}
        </Picker>
        </View>

      );
    }
}


// age range 18 to 99
