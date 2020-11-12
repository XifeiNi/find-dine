
import React, { Component } from 'react';
import { View, Text, Button} from 'react-native';

export default class PreferencesScreen extends Component {
  saveChanges = () => {
    // do a post
   this.props.navigation.pop();
 };

  render() {
    return (<View>
              <Text> Preferences </Text>
              <Text> Interested in </Text>
              <Text> Location </Text>
              <Text> Max Age </Text>
              <Text> Min Age </Text>
              <Text> Maximum Distance </Text>
              <Button title="Save" onPress={this.saveChanges} />
            </View>
        );
    }
}
