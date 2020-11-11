
import React, { Component } from 'react';
import { View, Text } from 'react-native';
import { createStackNavigator,createAppContainer } from 'react-navigation';
//import ProfileScreen from './Profile';
//import PreferencesScreen from './Preferences';


export default class PreferencesScreen extends Component {
  render() {
  return (<View>
            <Text> Preferences </Text>
            <Text> Interested in </Text>
            <Text> Location </Text>
            <Text> Max Age </Text>
            <Text> Min Age </Text>
            <Text> Maximum Distance </Text>
          </View>
  );
}
}
