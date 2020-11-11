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
    const {
      interestedIn,
      location,
      maximumDistance,
      maxAge,
      minAge
    } = UserPreferences[5]
    render() {
        return (
            <View>
              <Text>{name}</Text>
              <Text>{age}</Text>
              <Text>{bio}</Text>
            </View>
        );
    }
}
