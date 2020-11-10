import React, { Component } from 'react';
import {  
    StyleSheet,
    Button,
    TextInput,
    Image,
    View
} from "react-native";

import  loginStyles  from "../styles";
import logoWithText from "../Assets/find_dine.png";

class Signup extends Component {
    state = {
        username: '', 
        password: '',
        confirmed: '',
        email: ''
    }

    onChangeText = (key, value) => {
        this.setState({
            [key] : value
        })
    }



    render() {
        var logoWithTextUri = Image.resolveAssetSource(logoWithText).uri;
        return (
        <View style={loginStyles.container}>
            <Image 
                source={{ uri: logoWithTextUri }}
                style={{ width:350, height: 270, marginBottom: 20}}
            />
            <TextInput
                style={loginStyles.input}
                placeholder='Username'
                autoCapitalize="none"
                placeholderTextColor='white'
                onChangeText={val => this.onChangeText('username', val)}
            />
            <TextInput
                style={loginStyles.input}
                placeholder='Email'
                autoCapitalize="none"
                placeholderTextColor='white'
                onChangeText={val => this.onChangeText('email', val)}
            />
            <TextInput
                style={loginStyles.input}
                placeholder='Password'
                secureTextEntry={true}
                autoCapitalize="none"
                placeholderTextColor='white'
                onChangeText={val => this.onChangeText('password', val)}
            />
            <TextInput
                style={loginStyles.input}
                placeholder='Confirm password'
                secureTextEntry={true}
                autoCapitalize="none"
                placeholderTextColor='white'
                onChangeText={val => this.onChangeText('confirmed', val)}
            />
            <Button
            title='Sign Up'
            onPress={this.signUp}
            />
        </View>
        )
    }
}

export default Signup;
