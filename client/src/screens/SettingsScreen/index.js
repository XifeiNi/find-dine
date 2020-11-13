import React, { Component } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { createStackNavigator,createAppContainer } from 'react-navigation';
import ProfileScreen from './Profile';
import PreferencesScreen from './Preferences';
import SplashScreen from '../SplashScreen';


const SettingsScreen = ({navigation}) => {
        return (
            <View>
                <Text style={styles.title}> Settings</Text>
                <View style={styles.buttonViewStyle}>
                  <Button
                    title="Profile"
                    onPress={()=>navigation.navigate('Profile')}
                  />
                </View>
                <View style={styles.buttonViewStyle}>
                  <Button
                    style={styles.buttonStyle}
                    title="Preferences"
                    onPress={()=>navigation.navigate('Preferences')}
                  />
                </View>
                <View style={styles.buttonViewStyle}>
                  <Button title="Logout" 
                  onPress={()=>navigation.navigate('Splash')}/>
                </View>
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
    borderRadius: 10
  },
  buttonViewStyle: {
    width: 300,
    marginTop: 20,
    marginLeft: 20
  },
  smallText: {
    fontSize: 30,
    color: 'black'
  }
});

const SettingsApp = createStackNavigator({
    Profile: {
        screen: ProfileScreen
    },
    Preferences: {
        screen: PreferencesScreen
    },
    Splash: {
      screen: SplashScreen
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
