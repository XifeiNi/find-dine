const { Component } = require("react");

import React from 'react';
import {
    StyleSheet,
    TouchableOpacity,
    Text,
    View
} from "react-native";

// this should already have all of the profile info
export default class Preferences extends Component {
    render() {
        return (
            <View>
              <Text>I'm interested in</Text>
              <Text>My location</Text>
              <Text> Age range </Text>
              <Text> Maximum distance </Text>
            </View>
        );
    }
}
