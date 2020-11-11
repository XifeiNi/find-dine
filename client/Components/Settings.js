const { Component } = require("react");

import React, { Component } from 'react';
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
              <Button>Profile</Button>
              <Button>Preferences</Button>
            </View>
        );
    }
}
