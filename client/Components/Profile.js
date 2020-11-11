const { Component } = require("react");

import React from 'react';
import {
    StyleSheet,
    TouchableOpacity,
    Text,
    View
} from "react-native";

// this should already have all of the profile info
export default class Profile extends Component {

    render() {
        return (
            <View>
              <Text>name</Text>
              <Text>pics</Text>
              <Text>bio</Text>
              { this.state.isEditing ?
                <TextInput
                  value={this.state.txt}
                  onChangeText={(value) => this.setState({ txt: value })}
                  autoFocus
                  onBlur={() => this.setState({ isEditing: false })}
                /> :
                <Text
                  style={styles.t2}
                  onPress={() => this.setState({ isEditing: true })}
                  >
                    {this.state.txt}
                  </Text>
                }
              <Text> age </Text>

              <Text> favourite food, second favourite food </Text>

              <Text> Save button </Text>
            </View>
        );
    }
}
