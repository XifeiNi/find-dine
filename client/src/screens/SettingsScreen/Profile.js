import React, { Component, useState} from 'react';
import { View, Text, Button, TextInput } from 'react-native';
import styles from './index';
import Bio from './Bio';

export default class ProfileScreen extends Component {

  state = {
    bio: "",
    image: "",
    hasBeenChanged: false
  }

   saveChanges = () => {
  // postBio();
    this.props.navigation.pop();
  };

  updateProfileState = (bio, image, hasBeenChanged) => {
    if(hasBeenChanged) {
      this.setState({hasBeenChanged: true});
    }
  }


  render() {
    return (<View>
              <Text style={styles.title}> Profile </Text>
              <Text> Image (upload) </Text>
              <Text> Bio (max 200 char.)</Text>
              <Bio updateProfileState={this.updateProfileState}/>
              <Button title="Save" disable={this.state.hasBeenChanged}
                onPress={this.saveChanges}/>
          </View>
        );
    }
}
