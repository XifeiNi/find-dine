import { Component } from 'react';
import { Image, TextInput } from 'react-native';

import styles from './styles';
import logoWithText from '../../assets/images/find_dine.png';
import PropTypes from 'prop-types';

export default class SplashScreen extends Component {
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

    onPress = () => {
        const { navigation } = this.props;
        navigation.navigate('MainScreen');
    };
/
    render() {
        var logoWithTextUri = Image.resolveAssetSource(logoWithText).uri;
        return (
            <SafeAreaView style={styles.container}>
                <Image 
                    source={{ uri: logoWithTextUri }}
                    style={{ width:350, height: 270, marginBottom: 20}}
                />
                <TextInput
                    style={styles.input}
                    placeholder='Username'
                    autoCapitalize="none"
                    placeholderTextColor='white'
                    onChangeText={val => this.onChangeText('username', val)}
                />
                <TextInput
                    style={styles.input}
                    placeholder='Password'
                    secureTextEntry={true}
                    autoCapitalize="none"
                    placeholderTextColor='white'
                    onChangeText={val => this.onChangeText('password', val)}
                />
                <Button raised color="#0084ff" onPress={this.onPress}>
                    Login
                </Button>
              
            </SafeAreaView>
        );
    }
}

SplashScreen.propTypes = {
    navigation: PropTypes.object
};
