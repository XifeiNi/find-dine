import React, { Component } from 'react';
import {
    View,
    TouchableWithoutFeedback,
    Keyboard
} from 'react-native';
import Toolbar from './Toolbar';
import InputModule from './InputModule';

export default class Messenger extends Component {
    onBackPress = () => {
        this.props.onBackPress();
    };

    dismissKeyboard = () => {
        Keyboard.dismiss();
    };

    render() {
        return (
            <View style={{ flex: 1 }}>
                <Toolbar onBackPress={this.onBackPress} />
                <TouchableWithoutFeedback onPress={this.dismissKeyboard}>
                    <View style={{ flex: 1 }} />
                </TouchableWithoutFeedback>
                <InputModule />
            </View>
        );
    }
}
