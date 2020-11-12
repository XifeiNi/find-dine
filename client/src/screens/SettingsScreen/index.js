import React, { Component } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { createStackNavigator,createAppContainer } from 'react-navigation';
import ProfileScreen from './Profile';
import PreferencesScreen from './Preferences';


const SettingsScreen = ({navigation}) => {
        return (
            <View>
                <Text style={styles.title}> Settings</Text>
                <Button
                  title="Profile"
                  style={styles.buttonStyle}
                  onPress={()=>navigation.navigate('Profile')}
                  />
                <Button
                  title="Preferences"
                  onPress={()=>navigation.navigate('Preferences')}
                  />
                <Button title="Logout" />
            </View>
        );
}

export const styles = StyleSheet.create({
  title: {
    fontSize: 60,
    color: 'black',
    fontWeight: 'bold'
  },
  buttonStyle: {
    maxWidth: 30,
    borderRadius: 5,
    color: 'black',
    backgroundColor: 'white',
    borderWidth: 5,
    borderStyle: 'solid'
  }
});

const SettingsApp = createStackNavigator({
    Profile: {
        screen: ProfileScreen
    },
    Preferences: {
        screen: PreferencesScreen
    },
    Default: {
        screen: SettingsScreen
    }
},
{
  initialRouteName: "Default"
}

);

export default createAppContainer(SettingsApp);
