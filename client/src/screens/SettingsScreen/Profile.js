import React, { Component } from 'react';
import { View, Text } from 'react-native';
import { createStackNavigator,createAppContainer } from 'react-navigation';
//import ProfileScreen from './Profile';
//import PreferencesScreen from './Preferences';



export default class ProfileScreen extends Component {
  render() {
  return (<View>
              <Text> Profile </Text>
              <Text> Image </Text>
              <Text> Bio </Text>
              <Text> Favourite Cuisine </Text>
          </View>
  );
}
}
