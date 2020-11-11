import React, { Component } from 'react';
import { View, Text, Button } from 'react-native';
import { createStackNavigator,createAppContainer } from 'react-navigation';
import ProfileScreen from './Profile';
import PreferencesScreen from './Preferences';
//import PreferencesScreen from './Preferences';


const SettingsScreen = ({navigation}) => {
        return (
            <View>
                <Text> Settings</Text>
                <Text> Profile button </Text>
                <Button
                  title="Edit Profile"
                  onPress={()=>navigation.navigate('Prof')}
                  />
                <Text> Preferences Button </Text>
                <Button
                  title="Edit Preferences"
                  onPress={()=>navigation.navigate('Pref')}
                  />
                <Text> Logout </Text>
            </View>
        );
}



const SettingsApp = createStackNavigator({
    Prof: {
        screen: ProfileScreen
    },
    Pref: {
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


const SettingsDefaultScreen = () => {
  return (<Text> Settings default screen </Text>);
}

export default createAppContainer(SettingsApp);
