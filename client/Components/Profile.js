const { Component } = require("react");

import React, { Component } from 'react';
import {
    StyleSheet,
    TouchableOpacity,
    Text,
    View
} from "react-native";

// this should already have all of the profile info
export default class Profile extends Component {
    const {
      name,
      age,
      image,
      bio,
      gender,
      genderPreference,
      favouriteCuisine
    } = UserInfo[7]
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
