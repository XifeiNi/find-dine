const { Component } = require("react");

import React, { Component } from 'react';
import {
    StyleSheet,
    TouchableOpacity,
    Text,
    View
} from "react-native";

export default class Signin extends Component {
    render() {
        return (
            <View>
                <Text>
                    You are logged in
                </Text>
                <Button
                          onPress={this.props.onLogoutPress}
                          title="Logout"
                          />
            </View>
        );
    }
}
