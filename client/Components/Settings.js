
import React, {Component} from 'react';
import Profile from "./Profile";
import Preferences from "./Preferences"

import {
    StyleSheet,
    TouchableOpacity,
    Text,
    View
} from "react-native";

// this should already have all of the profile info
export default class Settings extends Component {
    render() {
        return (
            <View>
              <Profile />
              <Preferences />
            </View>
        );
    }
}
